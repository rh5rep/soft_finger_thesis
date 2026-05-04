# Minimal Disruption Move Proposal

## Goal

Reduce confusion without doing a disruptive full-vault reorganization.

## Current Problem

Right now `docs/` mixes:

- thesis control files
- topic memos
- presentation artifacts
- operations/process files
- templates

This makes it harder to see what is:

- active thesis thinking
- old presentation support material
- process/admin support

## Recommended Moves

### 1. Create Four Subfolders Under `docs/`

- `docs/core/`
- `docs/memos/`
- `docs/presentations/`
- `docs/ops/`

### 2. Move Files As Follows

Move into `docs/core/`:

- `docs/THESIS_BRIEF.md`
- `docs/CURRENT_TASK.md`
- `docs/DECISION_LOG.md`

Move into `docs/memos/`:

- everything currently in `docs/TOPIC_MEMOS/`

Move into `docs/presentations/`:

- `docs/3-26-presentation-draft.pdf`
- `docs/3-26-presentation-draft.pptx`
- `docs/PRESENTATION_NOTES.md`
- `docs/PRESENTATION_NOTES_2026-03-26_finger_tapping_and_adjacent_technologies.md`
- `docs/PRESENTATION_NOTES_2026-03-27_supervisor_meeting.md`
- `docs/DEVICE_COMPARISON_CRIB_SHEET_2026-03-27.md`

Move into `docs/ops/`:

- `docs/LITERATURE_WATCH.md`
- `docs/ZOTERO_SYNC.md`
- `docs/templates/`

### 3. Decide What To Do With `reports/`

Recommendation:

- move `reports/literature_watch_*.md` into `docs/ops/reports/`

Reason:

- these are process outputs, not thesis-facing deliverables

### 4. Root-Level Notes

Recommendation:

- move `Meeting Prep 10-04-26.md` to archive or delete it after confirming the copy in `notes/Meetings/`
- move future meeting prep into `notes/Meetings/` only
- leave `Meeting with Sævar 26-03-26.md` for now, but later move or rewrite it into `notes/Meetings/`

## What Not To Move Right Now

Do **not** move:

- `refs/`
- `notes/papers/`
- `simulation_modeling/`
- `scripts/`

These already have fairly clear roles.

## Why This Is Minimal Disruption

- no change to the bibliography pipeline
- no change to simulation paths
- no change to tracker paths
- only `docs/` gets clearer internal separation

## Suggested Execution Order

1. create the four `docs/` subfolders
2. move presentation files first
3. move ops/process files second
4. move core files third
5. move topic memos last
6. update any internal links if needed

## My Recommendation

This reorganization is worth doing, but only after the current Parkinson reading push for this week unless the current clutter is actively slowing you down.
