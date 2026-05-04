# Thesis OS

This repository is the operating system for the thesis:

**Biomechanical Modeling and Experimental Validation of a Soft Variable-Stiffness Finger Actuation System for Neurorehabilitation**

The workflow is always:

`Question -> Search -> Distill -> Decide -> Implement -> Validate -> Log`

## Workstreams

The repo has two explicit workstreams.

### 1. Literature

This workstream is for:

- finding new literature
- syncing Zotero metadata into the thesis tracker
- screening and analyzing papers
- promoting useful papers into topic memos, decisions, and scoped tasks
- maintaining recurring or automatable literature-watch workflows

Primary files and folders:

- `docs/LITERATURE_WATCH.md`
- `docs/ZOTERO_SYNC.md`
- `refs/PAPER_TRACKER.csv`
- `refs/SEARCH_TOPICS.csv`
- `refs/zotero_export.json`
- `refs/zotero_import_candidates.bib`
- `docs/TOPIC_MEMOS/`
- `scripts/`

### 2. Simulation Modeling

This workstream is for:

- reduced-order biomechanical finger modeling
- actuator-finger interaction assumptions and equations
- notebooks, plots, and parameter sweeps
- reusable model components that may later move from notebooks into tested Python code

Primary files and folders:

- `simulation_modeling/`
- `simulation_modeling/notebooks/01_mcp_1dof_static_hello_world.ipynb`
- `docs/THESIS_BRIEF.md`
- `docs/DECISION_LOG.md`

## Task Rule

The repo may contain multiple workstreams, but `docs/CURRENT_TASK.md` should still track only one primary task at a time.

## Core Files

- `AGENTS.md`: persistent context and working rules for Codex and other agents
- `docs/THESIS_BRIEF.md`: strategic source of truth for scope, research questions, and milestones
- `docs/THESIS_PROGRESS.md`: running narrative of thesis progress across literature, modeling, design, and validation
- `docs/CURRENT_TASK.md`: single primary active task with concrete output expectations
- `docs/DECISION_LOG.md`: append-only log of committed thesis decisions
- `docs/LITERATURE_WATCH.md`: recurring search workflow for new and newly relevant papers
- `docs/TOPIC_MEMOS/`: synthesis notes for each topic area
- `docs/WEEKLY_MEMOS/`: weekly checkpoint notes
- `docs/templates/`: reusable note, decision, and task templates
- `notes/papers/`: per-paper reading notes for Obsidian and manual synthesis
- `refs/PAPER_TRACKER.csv`: literature triage interface linked to Zotero
- `refs/SEARCH_TOPICS.csv`: editable keyword registry for recurring literature searches
- `refs/zotero_export.json`: Better BibTeX JSON export of the thesis Zotero collection
- `refs/zotero_import_candidates.bib`: Zotero-importable references proposed by the tracker/automation
- `simulation_modeling/`: notebooks and code for the simulation-first modeling track

## Weekly Cadence

1. Add and triage papers in `refs/PAPER_TRACKER.csv`.
2. Refresh or refine search topics in `refs/SEARCH_TOPICS.csv`.
3. Sync Zotero metadata into `refs/PAPER_TRACKER.csv`.
4. Generate or update per-paper notes in `notes/papers/`.
5. Convert reading into topic memos in `docs/TOPIC_MEMOS/`.
6. Record modeling or literature commitments in `docs/DECISION_LOG.md`.
7. Advance the current simulation notebook or reusable model component if simulation is the highest-leverage next step.
8. Update `docs/CURRENT_TASK.md` with the next highest-leverage primary question.
9. Write one weekly memo in `docs/WEEKLY_MEMOS/`.

## Runbook

### What Should Be In Place

- Obsidian vault pointed at the repository root
- a Zotero thesis collection exported to `refs/zotero_export.json`
- Better BibTeX export settings:
  - `BetterBibTeX JSON`
  - `Export Notes`: on
  - `Export Files`: off
  - `Keep updated`: on
- `CROSSREF_MAILTO` set in the shell when running literature-watch searches

### Core Commands

Refresh recent-paper candidates:

```bash
./.venv/bin/python scripts/search_new_papers.py
```

Sync Zotero metadata into the tracker:

```bash
./.venv/bin/python scripts/sync_zotero_to_tracker.py
```

Create or backfill per-paper notes:

```bash
./.venv/bin/python scripts/create_paper_notes.py
```

Export tracker-only candidates into a Zotero-importable file:

```bash
./.venv/bin/python scripts/export_tracker_candidates_to_bib.py
```

Open the current simulation notebook:

```bash
./.venv/bin/jupyter lab simulation_modeling/notebooks/01_mcp_1dof_static_hello_world.ipynb
```

Launch the reduced-order GUI explorer:

```bash
./.venv/bin/python -m simulation_modeling.gui_app
```

Or launch the Streamlit page directly:

```bash
./.venv/bin/python -m streamlit run simulation_modeling/streamlit_app.py
```

### Recommended Operating Sequence

1. Add papers to Zotero or import `refs/zotero_import_candidates.bib`.
2. Re-export or let Zotero refresh `refs/zotero_export.json`.
3. Run `./.venv/bin/python scripts/sync_zotero_to_tracker.py`.
4. Run `./.venv/bin/python scripts/create_paper_notes.py`.
5. Read and fill the relevant note files in `notes/papers/`.
6. Promote the useful takeaways into topic memos and decisions.

## Operating Rule

Literature is not considered processed until it ends in at least one of:

- a topic memo
- a decision entry
- a scoped task

If a paper does not change understanding, a decision, or a task, it is still unprocessed.
