#!/usr/bin/env python3
"""
Search recent papers for thesis topics defined in refs/SEARCH_TOPICS.csv.

This version is stricter than the initial scaffold:
- Crossref is used as the default source because its REST API is public.
- It fetches a wider candidate pool, then scores and filters locally.
- It rejects obvious drift, future years, and weak title matches.
- It writes a Markdown report for manual review.

This script belongs to the Literature workstream.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import pathlib
import re
import urllib.parse
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
SEARCH_TOPICS_PATH = ROOT / "refs" / "SEARCH_TOPICS.csv"
REPORTS_DIR = ROOT / "reports"
DEFAULT_DAYS = 30
QUERY_ROWS = 40
MAX_RESULTS_PER_TOPIC = 8
STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}
VENUE_HINTS = {
    "robot",
    "robotics",
    "rehabilitation",
    "biomechanics",
    "neuroengineering",
    "biomedical",
    "mechatronics",
    "mechanism",
    "machine theory",
    "prosthetic",
    "bionics",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS)
    parser.add_argument("--topic", help="Only search a single topic_id")
    return parser.parse_args()


def split_phrases(value: str) -> list[str]:
    return [part.strip().lower() for part in value.split(";") if part.strip()]


def tokenize(value: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", value.lower())
    return {word for word in words if len(word) >= 4 and word not in STOPWORDS}


def load_topics(topic_filter: str | None) -> list[dict[str, str]]:
    with SEARCH_TOPICS_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    active_rows = [row for row in rows if row["status"].strip().lower() == "active"]
    if topic_filter:
        active_rows = [row for row in active_rows if row["topic_id"].strip() == topic_filter]
    return active_rows


def crossref_query_url(topic: dict[str, str], since_date: dt.date) -> str:
    query_terms = []
    query_terms.extend(split_phrases(topic["keywords_any"]))
    query_terms.extend(split_phrases(topic["keywords_all"]))
    params = {
        "query.bibliographic": " ".join(query_terms),
        "filter": f"from-pub-date:{since_date.isoformat()}",
        "rows": str(QUERY_ROWS),
        "sort": "published",
        "order": "desc",
        "select": "DOI,title,author,container-title,published-print,published-online,URL,subject,type",
    }
    mailto = os.environ.get("CROSSREF_MAILTO")
    if mailto:
        params["mailto"] = mailto
    return "https://api.crossref.org/works?" + urllib.parse.urlencode(params)


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "soft-finger-thesis-literature-watch/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_year(item: dict) -> str:
    for field in ("published-print", "published-online"):
        parts = item.get(field, {}).get("date-parts", [])
        if parts and parts[0]:
            return str(parts[0][0])
    return ""


def extract_authors(item: dict) -> str:
    authors = []
    for author in item.get("author", [])[:4]:
        given = author.get("given", "").strip()
        family = author.get("family", "").strip()
        full_name = " ".join(part for part in (given, family) if part)
        if full_name:
            authors.append(full_name)
    return "; ".join(authors)


def score_item(topic: dict[str, str], item: dict) -> tuple[int, list[str]]:
    title = ((item.get("title") or [""]) or [""])[0].lower()
    venue = ((item.get("container-title") or [""]) or [""])[0].lower()
    subjects = " ".join(item.get("subject", [])).lower()
    text = " ".join(part for part in (title, venue, subjects) if part)
    exact_any = split_phrases(topic["keywords_any"])
    exact_all = split_phrases(topic["keywords_all"])
    exclude_terms = split_phrases(topic["exclude_terms"])
    topic_tokens = tokenize(topic["keywords_any"] + " " + topic["keywords_all"])
    title_tokens = tokenize(title)
    text_tokens = tokenize(text)
    score = 0
    reasons = []

    current_year = dt.date.today().year
    year = extract_year(item)
    if year and int(year) > current_year:
        return -999, [f"future year {year}"]

    if any(exclude in text for exclude in exclude_terms):
        return -999, ["matched excluded term"]

    any_title_matches = [phrase for phrase in exact_any if phrase and phrase in title]
    any_text_matches = [phrase for phrase in exact_any if phrase and phrase in text and phrase not in any_title_matches]
    all_text_matches = [phrase for phrase in exact_all if phrase and phrase in text]
    title_overlap = sorted(topic_tokens & title_tokens)
    text_overlap = sorted(topic_tokens & text_tokens)
    venue_hint_hits = [hint for hint in VENUE_HINTS if hint in venue]

    if any_title_matches:
        score += 6 + len(any_title_matches)
        reasons.append(f"title phrases: {', '.join(any_title_matches[:3])}")
    if any_text_matches:
        score += 2 * len(any_text_matches)
        reasons.append(f"text phrases: {', '.join(any_text_matches[:3])}")
    if all_text_matches:
        score += 2 * len(all_text_matches)
        reasons.append(f"required anchors: {', '.join(all_text_matches[:3])}")
    if title_overlap:
        score += len(title_overlap)
        reasons.append(f"title tokens: {', '.join(title_overlap[:5])}")
    if text_overlap:
        score += max(0, min(len(text_overlap), 5) - 1)
    if venue_hint_hits:
        score += 2
        reasons.append(f"venue hints: {', '.join(venue_hint_hits[:3])}")

    if not any_title_matches and len(title_overlap) < 2:
        return -999, ["weak title match"]

    if score < 6:
        return -999, ["low relevance score"]

    return score, reasons


def select_candidates(topic: dict[str, str], items: list[dict]) -> list[tuple[int, list[str], dict]]:
    scored = []
    seen_titles = set()
    for item in items:
        score, reasons = score_item(topic, item)
        if score < 0:
            continue
        title = ((item.get("title") or ["Untitled"])[0]).strip()
        title_key = re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        scored.append((score, reasons, item))

    scored.sort(
        key=lambda entry: (
            -entry[0],
            -(int(extract_year(entry[2])) if extract_year(entry[2]) else 0),
            ((entry[2].get("title") or [""])[0]).lower(),
        )
    )
    return scored[:MAX_RESULTS_PER_TOPIC]


def render_report(topics: list[dict[str, str]], days: int) -> str:
    today = dt.date.today()
    since_date = today - dt.timedelta(days=days)
    lines = [
        f"# Literature Watch Report - {today.isoformat()}",
        "",
        "Workstream: Literature",
        f"Generated by: {pathlib.Path(__file__).name}",
        "",
        f"Window: last {days} days since {since_date.isoformat()}",
        "",
    ]

    if not topics:
        lines.append("No active topics matched the requested filters.")
        return "\n".join(lines) + "\n"

    for topic in topics:
        lines.append(f"## {topic['topic_id']} - {topic['topic_name']}")
        lines.append("")
        lines.append(f"- priority: {topic['priority']}")
        lines.append(f"- cadence: {topic['cadence']}")
        lines.append(f"- notes: {topic['notes']}")
        lines.append("")
        try:
            payload = fetch_json(crossref_query_url(topic, since_date))
            items = payload.get("message", {}).get("items", [])
            candidates = select_candidates(topic, items)
        except Exception as exc:  # noqa: BLE001
            lines.append(f"Search failed: {exc}")
            lines.append("")
            continue

        if not candidates:
            lines.append("No high-signal candidates found after filtering.")
            lines.append("")
            continue

        for score, reasons, item in candidates:
            title = (item.get("title") or ["Untitled"])[0]
            authors = extract_authors(item)
            year = extract_year(item)
            venue = (item.get("container-title") or [""])[0]
            url = item.get("URL", "")
            lines.append(f"- **{title}** ({year})")
            lines.append("  Source: Crossref")
            lines.append(f"  Score: {score}")
            lines.append(f"  Why surfaced: {'; '.join(reasons)}")
            lines.append(f"  Authors: {authors or 'Unknown'}")
            lines.append(f"  Venue: {venue or 'Unknown'}")
            lines.append(f"  DOI/URL: {url}")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    topics = load_topics(args.topic)
    report = render_report(topics, args.days)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORTS_DIR / f"literature_watch_{dt.date.today().isoformat()}.md"
    output_path.write_text(report, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
