#!/usr/bin/env python3
"""
Build a markdown audit report from refs/PAPER_TRACKER.csv and notes/papers/.

The audit report is operational rather than rhetorical: it shows what has been
captured, what has actual extraction work in the note, and where quote-level
verification is still missing.
"""

from __future__ import annotations

import csv
import datetime as dt
import pathlib
import re
from collections import Counter, defaultdict


ROOT = pathlib.Path(__file__).resolve().parents[1]
TRACKER_PATH = ROOT / "refs" / "PAPER_TRACKER.csv"
TOPICS_PATH = ROOT / "refs" / "SEARCH_TOPICS.csv"
OUTPUT_PATH = ROOT / "docs" / "LITERATURE_AUDIT.md"

SUMMARY_HEADINGS = ["## Source-Verified Summary", "## Abstract / Summary"]
THESIS_HEADINGS = ["## What Matters For This Thesis"]
QUOTE_HEADINGS = ["## Exact Quotes / Evidence Bank", "## Quotes / Data To Reuse Later"]


def load_csv(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_topics() -> dict[str, str]:
    rows = load_csv(TOPICS_PATH)
    topics = {row["topic_id"]: row["topic_name"] for row in rows}
    topics[""] = "Unassigned"
    return topics


def extract_section(text: str, heading: str) -> str:
    pattern = rf"^{re.escape(heading)}\s*$\n(.*?)(?=^##\s|\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def has_meaningful_content(section_text: str) -> bool:
    if not section_text:
        return False
    placeholders = {
        "-",
        "- ",
        "_Fill in why this should be read now._",
        "_No source-verified synthesis entered yet._",
        "_Empty for now._",
    }
    lines = [line.strip() for line in section_text.splitlines()]
    meaningful = []
    for line in lines:
        if not line:
            continue
        if line in placeholders:
            continue
        if re.fullmatch(r"-\s*", line):
            continue
        meaningful.append(line)
    return bool(meaningful)


def note_signals(note_path: pathlib.Path) -> dict[str, bool]:
    if not note_path.exists():
        return {
            "exists": False,
            "has_summary": False,
            "has_thesis": False,
            "has_quotes": False,
            "reading_stage": "",
        }

    text = note_path.read_text(encoding="utf-8")
    summary = any(has_meaningful_content(extract_section(text, heading)) for heading in SUMMARY_HEADINGS)
    thesis = any(has_meaningful_content(extract_section(text, heading)) for heading in THESIS_HEADINGS)
    quotes = any(has_meaningful_content(extract_section(text, heading)) for heading in QUOTE_HEADINGS)
    match = re.search(r"^- Reading stage:\s*(.+)$", text, flags=re.MULTILINE)
    return {
        "exists": True,
        "has_summary": summary,
        "has_thesis": thesis,
        "has_quotes": quotes,
        "reading_stage": match.group(1).strip().lower() if match else "",
    }


def derive_audit_state(row: dict[str, str], signals: dict[str, bool]) -> str:
    if not signals["exists"]:
        return "missing note"
    if "quote-verified" in signals["reading_stage"]:
        return "quote-verified"
    if signals["has_quotes"]:
        return "evidence bank present"
    if signals["has_summary"] or signals["has_thesis"]:
        return "extracted"
    if row.get("status", "") == "read":
        return "tracker read; note not extracted"
    return "captured only"


def topic_sort_key(topic_id: str) -> tuple[int, str]:
    if topic_id == "":
        return (999, topic_id)
    digits = re.sub(r"\D+", "", topic_id)
    return (int(digits or "999"), topic_id)


def render_table(rows: list[dict[str, str]], topics: dict[str, str]) -> list[str]:
    lines = [
        "| Paper | Year | Topic | Tracker status | PDF | Audit state | Note |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        title = row.get("title", "").replace("|", "\\|")
        year = row.get("year", "")
        topic_id = row.get("topic", "")
        topic_label = topics.get(topic_id, topic_id or "Unassigned")
        tracker_status = row.get("status", "")
        pdf_status = "attached" if row.get("pdf_status", "") == "attached" else row.get("pdf_status", "") or "unknown"
        note_path = row.get("notes_file", "")
        note_label = pathlib.Path(note_path).name if note_path else "missing"
        note_ref = f"[{note_label}]({note_path})" if note_path else "missing"
        lines.append(
            f"| {title} | {year} | {topic_id or '-'}: {topic_label} | {tracker_status} | {pdf_status} | {row['audit_state']} | {note_ref} |"
        )
    return lines


def build_report() -> str:
    tracker_rows = load_csv(TRACKER_PATH)
    topics = load_topics()
    today = dt.date.today().isoformat()

    status_counts = Counter(row.get("status", "") for row in tracker_rows)
    pdf_counts = Counter(row.get("pdf_status", "") for row in tracker_rows)
    audit_counts = Counter()
    topic_groups: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in tracker_rows:
        note_path = ROOT / row.get("notes_file", "")
        signals = note_signals(note_path)
        row["audit_state"] = derive_audit_state(row, signals)
        audit_counts[row["audit_state"]] += 1
        topic_groups[row.get("topic", "")].append(row)

    lines = [
        "# Literature Audit",
        "",
        f"_Generated on `{today}` from `refs/PAPER_TRACKER.csv` and `notes/papers/`._",
        "",
        "This file is an operational audit ledger. It does not certify that a paper has been used safely in writing unless the underlying paper note contains source-verified summary material or exact quotes with page references.",
        "",
        "## Snapshot",
        "",
        f"- Total tracker rows: `{len(tracker_rows)}`",
        f"- Paper notes linked in tracker: `{sum(1 for row in tracker_rows if row.get('notes_file'))}`",
        f"- PDFs attached in tracker: `{pdf_counts.get('attached', 0)}`",
        f"- Tracker status counts: `{dict(status_counts)}`",
        f"- Audit state counts: `{dict(audit_counts)}`",
        "",
        "## Audit State Legend",
        "",
        "- `quote-verified`: the paper note explicitly says the note has been checked against the PDF and exact quotes were logged.",
        "- `captured only`: tracker entry and note exist, but no meaningful extraction detected yet.",
        "- `extracted`: a paper note contains summary or thesis-relevance content beyond the placeholder scaffold.",
        "- `evidence bank present`: a paper note contains non-placeholder quote or evidence bullets, but may still need exact page-level verification.",
        "- `tracker read; note not extracted`: the tracker says `read`, but the paper note still looks like a scaffold.",
        "- `missing note`: the tracker points to a note path that does not exist.",
        "",
        "## Topic Inventory",
        "",
    ]

    for topic_id in sorted(topic_groups, key=topic_sort_key):
        topic_name = topics.get(topic_id, topic_id or "Unassigned")
        rows = sorted(topic_groups[topic_id], key=lambda row: (row.get("year", ""), row.get("title", "")))
        lines.extend(
            [
                f"### {topic_id or 'UNASSIGNED'} - {topic_name}",
                "",
                f"- Papers in topic: `{len(rows)}`",
                "",
            ]
        )
        lines.extend(render_table(rows, topics))
        lines.append("")

    lines.extend(
        [
            "## Immediate Audit Priorities",
            "",
            "- Fill exact quotes and page numbers first for the highest-priority papers likely to appear in thesis writing.",
            "- Promote paper notes from `captured only` to `extracted` before adding any synthesis to `docs/STUDY_GUIDE.md`.",
            "- Treat memo-only claims as pending until they are rechecked against the PDF and logged in the paper note.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    OUTPUT_PATH.write_text(build_report(), encoding="utf-8")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
