# THESIS_PROGRESS

This is the running progress document for the thesis.

Purpose:

- keep a readable narrative of what has been clarified, built, and left open
- make future thesis writing easier by preserving the project story as it develops
- connect literature work, modeling work, design decisions, and validation planning
- avoid relying on chat history as the memory of the thesis

Related files:

- `docs/THESIS_BRIEF.md`: stable scope and project framing
- `docs/CURRENT_TASK.md`: one active primary task at a time
- `docs/DECISION_LOG.md`: committed decisions and rationale
- `docs/STUDY_GUIDE.md`: source-verified literature synthesis for writing
- `docs/TOPIC_MEMOS/`: topic-specific synthesis and working reasoning
- `notes/Meetings/`: meeting preparation and follow-up notes
- `simulation_modeling/`: notebooks, scripts, and reduced-order model code

## Current Snapshot

**Last updated:** 2026-04-28

**Project phase:** reduced-order routing geometry established; passive mechanics and underactuation scoring now being connected.

The thesis is currently moving from broad literature framing toward a simulation-first design comparison for a simplified index-finger actuation system. The main active repo task is now the design-screening mechanics layer for the reduced-order tendon-routing model. The modeling branch has a working three-link tendon-routing geometry model in `simulation_modeling/v0_model.py` and a first passive-joint torque module in `simulation_modeling/passive_joint_models.py`; it can now compare passive required torque against tendon torque per newton and start quantifying underactuation mismatch.

Current thesis direction in one sentence:

`Use a simplified, interpretable finger-actuator model to compare variable-stiffness and tendon-routing design options, then validate the most defensible reduced-order behavior with a benchtop index-finger mock-up.`

Current lab-presentation version:

`The model is becoming a design-screening tool: it compares routing choices by excursion, posture-dependent leverage, branch balance, and rough input-tension requirements before the hardware locks into TSA, CVT/CTA, a soft actuator, or a simpler tendon-series-stiffness branch.`

Current modeling formula to preserve:

`tau_tendon(q, T) = -T * partial L(q) / partial q`

For one independent tension input spanning MCP/PIP/DIP, the next useful scoring step is not independent joint-by-joint tension division. If that input splits into left/right physical branches, the branch moment-arm vectors should be summed first. Then the scalar input tension is fit against the required torque vector, with the residual torque reported as underactuation mismatch.

## Scope Status

### Stable Scope

- The thesis is about a simplified finger-actuator system, not a full wearable glove.
- The work should proceed simulation first, then physical mock-up validation.
- Variable stiffness remains central, but the implementation route is still open.
- Sensing is secondary unless later evidence makes it essential.
- Parkinson finger tapping and thumb-index opposition are useful task framings, but the thesis should avoid making clinical efficacy claims.

### Current Tension

There are two legitimate design identities competing:

1. a soft variable-stiffness actuator identity, such as a dorsal zig-zag or strain-limiting-layer actuator
2. a mechanically cleaner tendon-routing identity, such as a side/palmar-lateral tendon routed through removable rings to a distal thimble

The current modeling task should compare these without prematurely locking the prototype.

The current decision posture is deliberately staged: routing and torque/excursion requirements first, actuator architecture second. TSA and CVT/CTA-style ideas remain candidate actuation or transmission branches, but they should not be treated as v0 assumptions.

## Literature Progress

### Established Literature Infrastructure

- Zotero remains the bibliographic and PDF source of truth.
- `refs/PAPER_TRACKER.csv` tracks papers, status, priority, and note paths.
- `notes/papers/` holds per-paper reading notes.
- `docs/STUDY_GUIDE.md` stores writing-facing synthesis only when claims are source-checked.
- `docs/CLAIM_REGISTRY.md` stores reusable cross-paper claims.

### Current Literature Findings

- Direct Parkinson finger-tapping assistance hardware appears sparse compared with assessment literature.
- The Parkinson finger-tapping literature is currently more useful for defining movement features and validation outputs than for choosing a mechanism.
- Near-adjacent hardware precedents include MCP/index-finger exoskeletons, pinch devices, tendon-driven soft gloves, soft pneumatic actuators, and variable-stiffness robotic finger mechanisms.
- The most useful mechanism precedents for the current tendon-routing question include:
  - Exo-Glove Poly II for thimble anchoring, passive thumb support, tendon path length, and slack modeling
  - Bagneschi et al. 2023 for soft open rings and lateral tendon routing
  - Abdelhafiz et al. 2023 for bioinspired radial/ulnar tendon routing and joint coordination
  - Gallup et al. 2025 for quasi-static tendon-force modeling with compliant joints
  - Zhou et al. 2024 for comparing tendon transmission paths as design variables

### Literature Work Still Needed

- Resume and finish the broader Parkinson device landscape memo after the current modeling/design-screening task reaches a stable checkpoint.
- Source-verify exact quotes and page numbers for papers likely to appear in thesis writing.
- Decide which papers are direct mechanism precedents versus contextual framing papers.
- Promote the tendon-routing search branch into the tracker and paper notes as papers are screened.

