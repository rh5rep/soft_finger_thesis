# Thesis Audit 2026-05-04

## Purpose

This note audits the current thesis state across:

- code and model maturity
- literature and writing readiness
- prototype readiness
- highest-leverage next steps

It is a working project audit, not writing-safe thesis prose.

## Executive Conclusion

The thesis is **not yet at a true prototype-commit phase**.

It is at a **late design-screening / pre-prototyping phase**:

- the reduced-order routing and mechanics pipeline is now real
- one first parameter sweep has been completed and saved
- the current sweep is still too narrow to justify freezing hardware
- the strongest remaining uncertainty is passive stiffness and its effect on candidate ranking

The correct near-term posture is:

`finish the screening evidence -> choose 3-5 prototype candidates -> then prototype`

not:

`freeze one geometry now and start building as if the design is already validated`

## What Is Actually Implemented

### Modeling

The repo now contains a real V0.1 screening stack, not just exploratory plotting:

- `simulation_modeling/v01_model.py`
  - planar 3-link MCP/PIP/DIP finger kinematics
  - routing elements and ordered tendon paths
  - branch-aware tendon length and pull calculations
  - moment-arm calculation from `-dL/dq`
  - least-squares scalar tension fit for one input
  - torque-fit residual as underactuation mismatch
- `simulation_modeling/candidate_sweep_utils.py`
  - candidate generation
  - sweep evaluation
  - scoring and rejection logic
  - CSV export
- saved outputs in `simulation_modeling/results/`
  - raw sweep table
  - summary table
  - analysis HTML files for best candidates

### Tests

Behavioral tests pass when the repo is run with `PYTHONPATH=.`:

- `16 passed in 1.25s`

Important caveat:

- plain `uv run pytest -q` fails at collection because `simulation_modeling` is not discoverable as an installed package in the default test environment
- this is a repo/tooling gap, not currently a model-logic failure

### Notebooks

The active work has partly moved from notebooks into reusable code, which is good.

But the notebooks are still uneven as research artifacts:

- `04_joint_trajectories.ipynb` is still rough and lightly narrated
- `05_candidate_sweep.ipynb` is mostly code cells and assumes prior context

That means the code is ahead of the notebook storytelling.

## What The Current Sweep Actually Proves

Current saved summary:

- `162` scored cases in `candidate_sweep_summary.csv`
- all from one run label: `two_guide_first_pass`
- one routing family only: single-branch two-guide candidates
- nine model cases from three size assumptions x three stiffness assumptions

Current best saved score in the summary file:

- `large_nominal`
- candidate `twoG_b-p_m_l-0.25_0.65_o--5.00_-5.00_al-0.80_ao--4.00_ex--8.00_ey--4.00`
- peak tension about `1.77 N`
- peak pull about `21.39 mm`
- RMS relative torque mismatch about `0.432`

What this does prove:

- the screening framework can rank candidates
- routing placement materially changes pull, tension, and mismatch
- the model is already useful for narrowing a search region

What this does not yet prove:

- that the current best candidate is robust to broader parameter choices
- that two-guide single-branch routing is better than other routing families
- that the chosen passive stiffness assumptions are defensible enough to lock hardware
- that a final prototype geometry is ready to fabricate

## Why This Is Not Yet Prototype-Commit Ready

### 1. The sweep is still narrow

The current saved run covers one family only:

- single-branch
- two-guide
- one coordinated flexion sweep

That is enough for first design-space reduction, but not enough for final concept lock.

### 2. Passive stiffness is still the dominant uncertainty

The repo itself already recognizes this repeatedly:

- supervisor packet
- study guide project context
- progress notes

If passive stiffness moves, then all of these can move with it:

- required torque
- fitted tension
- mismatch
- ranking
- actuator plausibility

Until stiffness is either:

- better justified from literature, or
- calibrated with a simple experiment, or
- explicitly treated as a formal uncertainty axis

you do not yet have a strong basis for locking the first physical design.

### 3. The branch architecture is not yet tested in the model

The intended hardware story increasingly points toward:

- one input
- potentially multiple physical branches
- left/right balance concerns

But the current saved candidate family is still single-branch.

That means an important hardware-relevant question is still unresolved in the actual screening pipeline.

### 4. The prototype criteria are not yet fixed

You still need explicit thresholds for:

- acceptable tension
- acceptable pull
- acceptable mismatch
- acceptable clearance / wearability proxy
- acceptable complexity for a thesis-scale mock-up

Without that, the model can rank candidates but not yet certify one as “good enough to fabricate.”

## Best Current Thesis Conclusions

These are the conclusions the repo can already support safely at the project level.

### 1. The thesis has successfully moved beyond vague concept exploration

You are no longer at “soft robotic glove idea” level.

You now have:

- a defined reduced-order abstraction
- a mechanics bridge from geometry to torque and tension
- a first candidate-screening pipeline
- saved sweep outputs

That is real progress.

### 2. The current thesis identity is becoming clearer

The strongest current identity is:

`simulation-first, reduced-order design-screening for a simplified index-finger actuator system`

not:

- full glove development
- full Parkinson clinical device program
- sensing-led thesis
- immediate actuator-technology bakeoff

### 3. Routing should be chosen before actuator complexity

The repo consistently supports this conclusion:

- route first
- estimate pull and tension
- then decide whether TSA, pulley drive, series compliance, or another variable-stiffness branch is justified

That is one of the strongest thesis-level engineering decisions already made.

### 4. Parkinson finger tapping is currently strongest as a task-framing and measurement layer

The direct assistive hardware precedent is still weak.

