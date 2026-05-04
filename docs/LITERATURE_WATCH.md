# LITERATURE_WATCH

This file defines the recurring workflow for finding new or newly relevant papers without repeating manual searches from scratch.

It belongs to the `Literature` workstream of the thesis repo, not the full thesis workflow by itself.

## Goal

Maintain a small, updateable table of thesis topics and search terms that can drive:

- periodic paper discovery
- suggested reading queues
- topic-specific refresh reports
- additions to `refs/PAPER_TRACKER.csv`

## Source Of Truth

- `refs/SEARCH_TOPICS.csv`: the search registry
- `refs/PAPER_TRACKER.csv`: the shared reading queue

## Recommended Workflow

1. Update or add rows in `refs/SEARCH_TOPICS.csv`.
2. Run a literature-watch pass for active rows.
3. Review candidate papers returned by the search.
4. Add worthwhile papers to `refs/PAPER_TRACKER.csv` with:
   - `added_by`
   - `source`
   - `question_supported`
   - `why_read_now`
   - `status`
5. Promote strong papers from `screening` to `shortlist`, `must-read`, or `read`.

## Suggested Status Vocabulary

- `inbox`: captured but not screened
- `screening`: worth a quick abstract/title pass
- `shortlist`: likely relevant and worth reading soon
- `must-read`: directly supports an active thesis decision
- `read`: already read
- `used-in-memo`: incorporated into a topic memo
- `used-in-decision`: cited in a decision entry
- `irrelevant`: screened out

## Suggested Priority Vocabulary

- `high`: directly supports the current thesis question
- `medium`: useful soon, but not blocking
- `low`: peripheral or background

## Added By Vocabulary

- `rami`
- `codex`
- `supervisor`
- `citation_chase`
- `alert`

## Source Vocabulary

- `zotero`
- `crossref`
- `semantic_scholar`
- `manual`
- `supervisor`
- `citation_chase`

## Search Strategy

Keep each search topic broad enough to return relevant papers but narrow enough to avoid dumping an entire field. Use:

- `keywords_any` for synonyms and adjacent phrases
- `keywords_all` for mandatory anchors
- `exclude_terms` to cut obvious drift

The goal is not to capture every paper. The goal is to surface a manageable candidate set that can be screened and justified.

## Output Pattern

Each literature-watch run should produce:

- a short candidate list with title, year, source, and reason to screen
- a small set of papers added to `refs/PAPER_TRACKER.csv`
- a note on which search topics need refining

## Automation Direction

The best recurring setup is a weekly or biweekly run that:

1. reads `refs/SEARCH_TOPICS.csv`
2. searches for recent papers for active topics
3. writes a dated report under `docs/WEEKLY_MEMOS/` or a future `reports/` folder
4. proposes additions to `refs/PAPER_TRACKER.csv`

Start with manual review of candidate papers. Keep the final judgment step manual even if search and reporting become automated.

## Command Pattern

When using the repo environment, prefer:

```bash
./.venv/bin/python scripts/search_new_papers.py
```
