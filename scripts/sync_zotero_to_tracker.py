#!/usr/bin/env python3
"""
Merge Better BibTeX JSON export data into refs/PAPER_TRACKER.csv.

Design goals:
- Read Zotero-exported metadata from refs/zotero_export.json.
- Ignore notes and attachments.
- Update bibliographic fields in PAPER_TRACKER.csv without overwriting
  manual thesis-judgment fields when they already contain values.
- Match existing rows by zotero_key first, then DOI, then normalized title.

This script belongs to the Literature workstream.
"""

from __future__ import annotations

import csv
import json
import pathlib
import re
import unicodedata
from typing import Iterable


ROOT = pathlib.Path(__file__).resolve().parents[1]
ZOTERO_EXPORT_PATH = ROOT / "refs" / "zotero_export.json"
TRACKER_PATH = ROOT / "refs" / "PAPER_TRACKER.csv"

TRACKER_FIELDS = [
    "paper_id",
    "title",
    "authors",
    "year",
    "venue",
    "doi",
    "url",
    "pdf_path",
    "pdf_status",
    "zotero_select_uri",
    "topic",
    "status",
    "priority",
    "added_by",
    "source",
    "paper_type",
    "actuation_type",
    "model_type",
    "validation_type",
    "question_supported",
    "why_opened",
    "why_read_now",
    "why_relevant",
    "screening_notes",
    "key_takeaway",
    "limitations",
    "decision_impact",
    "zotero_key",
    "notes_file",
    "next_action",
]

TOPIC_TAG_MAP = {
    "soft-actuation": "T001",
    "variable-stiffness": "T002",
    "finger-biomechanics": "T003",
    "validation": "T004",
    "rehab-positioning": "T005",
}


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def normalize_ascii(value: str) -> str:
    return unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode("ascii")


def slugify(value: str) -> str:
    ascii_value = normalize_ascii(value).lower()
    return re.sub(r"[^a-z0-9]+", "_", ascii_value).strip("_")


def extract_year(date_value: str) -> str:
    match = re.search(r"(19|20)\d{2}", date_value or "")
    return match.group(0) if match else ""


def format_authors(creators: Iterable[dict]) -> str:
    names = []
    for creator in creators:
        if creator.get("creatorType") != "author":
            continue
        first = (creator.get("firstName") or "").strip()
        last = (creator.get("lastName") or "").strip()
        full_name = " ".join(part for part in (first, last) if part)
        if full_name:
            names.append(full_name)
    return "; ".join(names)


def first_author_token(authors: str) -> str:
    first_author = (authors or "").split(";")[0].strip()
    if not first_author:
        return "unknown"
    tokens = normalize_ascii(first_author).replace(".", " ").split()
    if not tokens:
        return "unknown"
    return slugify(tokens[-1]) or "unknown"


def title_keywords(title: str, max_tokens: int = 6) -> str:
    stopwords = {
        "a",
        "an",
        "the",
        "of",
        "on",
        "in",
        "for",
        "with",
        "to",
        "and",
        "using",
        "use",
        "used",
        "via",
        "from",
    }
    generic_words = {
        "study",
        "paper",
        "development",
        "design",
        "validation",
        "improving",
        "exploring",
        "effects",
        "effect",
        "impact",
        "analysis",
        "analyzing",
        "approach",
        "approaches",
        "current",
        "future",
        "present",
        "pilot",
    }
    tokens = [token for token in slugify(title).split("_") if token]
    filtered = [token for token in tokens if token not in stopwords and token not in generic_words]
    chosen = filtered[:max_tokens] or tokens[:max_tokens] or ["untitled", "paper"]
    return "_".join(chosen)


def collect_tags(item: dict) -> set[str]:
    return {tag.get("tag", "").strip() for tag in item.get("tags", []) if tag.get("tag")}


def infer_topic(tags: set[str]) -> str:
    for tag, topic_id in TOPIC_TAG_MAP.items():
        if tag in tags:
            return topic_id
    return ""


def infer_status(tags: set[str]) -> str:
    if "read" in tags:
        return "read"
    if "to-read" in tags:
        return "shortlist"
    return "inbox"


def infer_priority(tags: set[str]) -> str:
    if "core" in tags:
        return "high"
    return "medium"


def infer_readable_notes_file(year: str, authors: str, title: str, item_key: str) -> str:
    year_token = year if year else "unknown"
    author_token = first_author_token(authors)
    title_token = title_keywords(title)
    fallback = slugify(item_key) or "paper"
    filename = f"p{year_token}_{author_token}_{title_token or fallback}.md"
    return f"notes/papers/{filename}"


def extract_pdf_fields(item: dict) -> tuple[str, str, str]:
    for attachment in item.get("attachments", []):
        path = (attachment.get("path") or "").strip()
        select_uri = (attachment.get("select") or "").strip()
        if path:
            return path, "attached", select_uri
    return "", "missing", ""


