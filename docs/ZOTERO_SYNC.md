# ZOTERO_SYNC

This repo treats Zotero as the source of bibliographic truth and `refs/PAPER_TRACKER.csv` as the thesis triage layer for the `Literature` workstream.

## Export Path

Export the thesis Zotero collection to:

`refs/zotero_export.json`

Recommended format:

- `BetterBibTeX JSON`
- `Export Notes`: on
- `Export Files`: off
- `Keep updated`: on

## Sync Command

Run:

```bash
./.venv/bin/python scripts/sync_zotero_to_tracker.py
./.venv/bin/python scripts/create_paper_notes.py
./.venv/bin/python scripts/export_tracker_candidates_to_bib.py
```

## What The Sync Does

- reads `refs/zotero_export.json`
- ignores notes and attachments
- updates bibliographic fields in `refs/PAPER_TRACKER.csv`
- can be followed by note generation under `notes/papers/`
- can export tracker-only candidates to `refs/zotero_import_candidates.bib`
- uses human-readable note filenames by default, while keeping Zotero keys in tracker metadata
- preserves manual thesis fields such as:
  - `why_read_now`
  - `why_relevant`
  - `screening_notes`
  - `key_takeaway`
  - `decision_impact`

## Matching Rules

The sync matches existing tracker rows in this order:

1. `zotero_key`
2. DOI-backed `paper_id`
3. normalized title

## Tag Conventions

These Zotero tags can seed tracker defaults:

- `soft-actuation` -> `T001`
- `variable-stiffness` -> `T002`
- `finger-biomechanics` -> `T003`
- `validation` -> `T004`
- `rehab-positioning` -> `T005`
- `read` -> tracker status `read`
- `to-read` -> tracker status `shortlist`
- `core` -> tracker priority `high`

## Important

The tracker is still the place for judgment. Zotero tags and metadata should help seed the queue, not replace memo writing, decision logging, or simulation-modeling choices.