## Modeling Progress

### Existing Modeling Baseline

The repo already contains a simulation-modeling workstream, including:

- a 1-DOF quasi-static MCP starting notebook
- reduced-order model code for simple finger/actuator interaction
- method notes on quasi-static finger modeling and modeling-paper audit

The current modeling philosophy is stable:

- start with the simplest defensible model
- keep assumptions explicit and parameterized
- separate kinematics, passive mechanics, actuator/transmission mechanics, and validation outputs
- avoid full FEM unless a later result makes it necessary

### Current Modeling Direction

The current simulation branch is now a working index-finger tendon-routing sandbox with:

1. planar three-link index finger with MCP/PIP/DIP joints
2. configurable routing elements attached to world or phalanx frames
3. distal thimble anchor point
4. tendon path length as a function of joint angles
5. tendon segment-length decomposition
6. fingertip trajectory and finger-routing visualization
7. local numerical tendon-length gradient with respect to MCP, PIP, and DIP angles
8. tendon torque mapping from `tau_tendon = -T * dL/dq`
9. coordinated flexion sweeps and reusable Plotly summary figures for path length, excursion, and gradient

The geometry stage has now clarified several thesis-relevant facts:

- a simple planar reduced-order model is sufficient for early routing and stroke questions
- the current palmar routing shortens smoothly during physiological flexion under the chosen sign convention
- the dorsal extension comparison path lengthens during the same flexion sweep, which is a useful sanity check
- same-phalanx tendon segments remain constant while segments spanning different bodies vary with posture
- routing sensitivity is posture-dependent and currently strongest at MCP, then PIP, then DIP
- the current fixed world entry point means flexion and extension paths should not be expected to be perfect mirror images

The next mechanics stage should add:

1. passive joint torque models at MCP/PIP/DIP
2. quasi-static equilibrium solving
3. routing-variant scorecards for ring count, placement, excursion, and tension demand
4. later comparison of antagonistic extension paths and bench-top measurements

The key modeling relationship to preserve is:

```text
tau_i = -F_tendon * partial x_tendon / partial theta_i
```

This connects tendon routing geometry to joint torque without hand-assigning arbitrary forces at the joints.

### Modeling Questions Still Open

- Which passive joint law is the right first mechanics layer: linear torsional spring, nonlinear spring, or literature-fitted passive torque?
- Should the first multi-joint equilibrium stage keep MCP/PIP/DIP independent, or impose a simple DIP-PIP coupling?
- Should the first mechanics comparison target generic flexion, finger tapping, or pinch-like closure?
- How should fingertip force be defined before explicit contact with an object or passive thumb pad is added?
- How much tendon friction or slack should stay ignored in the first equilibrium model?
- Should variable stiffness enter first as tendon-series stiffness, actuator stiffness, or as a separate later comparison once the baseline torque balance works?

## Design And Prototype Progress

### Current Candidate Branches

The current design space has been narrowed to a few candidate branches:

| Branch | Status | Why It Matters |
|---|---|---|
| Dorsal zig-zag soft actuator plus thimble | promising but unproven | closest to soft variable-stiffness actuator identity |
| Side/palmar-lateral flexion tendon plus thimble and rings | promising | cleanest mechanics and easiest to simulate/validate |
| Dorsal extension return or support | secondary | useful for repeated flexion/extension or tapping-like motion |
| Antagonistic flexion/extension tendons | stage 2 | best bidirectional control, but adds slack/routing complexity |
| Passive thumb pad or passive thumb opposition structure | likely useful | enables pinch-like validation while keeping the active system index-focused |
| TSA, CVT, or CTA transmission | candidate after sizing | should be evaluated after routing gives stroke, torque, and tension requirements |

### Current Design Hypothesis

The first buildable mock-up should probably not be a full glove. A better first prototype candidate is:

`index thimble + two or three removable soft rings + tendon transmission + optional passive thumb/contact pad`

This allows ring count and ring position to be tested rather than assumed.

Comfort and task access are now explicit design filters: preserve palmar contact as much as possible, avoid bulky dorsal cages, and treat straps/rings as retention and routing features rather than as a full wearable glove architecture.

### Design Questions Still Open

- Which side of the index finger should carry the primary flexion tendon path?
- How many rings are needed before the tendon path becomes mechanically useful?
- Can the rings be removable enough to support experiments with different routing layouts?
- Will palmar-lateral routing interfere with pinch/tapping contact?
- What is the smallest passive thumb/contact setup that gives useful validation data?

## Validation Planning

Current likely validation outputs:

- joint angle trajectory
- fingertip trajectory
- tendon stroke
- tendon tension
- fingertip force against an object or passive pad
- repeatability over repeated cycles
- sensitivity to ring placement and finger length
- comparison between simulated and measured posture or marker positions

Validation should start with bench-top mechanical behavior, not clinical claims.

