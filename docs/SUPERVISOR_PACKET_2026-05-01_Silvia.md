# Supervisor Update Packet For Silvia

**Prepared for:** Silvia Tolu  
**Date to share:** 2026-05-01  
**Purpose:** concise pre-read for the postponed supervisor meeting  
**Core ask:** critique whether the current V0.1 reduced-order model is sufficient for choosing first sleeve/routing prototype candidates, and identify which decisions still need more modeling or experiments.

---

## Two-Page Memo Draft

### 1. Current State

Over the last two weeks, I moved from general design exploration toward a V0.1 reduced-order mechanical screening model for an index-finger sleeve/tendon-routing prototype. The model is intended to turn literature-driven biomechanical and robotic assumptions into concrete routing candidates before fabrication.

The current model should be framed narrowly:

> V0.1 is a mechanical design-space reduction model. It is not yet a full Parkinsonian finger-tapping dynamics model, a clinical performance model, or a final actuator design.

The model uses a planar rigid-link index finger with MCP/PIP/DIP joints, effective routing elements, and a distal thimble/anchor. It computes tendon path length, pull excursion, numerical sensitivity, tendon-induced torque, required passive holding torque, least-squares scalar tendon tension, residual torque mismatch, and fingertip trajectory.

Current implementation anchors:

- model code: `simulation_modeling/v01_model.py`
- sweep utilities: `simulation_modeling/candidate_sweep_utils.py`
- sweep notebook: `simulation_modeling/notebooks/05_candidate_sweep.ipynb`
- saved results: `simulation_modeling/results/`
- context update: `docs/STUDY_GUIDE.md`

### 2. Current Equation Story

Given a posture `q = [theta_MCP, theta_PIP, theta_DIP]`:

```text
1. Forward kinematics gives joint, fingertip, guide, and anchor positions.
2. Tendon length L(q) is the sum of straight segment distances.
3. Routing sensitivity is estimated by central difference: dL/dq.
4. Moment-arm equivalent: R(q) = -dL/dq.
5. Tendon torque: tau_tendon(q, T) = T * R(q).
6. Passive holding torque: tau_req(q) = K * (q - q0).
7. One scalar input tension is fit by least squares against tau_req.
8. The residual torque is reported as underactuation mismatch.
```

For a branched single input, the correct future extension is:

```text
R_total(q) = sum_j R_j(q)
tau_tendon(q, T) = T * R_total(q)
```

where `j` is a physical branch, not an independent actuator.

### 3. What Is Verified Versus Assumed

Verified in code/results:

- forward kinematics for a three-link planar finger
- effective routing elements attached to world/proximal/middle/distal frames
- tendon path length and branch pull excursion
- central-difference `dL/dq`
- moment-arm conversion from `mm/rad` to `m/rad` before torque/tension fitting
- least-squares scalar tension for one independent input
- candidate summary metrics and CSV exports
- coarse and refined two-guide candidate sweeps

Still assumed:

- passive stiffness values and their distribution across MCP/PIP/DIP
- coordinated flexion ratios used in the sweep
- straight-line tendon segments without friction, wrap, slack, stretch, or ring deformation
- 2D routing as a proxy for later left/right side routing
- comfort, pressure, donning, and palmar clearance as design filters rather than measured quantities

### 4. First Sweep Result

The current pipeline compares a single-branch two-guide routing family across:

- three scaled finger geometries
- three passive stiffness cases
- one coordinated flexion sweep

The best coarse-pass candidate was:

| Metric | Value |
|---|---:|
| model case | `large_nominal` |
| proximal guide long | `0.25` |
| middle guide long | `0.65` |
| guide offset | `-5.0 mm` |
| peak required tension | `1.77 N` |
| peak pull excursion | `21.4 mm` |
| RMS relative torque mismatch | `0.43` |
| heuristic score | `0.85` |

The best refined candidate shifted to:

| Metric | Value |
|---|---:|
| model case | `large_nominal` |
| proximal guide long | `0.20` |
| middle guide long | `0.75` |
| guide offset | `-4.0 mm` |
| peak required tension | `1.82 N` |
| peak pull excursion | `19.8 mm` |
| RMS relative torque mismatch | `0.34` |
| heuristic score | `0.75` |

Interpretation: the refined pass reduced torque-distribution mismatch while keeping tension and pull requirements in a plausible range. This supports using the model to narrow routing regions, but not to freeze final prototype geometry.

### 5. Critical Caveat

The current rankings depend directly on the passive stiffness strategy. If passive joint stiffness changes, then required torque, fitted tendon tension, torque mismatch, actuator plausibility, and candidate ranking can all change.

The most important technical question for Silvia:

> What is the thesis-safe strategy for passive stiffness now: continue the current nominal/mid/high screening sweep, broaden it with literature-informed stiffness values, calibrate a nominal passive law with a simple benchtop test before selecting the prototype, or treat passive stiffness as a primary uncertainty axis in the first prototype decision?

### 6. Skylab And Resource Update

The resource situation is better than previously understood. Skylab appears to offer fabrication support, expert design review, prototyping guidance, innovation coaching, and grant-navigation support. A joint meeting with Michael and Michael Holbeck may be useful to clarify:

