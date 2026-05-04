#!/usr/bin/env python3
"""
Create per-paper Markdown notes from refs/PAPER_TRACKER.csv.

This is part of the Literature workstream. It also backfills notes_file
paths in the tracker when they are missing.
"""

from __future__ import annotations

import argparse
import csv
import pathlib
import re
import unicodedata


ROOT = pathlib.Path(__file__).resolve().parents[1]
TRACKER_PATH = ROOT / "refs" / "PAPER_TRACKER.csv"
NOTES_DIR = ROOT / "notes" / "papers"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--refresh-existing",
        action="store_true",
        help="Rewrite existing paper notes from tracker metadata.",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "_", ascii_value).strip("_")


def first_author_token(authors: str) -> str:
    first_author = (authors or "").split(";")[0].strip()
    if not first_author:
        return "unknown"
    tokens = first_author.replace(".", " ").split()
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


def infer_readable_note_path(row: dict[str, str]) -> str:
    year = row.get("year", "") or "unknown"
    author_token = first_author_token(row.get("authors", ""))
    title_token = title_keywords(row.get("title", ""))
    return f"notes/papers/p{year}_{author_token}_{title_token}.md"


def note_path_for_row(row: dict[str, str]) -> str:
    if row.get("notes_file"):
        return row["notes_file"]
    if row.get("title"):
        return infer_readable_note_path(row)
    return f"notes/papers/{slugify(row['paper_id'] or row['title'])}.md"


def render_note(row: dict[str, str]) -> str:
    title = row.get("title", "").strip() or "Untitled paper"
    url = row.get("url", "").strip()
    doi = row.get("doi", "").strip()
    pdf_status = row.get("pdf_status", "").strip()
    pdf_path = row.get("pdf_path", "").strip()
    zotero_select_uri = row.get("zotero_select_uri", "").strip()
    lines = [
        f"# {title}",
        "",
        "## Metadata",
        "",
        f"- Paper ID: `{row.get('paper_id', '')}`",
        f"- Zotero key: `{row.get('zotero_key', '')}`",
        f"- Topic: `{row.get('topic', '')}`",
        f"- Status: `{row.get('status', '')}`",
        f"- Priority: `{row.get('priority', '')}`",
        f"- Source: `{row.get('source', '')}`",
        f"- Year: `{row.get('year', '')}`",
        f"- Venue: {row.get('venue', '')}",
        f"- Authors: {row.get('authors', '')}",
        f"- DOI: {doi or '_missing_'}",
        f"- URL: {url or '_missing_'}",
        f"- PDF status: `{pdf_status or 'unknown'}`",
        f"- PDF path: {pdf_path or '_not attached_'}",
        f"- Zotero open link: {zotero_select_uri or '_missing_'}",
        "",
        "## Audit Status",
        "",
        "- Reading stage: captured",
        "- Source verification: not checked against PDF",
        "- Exact quotes logged: no",
        "- Last audited:",
        "- Used in:",
        "",
        "## Why This Paper Is In The Queue",
        "",
        row.get("why_read_now", "") or "_Fill in why this should be read now._",
        "",
        "## Citation / Bibliographic Notes",
        "",
        f"- Title: {title}",
        f"- Authors: {row.get('authors', '')}",
        f"- Venue: {row.get('venue', '')}",
        f"- Year: {row.get('year', '')}",
        f"- DOI: {doi}",
        f"- URL: {url}",
        f"- Tracker question: {row.get('question_supported', '')}",
        "",
        "## Classification",
        "",
        f"- Type: {row.get('paper_type', '')}",
        f"- Topic: {row.get('topic', '')}",
        f"- Actuation type: {row.get('actuation_type', '')}",
        f"- Model type: {row.get('model_type', '')}",
        f"- Validation type: {row.get('validation_type', '')}",
        "",
        "## Source-Verified Summary",
        "",
        "- ",
        "",
        "## One-Sentence Thesis Relevance",
        "",
        "- ",
        "",
        "## Core Definitions (Only From Source)",
        "",
        "- Term:",
        "  - Definition:",
        "  - Support:",
        "",
        "## Main Claims (Only From Source)",
        "",
        "- Claim:",
        "  - Explanation:",
        "  - Support:",
        "",
        "## Key Quotes (Only When Wording Matters)",
        "",
        "- Quote:",
        "  - Page:",
        "  - Why wording matters:",
        "",
        "## Mechanistic Insights (From Paper)",
        "",
        "- Mechanism:",
        "  - Description:",
        "  - Support:",
        "",
        "## Observations / Results (From Paper)",
        "",
        "- Finding:",
        "  - Description:",
        "  - Support:",
        "",
        "## What This Paper Suggests (Project Interpretation)",
        "",
        "- Interpretation:",
        "  - Why it matters:",
        "",
        "## Model / Mechanism / Validation Details",
        "",
        "- System type:",
        "- Actuation type:",
        "- Model type:",
        "- Validation setup:",
        "- Main metrics:",
        "",
        "## What Matters For This Thesis",
        "",
        "- ",
        "",
        "## Relevance To Finger Tapping / Thesis",
        "",
        "- Direct relevance:",
        "- Indirect relevance:",
        "",
        "## Control-System Interpretation (Project Interpretation)",
        "",
        "- Controller:",
        "- Plant:",
        "- Feedback:",
        "- Reference:",
        "- Notes:",
        "",
        "## Exact Quotes / Evidence Bank",
        "",
        "- Quote:",
        "- Page:",
        "- Section or figure:",
        "- Why it matters:",
        "- Reusable in:",
        "",
        "## Claims Safe To Reuse Later",
        "",
        "- Claim:",
        "- Support:",
        "- Confidence:",
        "",
        "## What This Paper Does Not Answer",
        "",
        "- Gap:",
        "- Gap:",
        "",
        "## Open Questions",
        "",
        "- Question:",
        "- Question:",
        "",
        "## Limitations",
        "",
        "- ",
        "",
        "## Tags",
        "",
        "- ",
        "",
        "## Decision Impact",
        "",
        "- Which memo or decision this should affect:",
        "- What it changes:",
        "",
        "## Next Action",
        "",
        row.get("next_action", "") or "- ",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    with TRACKER_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return 0
    fieldnames = list(rows[0].keys())

    created_count = 0
    refreshed_count = 0
    tracker_changed = False
    updated_rows = []
    for row in rows:
        original_notes_file = row.get("notes_file", "")
        row["notes_file"] = note_path_for_row(row)
        if row["notes_file"] != original_notes_file:
            tracker_changed = True
        note_path = ROOT / row["notes_file"]
        if not note_path.exists():
            note_path.write_text(render_note(row), encoding="utf-8")
            created_count += 1
        elif args.refresh_existing:
            note_path.write_text(render_note(row), encoding="utf-8")
            refreshed_count += 1
        updated_rows.append(row)

    if tracker_changed:
        with TRACKER_PATH.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

    print(f"created {created_count} paper notes, refreshed {refreshed_count} existing notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