The Parkinson literature is currently most useful for:

- movement framing
- symptom vocabulary
- output/metric selection

not as the main mechanical design precedent.

### 5. The first prototype should be adjustable, not final-form

The repo evidence supports a first prototype more like:

- distal thimble or fingertip cap
- removable rings / routing supports
- routing-adjustable tendon path
- optional passive thumb or contact feature

rather than a polished final wearable.

## Code / Repo Audit

### Strengths

- model layers are getting separated well
- useful sweep utilities exist outside notebooks
- test coverage exists for reduced models, passive torque helpers, and GUI/Streamlit figure creation
- results are exported in inspectable CSV form

### Weaknesses

- no git commits exist yet; the repo has zero commit history
- default test invocation is brittle because package discovery is not configured cleanly
- `simulation_modeling/model_config/candidate_specs.py` is effectively empty
- notebook narration lags behind the code
- `docs/THESIS_PROGRESS.md` is stale relative to the May 1 supervisor packet and April 30 sweep work
- literature tracker discipline is lagging: most papers are still marked `inbox`

### Consequence

The technical work is ahead of the project hygiene.

That is fixable, but it matters because thesis writing and supervisor communication depend on traceability.

## Literature And Writing Readiness

### What Is Ready

You already have enough material to start writing these parts:

1. problem framing and scope
2. thesis positioning
3. why a simplified finger system is justified
4. why simulation-first is the right method
5. why finger tapping is a useful task lens
6. why direct hardware precedents come from near-adjacent MCP/index-finger exoskeletons
7. modeling assumptions and current reduced-order abstraction

### What Is Not Ready For Final Writing

These still need more evidence or stabilization first:

1. final prototype architecture
2. strong claims about variable stiffness implementation choice
3. finalized passive stiffness law
4. final routing-family decision
5. final validation protocol details

### Best Writing Strategy Now

Start writing the parts that are already structurally true and unlikely to change:

- Introduction
- Problem statement
- Scope and non-goals
- Research questions
- Literature review backbone
- Methods chapter skeleton
- Reduced-order modeling rationale
- Current validation philosophy

Do not wait for the final prototype to start those.

## Recommended Thesis Writing Outline To Start Now

### Chapter 1: Introduction

Write now:

- rehabilitation / neuro-motor motivation
- why repetitive finger motion matters
- why simplified bench-top study is valuable
- thesis objective
- research questions
- scope and exclusions

### Chapter 2: Background And Literature Review

Write now:

- bradykinesia and finger tapping as task framing
- assessment versus assistance distinction
- direct and near-adjacent device precedents
- variable stiffness mechanism landscape
- reduced-order biomechanical modeling rationale

Hold for later refinement:

- final hardware comparison table tied to your selected prototype branch

### Chapter 3: Methods

Write the stable skeleton now:

- reduced-order modeling philosophy
- finger kinematics abstraction
- tendon routing abstraction
- passive torque assumptions
- one-input underactuation framing
- sweep variables and candidate ranking logic

Leave placeholders where needed:

- final passive stiffness source or calibration method
- final chosen prototype family
- final benchtop setup details

### Chapter 4: Simulation Results

Start structuring now, even if not final:

- sanity checks
- candidate family comparison
- first sweep summary
- sensitivity to geometry and stiffness
- interpretation of mismatch and pull/tension tradeoffs

### Chapter 5: Prototype And Validation

Do not fully write yet.

Start only the scaffold:

- intended validation question
- bench-top setup concept
- measurements to collect
- expected model-to-experiment comparisons

## Highest-Leverage Next Questions

These are the questions that matter most before prototyping.

1. Which prototype decision is the next real one: routing family, branch architecture, passive stiffness assumption, or actuator type?
2. What makes a candidate “good enough to fabricate” in explicit numerical terms?
3. Should passive stiffness be calibrated now, literature-bounded, or treated as a formal uncertainty sweep?
4. Does a two-branch symmetric routing family materially outperform the best current single-branch family?
5. Which outputs will be compared in the first benchtop validation: posture, pull, tension, fingertip path, repeatability, or contact force?
6. Is the first physical prototype meant to study motion assistance, routing mechanics, or variable-stiffness behavior specifically?
7. What is the minimum prototype that still answers the thesis question?

## Recommended Next 10 Days

### Modeling

1. Add at least one more routing family beyond the current single-branch two-guide case.
2. Add a two-branch symmetric candidate family and report branch imbalance explicitly.
3. Decide how passive stiffness will be handled:
   - literature-bounded
   - benchtop-calibrated
   - formal uncertainty axis
4. Define prototype-go / no-go thresholds for tension, pull, mismatch, and simplicity.
5. Produce a top `3-5` candidate shortlist with one-page comparisons.

### Writing

1. Draft the introduction.
2. Draft the scope, non-goals, and research questions section.
3. Draft the reduced-order methods section skeleton.
4. Turn the current literature positioning into a review outline with citation placeholders tied to existing notes.

### Repo Hygiene

1. Make the test command work without manual `PYTHONPATH` intervention.
2. Update `docs/THESIS_PROGRESS.md` to reflect the April 30 / May 1 state.
3. Reclassify tracker items so the literature status field reflects reality better.
4. Create the first real git commit so the thesis evidence trail has version history.

## Bottom Line

You are not stuck.

You are also not yet at the point where one prototype should be treated as the obvious answer.

The thesis has reached the point where the next work should be disciplined narrowing:

`broaden the screening just enough -> shortlist candidates -> write the stable chapters now -> prototype after the shortlist is defensible`
