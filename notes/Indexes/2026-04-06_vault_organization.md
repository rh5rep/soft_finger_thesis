# Vault Organization Note 2026-04-06

## Why Change Anything

The vault already has a good split between:

- `docs/` for thesis-facing outputs
- `notes/papers/` for paper notes
- `refs/` for bibliography tracking
- `simulation_modeling/` for technical work

What is missing is a clean home for:

- background learning
- meeting prep
- methods foundations

## Recommended Structure

- `docs/`
  - thesis-facing memos, decisions, current task, presentation notes
- `notes/Meetings/`
  - meeting prep, meeting debriefs, action lists
- `notes/papers/`
  - one note per paper
- `notes/Background/Parkinsons/`
  - disease background and non-paper learning notes
- `notes/Methods/`
  - math, software, control, validation, modeling foundations
- `notes/Indexes/`
  - maps of how the vault is organized
- `refs/`
  - tracker, search topics, Zotero export/import
- `simulation_modeling/`
  - notebooks and reusable model code

## Minimal Rules Going Forward

- Put new meeting prep notes in `notes/Meetings/`.
- Put disease learning notes in `notes/Background/Parkinsons/`.
- Put methods learning notes in `notes/Methods/`.
- Keep the repo root for project-level files only.
- Avoid creating stray scratch notes at the root unless they are temporary and will be cleaned the same day.

## Suggested Naming

- meetings: `YYYY-MM-DD_short_topic.md`
- background notes: `NN_topic.md`
- methods notes: `NN_topic.md`
- paper notes: `pYYYY_firstauthor_short_title.md`

## Low-Disruption Next Cleanup

Do not do a large reorg yet.

Good next cleanup items:

- move future meeting notes into `notes/Meetings/`
- gradually move root-level personal scratch notes into a clearer home or archive them
- keep `docs/` reserved for things you may cite, present, or use for thesis decisions

## Immediate Outcome

The vault now has dedicated places for:

- Parkinson background
- methods foundations
- organized meeting prep