## Progress Log

### 2026-04-24

- Consolidated the recent working thesis context into `docs/STUDY_GUIDE.md` under a separate non-writing-safe project-context section.
- Clarified the current model identity: an ordered routing path made of `entry`, `guide`, and `anchor` elements attached to body frames, not a literal one-to-one model of every physical ring or slot.
- Confirmed the presentation-safe interpretation of the latest routing outputs: flexion path shortens, extension path lengthens, excursions have the expected sign, and gradients are smooth and posture-dependent.
- Reframed the simulation branch as a design-screening framework that should compare routing alternatives under explicit metrics and constraints.
- Clarified that TSA, CVT, and CTA ideas are actuator/transmission candidates to evaluate after stroke, moment-arm, and tension requirements are estimated.
- Added a dated lab-update presentation packet for the 2026-04-24 lab discussion.

### 2026-04-22

- Consolidated the first working three-link routing model in `simulation_modeling/v0_model.py`.
- Confirmed the core modeling abstraction: planar 2D, three rigid phalanges, three revolute joints, one routed palmar tendon, fixed local guide points, and quasi-static interpretation.
- Implemented and validated forward kinematics, routing-point transforms, total tendon length, tendon segment lengths, fingertip path, and geometry plots.
- Resolved the sign convention so physiological flexion is represented by negative joint angles in the current coordinate setup.
- Verified that the routed palmar tendon shortens smoothly and monotonically during the tested coordinated flexion sweep, with about 6.6 mm total excursion for the current geometry.
- Confirmed that same-phalanx tendon segments remain constant while cross-body segments vary with posture, which explains why the total path length changes despite rigid links.
- Implemented the local numerical gradient `dL/dq` and clarified the difference between a sweep derivative and the mechanics-relevant partial derivatives at a single posture.
- Established that the gradient is posture-dependent and currently strongest at MCP, providing the geometric quantity needed for generalized tendon torque in the next stage.

### 2026-04-20

- Added `docs/TOPIC_MEMOS/11_tendon_routing_and_ring_placement.md`.
- Added recurring search topic `T011` for tendon routing and ring placement.
- Screened Exo-Glove Poly II for mechanism/model relevance and updated its paper note.
- Clarified that Exo-Glove Poly II is best for tendon kinematics and slack, while Gallup 2025 is stronger for force/torque modeling.
- Clarified that the first useful simulation should compare routing variants, not simply animate a fixed concept.
- Created this thesis progress document.

### 2026-04-17

- Supervisor follow-up clarified that the next step should not be to lock the final prototype immediately.
- Current priority became comparing design options against feasibility, modeling value, and thesis scope.
- Design branches discussed included dorsal zig-zag soft actuator, side-routed tendon with thimble, and antagonistic tendon routing.

### 2026-04-10 To 2026-04-15

- Modeling notes were consolidated around quasi-static reduced-order finger modeling.
- The strongest modeling direction became: start simple, then add geometry-aware actuator/finger interaction.
- Meeting preparation connected clinical finger-tapping features to engineering outputs without overclaiming clinical efficacy.

### 2026-03-27 To 2026-04-06

- Repo structure was formalized into Literature and Simulation Modeling workstreams.
- Decision log established the one-repo, two-workstream structure.
- Study guide and paper-note workflows were established to keep source-backed literature synthesis separate from chat reasoning.
- Topic memos began mapping soft finger actuation, variable stiffness, finger biomechanics, validation, pinch/finger-tapping technologies, and thesis positioning.

## Writing-As-You-Go Notes

These sections are likely to become thesis material later, but they still need source verification before being used as final prose.

Potential thesis sections:

- Introduction and motivation:
  - neurorehabilitation context
  - Parkinson finger-tapping relevance as movement framing
  - why simplified finger assistance is a defensible engineering target
- Literature review:
  - finger-tapping assessment versus assistance
  - tendon-driven hand exoskeletons
  - soft hand exoskeletons and wearable routing problems
  - variable-stiffness actuation for finger systems
  - reduced-order finger and tendon modeling
- Methods:
  - reduced-order finger model
  - tendon-routing kinematics
  - passive joint stiffness assumptions
  - actuator or series-stiffness model
  - bench-top validation setup
- Results:
  - routing comparison
  - stiffness comparison
  - simulated versus measured behavior
  - sensitivity to geometry and parameters
- Discussion:
  - what the simplified model captures
  - what it misses
  - implications for future soft wearable hand devices

## How To Update This File

Update this file when one of these happens:

- a design branch becomes more or less likely
- a modeling assumption changes
- a literature cluster changes the thesis direction
- a supervisor meeting changes the scope
- a simulation or prototype milestone is reached
- a validation metric becomes clearly important or clearly unnecessary

Each update should add:

1. a short dated entry in `Progress Log`
2. any changed assumptions in the relevant section
3. links to the topic memo, decision entry, paper note, notebook, or meeting note that supports the change
