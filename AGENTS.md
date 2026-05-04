# AGENTS.md

## Project Purpose

This repository supports an MSc thesis on biomechanical modeling and experimental validation of a soft variable-stiffness finger actuation system for neurorehabilitation.

## Thesis Title

Biomechanical Modeling and Experimental Validation of a Soft Variable-Stiffness Finger Actuation System for Neurorehabilitation

## Current Scope

- Focus on a simplified finger-actuator system, not a full hand glove
- Proceed simulation first, then physical mock-up validation
- Study how variable stiffness affects controllability and biomechanical interaction
- Treat soft or embedded elastomeric sensing as secondary or future work unless later evidence makes it essential
- For literature-review tasks, do not assume only soft robotics is relevant; include any technology family that directly informs pinch grasp, thumb-index opposition, finger tapping, or related task-specific motion

## Non-Goals

- Full wearable glove development
- Sensing-led thesis framing
- Clinical efficacy claims
- Full FEM by default
- Large open-ended implementation without a prior decision or scoped task

## Preferred Stack

- Python scientific stack for reusable models and analysis
- Notebooks for exploration and plots
- Markdown for thesis context, synthesis, and decisions
- Zotero outside the repo for reference management and PDFs

## Working Principles

- Start with the simplest defensible model
- Prefer interpretable code over clever abstractions
- Keep assumptions explicit and parameterized
- Separate literature synthesis from implementation work
- Add tests for reusable model components when code exists
- Keep one active task at a time in `docs/CURRENT_TASK.md`

## Required Pre-Task Context

Before starting implementation work, read:

1. `docs/THESIS_BRIEF.md`
2. `docs/CURRENT_TASK.md`
3. the latest relevant entry in `docs/DECISION_LOG.md`

## Task Completion Rules

Before closing a task:

- update assumptions if they changed
- document limitations and open questions
- update or create the relevant memo or decision entry
- run relevant checks when code exists
- keep outputs aligned with the current thesis scope

## What Good Results Look Like

- Clear connection from literature to modeling or validation choices
- Small scoped deliverables with explicit acceptance criteria
- Reproducible analysis artifacts
- Decisions that can be revisited later without losing rationale