- what prototype fabrication support is realistic
- whether TPU/FDM or other soft-manufacturing support is available
- what design review should happen before fabrication
- whether a startup/company or grant path is worth discussing

This lowers the practical risk of moving toward a first prototype after the next routing pass. It should not expand the thesis scope prematurely.

The company/SOI ownership question is better handled verbally with Silvia, not as a hard written agenda demand.

### 7. Decisions Needed From Silvia

1. Is the V0.1 quasi-static model sufficient for selecting first sleeve/routing candidates?
2. Which passive stiffness strategy is most defensible?
3. Which output metrics should define a "good enough to fabricate" candidate?
4. Should the next pass prioritize more routing families, two-branch routing, or passive-stiffness calibration?
5. Should actuation stay separate from routing until stroke/tension requirements are clearer?
6. How should "variable stiffness" be defined for this thesis: actuator-side, transmission-side, joint-level, endpoint-level, or controller-rendered?
7. What should be included in a Skylab design-review meeting?

### 8. Proposed Next 7-14 Days

1. Clean the current sweep figures into presentation-ready visuals.
2. Add at least one additional routing family beyond the current single-branch two-guide case.
3. Extend the model to symmetric two-branch routing and report branch imbalance.
4. Treat passive stiffness as an uncertainty sweep unless Silvia prefers immediate calibration.
5. Produce 3-5 candidate sketches with tension, pull, mismatch, and feasibility notes.
6. Prepare a minimal BOM for a routing-adjustable benchtop mock-up.
7. Set up a Skylab design-review conversation if Silvia agrees.

---

## Six-Slide Appendix Outline

### Slide 1 - What Changed Since The Last Update

**Claim:** The project has moved from mechanism exploration to a working V0.1 routing-screening model.

Show:

- one-line thesis scope
- V0.1 model purpose
- current result: first coarse/refined sweep completed
- next decision: whether this is enough to guide prototype candidates

### Slide 2 - V0.1 Model Boundary

**Claim:** The model is deliberately mechanical and reduced-order.

Show:

- "does" column: routing geometry, excursion, moment arms, tension, mismatch
- "does not" column: clinical improvement, dynamic tapping frequency, sequence effect, patient adaptation
- one sentence: "mechanical interface first, controls/dynamics later"

### Slide 3 - Equations And Implementation

**Claim:** The model has a clear chain from geometry to prototype metrics.

Show:

```text
q -> FK -> L(q) -> dL/dq -> R(q) -> T_req -> tau_error
```

Small implementation map:

| Block | File |
|---|---|
| kinematics/routing | `v01_model.py` |
| candidate generation | `candidate_sweep_utils.py` |
| sweep notebook | `05_candidate_sweep.ipynb` |
| outputs | `results/` |

### Slide 4 - First Candidate Sweep

**Claim:** The first sweep already narrows promising routing regions.

Show:

- current best refined candidate
- peak tension: `1.82 N`
- pull: `19.8 mm`
- RMS relative mismatch: `0.34`
- include `candidate_run_02.png` or a cleaned remake

Visual note: do not present this as final geometry.

### Slide 5 - Main Technical Caveat

**Claim:** Passive stiffness is the key uncertainty before prototype sizing.

Show:

```text
K changes -> tau_req changes -> T_req changes -> mismatch changes -> ranking changes
```

Ask Silvia to choose:

- nominal/mid/high sweep, broader literature sweep, or quick calibration
- quick calibration test
- passive stiffness as primary uncertainty axis

### Slide 6 - Decisions, Resources, And Next Step

**Claim:** The next step is a controlled prototype path, not more open-ended exploration.

Show:

- decisions requested from Silvia
- Skylab resources now look more available
- next 7-14 days
- possible Skylab design-review meeting

---

## Agenda Update For The Postponed Meeting

1. **Current V0.1 model status**
   - what is implemented
   - what is deliberately out of scope
   - first sweep outputs

2. **Passive stiffness and model validity**
   - whether current assumptions are sufficient
   - whether to sweep, calibrate, or reframe stiffness

3. **Prototype candidate criteria**
   - acceptable tension/pull/mismatch ranges
   - how many routing candidates to sketch
   - when a candidate is "good enough to fabricate"

4. **Actuation and variable stiffness**
   - keep TSA/pulley separate until requirements are clearer
   - define variable stiffness level for the thesis

5. **Skylab and prototyping resources**
   - design review
   - fabrication support
   - possible innovation/grant discussion

6. **Next 7-14 days**
   - next routing-family sweep
   - two-branch extension
   - candidate sketches
   - BOM and design-review prep

## Materials To Link Or Attach

- [April 30 Silvia update note](../notes/Meetings/2026_30_04_Silvia_Updates.md)
- [Living study guide](STUDY_GUIDE.md)
- [Current task](CURRENT_TASK.md)
- [Candidate sweep notebook](../simulation_modeling/notebooks/05_candidate_sweep.ipynb)
- [Candidate run 01](../simulation_modeling/results/candidate_run_01.png)
- [Candidate run 02](../simulation_modeling/results/candidate_run_02.png)
- [April 24 journal club note](../notes/Meetings/2026_24_04_Journal_Club.md)