def flatten_items(export_data: dict) -> list[dict]:
    items = []
    for item in export_data.get("items", []):
        if item.get("itemType") in {"note", "attachment"}:
            continue
        items.append(item)
    return items


def load_tracker_rows() -> list[dict[str, str]]:
    with TRACKER_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_indexes(rows: list[dict[str, str]]) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    by_key = {}
    by_doi = {}
    by_title = {}
    for row in rows:
        if row.get("zotero_key"):
            by_key[row["zotero_key"]] = row
        if row.get("paper_id", "").startswith("DOI:"):
            by_doi[row["paper_id"][4:].lower()] = row
        title_key = normalize_title(row.get("title", ""))
        if title_key:
            by_title[title_key] = row
    return by_key, by_doi, by_title


def tracker_row_from_item(item: dict) -> dict[str, str]:
    tags = collect_tags(item)
    doi = (item.get("DOI") or "").strip()
    title = (item.get("title") or "").strip()
    zotero_key = (item.get("itemKey") or item.get("key") or "").strip()
    pdf_path, pdf_status, zotero_select_uri = extract_pdf_fields(item)
    authors = format_authors(item.get("creators", []))
    year = extract_year(item.get("date", ""))
    return {
        "paper_id": f"DOI:{doi}" if doi else f"ZOTERO:{zotero_key}",
        "title": title,
        "authors": authors,
        "year": year,
        "venue": (item.get("publicationTitle") or item.get("bookTitle") or "").strip(),
        "doi": doi,
        "url": (item.get("url") or "").strip(),
        "pdf_path": pdf_path,
        "pdf_status": pdf_status,
        "zotero_select_uri": zotero_select_uri,
        "topic": infer_topic(tags),
        "status": infer_status(tags),
        "priority": infer_priority(tags),
        "added_by": "rami",
        "source": "zotero",
        "paper_type": item.get("itemType", ""),
        "actuation_type": "",
        "model_type": "",
        "validation_type": "",
        "question_supported": "",
        "why_opened": "",
        "why_read_now": "",
        "why_relevant": "",
        "screening_notes": "",
        "key_takeaway": "",
        "limitations": "",
        "decision_impact": "",
        "zotero_key": zotero_key,
        "notes_file": infer_readable_notes_file(year, authors, title, zotero_key) if zotero_key else "",
        "next_action": "screen abstract and decide topic memo placement",
    }


def merge_row(existing: dict[str, str], incoming: dict[str, str]) -> dict[str, str]:
    merged = dict(existing)

    metadata_fields = [
        "paper_id",
        "title",
        "authors",
        "year",
        "venue",
        "doi",
        "url",
        "pdf_path",
        "pdf_status",
        "zotero_select_uri",
        "paper_type",
        "zotero_key",
    ]
    defaultable_fields = [
        "topic",
        "status",
        "priority",
        "added_by",
        "source",
        "notes_file",
        "next_action",
    ]

    for field in metadata_fields:
        if incoming.get(field):
            merged[field] = incoming[field]

    for field in defaultable_fields:
        if not merged.get(field) and incoming.get(field):
            merged[field] = incoming[field]

    return merged


def main() -> int:
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    export_data = json.loads(ZOTERO_EXPORT_PATH.read_text(encoding="utf-8"))
    tracker_rows = load_tracker_rows()
    by_key, by_doi, by_title = build_indexes(tracker_rows)
    new_count = 0
    updated_count = 0

    for item in flatten_items(export_data):
        incoming = tracker_row_from_item(item)
        row = None
        zotero_key = incoming.get("zotero_key", "")
        doi = incoming.get("paper_id", "")[4:].lower() if incoming.get("paper_id", "").startswith("DOI:") else ""
        title_key = normalize_title(incoming.get("title", ""))

        if zotero_key and zotero_key in by_key:
            row = by_key[zotero_key]
        elif doi and doi in by_doi:
            row = by_doi[doi]
        elif title_key and title_key in by_title:
            row = by_title[title_key]

        if row is None:
            tracker_rows.append(incoming)
            new_count += 1
            if zotero_key:
                by_key[zotero_key] = incoming
            if doi:
                by_doi[doi] = incoming
            if title_key:
                by_title[title_key] = incoming
            continue

        merged = merge_row(row, incoming)
        row.update(merged)
        updated_count += 1

    tracker_rows.sort(key=lambda row: (row.get("topic", ""), row.get("priority", ""), row.get("year", ""), row.get("title", "")))

    with TRACKER_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRACKER_FIELDS)
        writer.writeheader()
        writer.writerows(tracker_rows)

    print(f"synced {new_count} new rows, updated {updated_count} existing rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
