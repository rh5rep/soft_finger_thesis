#!/usr/bin/env python3
"""
Export tracker rows without zotero_key into a BibTeX file that can be imported into Zotero.

This script belongs to the Literature workstream.
"""

from __future__ import annotations

import csv
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
TRACKER_PATH = ROOT / "refs" / "PAPER_TRACKER.csv"
OUTPUT_PATH = ROOT / "refs" / "zotero_import_candidates.bib"


def bibtex_escape(value: str) -> str:
    value = value.replace("\\", "\\\\")
    value = value.replace("{", "\\{").replace("}", "\\}")
    return value


def bibtex_key(row: dict[str, str]) -> str:
    if row.get("paper_id"):
        return re.sub(r"[^A-Za-z0-9]+", "_", row["paper_id"]).strip("_")
    base = f"{row.get('year', '')}_{row.get('title', '')}"
    return re.sub(r"[^A-Za-z0-9]+", "_", base).strip("_")


def render_entry(row: dict[str, str]) -> str:
    fields = {
        "title": row.get("title", ""),
        "author": row.get("authors", ""),
        "year": row.get("year", ""),
        "journal": row.get("venue", ""),
        "doi": row.get("doi", ""),
        "url": row.get("url", ""),
        "note": row.get("why_read_now", ""),
        "keywords": ", ".join(filter(None, [row.get("topic", ""), row.get("status", ""), row.get("priority", "")])),
    }
    lines = ["@article{" + bibtex_key(row) + ","]  # Better BibTeX / Zotero can import this and clean up later.
    for field, value in fields.items():
        if value:
            lines.append(f"  {field} = {{{bibtex_escape(value)}}},")
    lines.append("}")
    return "\n".join(lines)


def main() -> int:
    with TRACKER_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    candidates = [row for row in rows if not row.get("zotero_key")]
    entries = [render_entry(row) for row in candidates if row.get("title")]
    OUTPUT_PATH.write_text("\n\n".join(entries) + ("\n" if entries else ""), encoding="utf-8")
    print(f"exported {len(entries)} candidates to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
