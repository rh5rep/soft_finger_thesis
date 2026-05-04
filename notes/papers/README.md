# Paper Notes

This folder contains one Markdown note per paper tracked in `refs/PAPER_TRACKER.csv`.

## Naming

Paper notes should use human-readable filenames, not raw Zotero keys.

Preferred pattern:

```text
notes/papers/pYYYY_firstauthor_short_title.md
```

The Zotero key still belongs inside the note metadata and tracker, but not as the main filename.

## Workflow

1. Papers enter through Zotero sync or literature-watch screening.
2. `scripts/create_paper_notes.py` ensures each paper has a note file.
3. Reading, extraction, and quote logging happen in these note files.
4. Each note should separate `only from source` material from `project interpretation`.
5. Exact quotes and page numbers should be stored here before the wording is reused in thesis-facing synthesis.
6. Cross-paper claims that recur across multiple notes should be promoted into `docs/CLAIM_REGISTRY.md`.
7. Key takeaways move into `docs/STUDY_GUIDE.md`, topic memos, and decision entries only after the note is source-checked.

## Required Minimum For Writing-Safe Use

Before a paper is treated as safe to reuse in writing:

- fill `Audit Status`
- add a source-verified summary or thesis-relevance note
- distinguish direct source claims from project interpretation
- log exact quotes with page numbers when wording matters
- record any important limitation or scope caveat

Chat memory is not enough. The paper note should be the local audit trail.

## Commands

Create or backfill notes:

```bash
python3 scripts/create_paper_notes.py
```

Build the current literature audit report:

```bash
python3 scripts/build_literature_audit.py
```

Export tracker-only candidates to a Zotero-importable BibTeX file:

```bash
python3 scripts/export_tracker_candidates_to_bib.py
```

## Recommended Depth Tiers

- `screening`: short structured note with thesis relevance, one or two claims, and clear gaps
- `shortlist`: fuller note with source-backed claims, quote bank, limitations, and thesis impact
- `high priority + attached PDF`: deep evidence sheet with figure/result takeaways and cross-paper claim promotion when justified
