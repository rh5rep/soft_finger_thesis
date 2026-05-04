# Thesis Literature Study Guide

This is the canonical thesis study guide for literature already captured in the repo.

It is a living synthesis document, but it is intentionally stricter than chat notes:

- do not add claims from memory alone
- do not add paraphrases unless they can be traced to a paper note
- keep exact quotes, page numbers, and figure references in the per-paper notes under `notes/papers/`
- use Zotero as the source of truth for PDFs and bibliographic storage
- use this guide for thesis-facing synthesis only

## How To Use This Guide

1. Read or screen a paper from Zotero.
2. Update its note in `notes/papers/`.
3. Log exact quotes and page numbers in the paper note before reusing any wording.
4. Only then add a synthesis statement here.
5. If a statement here is not backed by a paper note, remove it or mark it as pending verification.

## Evidence Rules

- `Verified synthesis` means the statement is backed by at least one paper note with source-checked content.
- `Exact quote available` means the quote and page number live in the paper note, not only in chat.
- `Pending verification` means the idea exists in a memo or discussion but has not yet been checked against the source PDF closely enough for writing use.

## Current Status

As of `2026-04-24`, this guide remains the source-verified synthesis entry point, but the thesis now also has a separate working project context section below. Use [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md) as the operational ledger for what is captured, extracted, or still pending.

Important boundary:

- `Topic Map` and `Writing-Safe Statement Bank` are for source-verified literature synthesis.
- `Working Project Context` records current thesis decisions, modeling status, and presentation context. It is useful for meetings and planning, but it is not automatically writing-safe thesis prose.

## Working Project Context

### 2026-04-30 V0.1 Modeling And Supervisor-Update Context

Status:
- `Project decision / discussion synthesis`, not writing-safe literature prose.
- This entry updates the working context after the first candidate-screening sweep and the Skylab resource clarification.

Current V0.1 framing:
- The current model should be described as a reduced-order mechanical design-screening model for an index-finger sleeve/tendon-routing prototype.
- It is not a full model of Parkinsonian finger tapping, dynamic tapping frequency, sequence effect, patient-specific adaptation, or clinical performance.
- The defensible claim is that V0.1 can narrow sleeve/routing geometry before fabrication by comparing excursion, moment-arm behavior, required tension, fingertip trajectory, and underactuation mismatch.

Current implemented candidate-screening layer:
- The current candidate pipeline evaluates a single-branch two-guide routing family over a coordinated flexion sweep.
- The sweep covers scaled finger geometries and passive stiffness cases.
- The model computes required passive holding torque, total tendon moment-arm vector, least-squares scalar tendon tension, fitted tendon torque, residual torque error, pull excursion, fingertip trajectory, and score/rejection metrics.
- Current saved outputs live under `simulation_modeling/results/`.

Current best refined candidate, for discussion only:
- model case: `large_nominal`
- proximal guide longitudinal fraction: `0.20`
- middle guide longitudinal fraction: `0.75`
- guide offset: `-4.0 mm`
- distal anchor longitudinal fraction: `0.80`
- distal anchor offset: `-4.0 mm`
- tendon entry: `(-8.0, -4.0) mm`
- approximate outputs: peak tension `1.82 N`, peak pull `19.8 mm`, RMS relative torque mismatch `0.34`, heuristic score `0.75`

Interpretation:
- The refined pass suggests the model is already useful for narrowing promising routing regions.
- The current result should not be treated as final prototype geometry because it depends on passive stiffness assumptions and only covers the current single-branch two-guide family.
- The most important supervisor question is whether passive stiffness should stay as the current nominal/mid/high screening sweep, be broadened with literature-informed stiffness values, be calibrated with a quick experiment, or be treated as a primary uncertainty axis in the prototype decision.

Current next modeling steps:
- widen candidate-family coverage beyond the current single-branch two-guide family
- tighten rejection thresholds and candidate bounds around promising regions
- generate 2D sketch-style visuals for the top `3-5` candidates or top `3-5` per routing family
- extend the routing model from one branch to two branches
- test whether symmetric two-branch routing is enough or whether asymmetric left/right routing belongs in the design space

Current Skylab resource context:
- The earlier concern about lack of prototyping resources is reduced but not fully closed.
- Skylab appears to offer more fabrication, design-review, expert, coaching, and grant-navigation support than previously understood.
- A joint meeting with Skylab innovation partners may be useful to clarify prototyping support, design review, startup/company path, and grant options.
- This should be kept as a resource and strategy update, not as a reason to expand the thesis scope prematurely.

### 2026-04-24 Consolidated Thesis Context

Status:
- `Project decision / discussion synthesis`, not a substitute for source-verified paper notes.
- Use this section to orient lab presentations, supervisor conversations, and next modeling tasks.
- Promote specific literature claims into the `Topic Map` or `Writing-Safe Statement Bank` only after checking the corresponding paper note.

Current thesis framing:
- The thesis is anchored on a simplified finger-actuator system, not a full hand glove.
- The workflow remains simulation first, followed by a bench-top mock-up and experimental validation.
- Variable stiffness is the central research theme, but the first model should establish routing geometry, excursion, and force requirements before committing to a complex actuator architecture.
- Parkinson finger tapping is a useful clinical task lens because it connects the engineering outputs to amplitude, speed, rhythm, decrement, and irregularity without requiring clinical efficacy claims.

Current motor-task interpretation:
- The useful framing is not `bradykinesia = slowness`.
- The working interpretation separates slowness, reduced amplitude or hypokinesia, sequence effect, and hesitation/irregularity.
- The current reduced-order model is best suited to the amplitude, excursion, leverage, and tendon-tension side of that task, rather than rhythm or sequence-effect modeling.

Current modeling abstraction:
- Use a planar 2D index-finger model with rigid proximal, middle, and distal phalanges and revolute MCP/PIP/DIP joints.
- Represent a tendon as an ordered routing path made of mechanically meaningful routing elements: `entry`, `guide`, and `anchor`.
- Treat physical rings, straps, slots, and thimbles as effective routing elements in the first model, rather than modeling every local contact detail.
- Approximate tendon path length as straight segments between effective routing points.
- Keep friction, pulley radii, wrap/contact mechanics, soft-tissue pressure, tendon stretch, and dynamics out of v0.

Current sign convention:
- Zero joint angles mean the finger is straight along `+x`.
- Positive rotation is counterclockwise.
- Negative joint angles represent physiological flexion for the current palmar routing setup.
- With that convention, the current palmar/flexion path shortens in flexion and the dorsal/extension path lengthens in flexion.

Current mechanics bridge:

```text
tau_tendon = -T * partial L / partial q
```

This is the key step from geometry to mechanics: once the model computes tendon path length and its posture-dependent gradient, assumed tendon tension can be mapped to generalized joint torque.

Current underactuation note:
- For one independent tension input spanning MCP/PIP/DIP, one scalar tension cannot independently match three joint torques, even if the physical route splits into left/right branches.
- If one input drives multiple branches, compute each branch length and moment-arm vector, sum the branch torque-per-newton vectors, then project the required torque onto that total torque-per-newton direction.
- For a required torque vector, the next model should estimate the best scalar input tension by projecting the required torque onto the total routing torque-per-newton direction, then report the residual torque error as underactuation mismatch.
- This should be treated as a design-screening calculation, not as proof that one tendon fully controls all joints.

Current tapping-coupling verification gap:
- Tapping-specific joint coordination should not be inferred only from curl, fist-closure, or grasp data.
- Candidate sources to add to the literature tracker and verify in paper notes include `Finger joint coordination during tapping` and `Finger joint impedance during tapping on a computer keyswitch` from *Journal of Biomechanics*.
- Until those papers are extracted, MCP/PIP/DIP coupling ratios in the model should be treated as scenario assumptions rather than writing-safe anatomical claims.

Current design-screening logic:
- The model should compare candidate routings, not merely show that one routing is plausible.
- Candidate design variables include independent input count, branch count per input, ring or routing-element count, longitudinal placement, dorsal/palmar/lateral offset, splitter or entry location, anchor location, and thimble geometry.
- Candidate outputs include total excursion, peak input tension, leverage distribution across MCP/PIP/DIP, branch imbalance, smoothness, monotonicity, palmar clearance, and hardware simplicity.
- Candidate constraints include palmar contact clearance, comfort, manufacturability, wearable geometry, acceptable tendon load, and bench-top prototype compatibility.

Current actuator implication:
- Twisted string actuation may be feasible later, but it should not be assumed necessary for v0.
- TSA alone should not be treated as equivalent to variable stiffness.
- CVT/CTA or other variable-transmission ideas matter only after the model shows the needed posture-dependent tradeoff between speed, stroke, and torque.
- The immediate modeling priority is to estimate stroke, moment-arm/gradient behavior, and tension requirements before choosing the final actuator architecture.

Current hardware concept:
- Prefer a distal thimble or fingertip cap for secure attachment.
- Prefer soft rings, retainers, side-routed cords, or dorsal/lateral routing features over a bulky rigid full-finger cage.
- Keep the palmar side as unobstructed as possible for tapping, pinch, and comfort.
- Treat intermediate supports as retention/routing features, not necessarily as separate detailed geometric objects in v0.
- A bench-top prototype should preserve routing adjustability so ring count and placement can be tested.

## Topic Map

### 1. Parkinson Task And Device Framing

Scope:
- finger tapping as a clinical task
- Parkinson device landscape relevant to thesis positioning
- assessment systems versus assistive hardware versus stabilization systems

Verified synthesis:
- `Bologna 2020` and `Paparella 2026` support treating Parkinson bradykinesia as a multi-feature phenomenon rather than a single generic slowness variable. `Bologna 2020` frames bradykinesia through slowness, reduced amplitude, and sequence effect, while `Paparella 2026` argues that using `bradykinesia and associated features` is often more appropriate than the narrower current clinical wording. Evidence: [p2020_bologna_bradykinesia_concepts.md](../notes/papers/p2020_bologna_bradykinesia_concepts.md), [p2026_paparella_bradykinesia_complex.md](../notes/papers/p2026_paparella_bradykinesia_complex.md)
- `Zarrat Ehsan 2026` is currently one of the strongest direct finger-tapping assessment anchors in the repo: it evaluates `4,073` videos from `446` people with Parkinson's disease, operationalizes the task as a normalized thumb-index distance signal, and organizes analysis around `hypokinesia`, `bradykinesia`, `sequence effect`, and `hesitation-halts`, while showing that those domains expand into a richer `six-component` structure in practice. Evidence: [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)
- `Ravichandran 2023` and `Amo-Salas 2024` together show that the direct Parkinson finger-tapping literature is strong on assessment systems: one provides a wearable glove-based tele-assessment platform, the other maps the computer-vision assessment literature and describes finger tapping as one of the more sensitive MDS-UPDRS items. Evidence: [p2023_ravichandran_itex_gloves.md](../notes/papers/p2023_ravichandran_itex_gloves.md), [p2024_amo_salas_pd_ft_survey.md](../notes/papers/p2024_amo_salas_pd_ft_survey.md)

Pending verification:
- The exact clinical task wording still needs care because at least one current assessment paper contains internal ambiguity between `10 times` and `10 seconds`.

Core paper buckets:
- task and motion framing
- Parkinson finger tapping assessment systems
- broader Parkinson assistive and control-device landscape

### 2. Direct And Near-Adjacent Repetitive Finger-Motion Devices

Scope:
- direct tapping-like devices
- repeated flexion-extension systems
- MCP-centered exoskeletons
- index-finger exoskeletons

Verified synthesis:
- `Sun 2021` shows that a self-aligning rigid index-finger exoskeleton can preserve richer motion than an MCP-only design: the paper reports a three-motor architecture, a spatial `P3RPU` MCP mechanism, a `65.8%` reduction in standardized reaction-force square sum, and trajectory correlations of `0.930`, `0.840`, and `0.954` for MCP f/e, MCP a/a, and PIP f/e. Evidence: [p2021_sun_self_aligning_index_finger.md](../notes/papers/p2021_sun_self_aligning_index_finger.md)
- `Peperoni 2023` is a strong MCP-dominant precedent for a simplified first device because it combines self-alignment, an `RPR` architecture with a geared virtual hinge, and joint-level estimation; the paper reports MCP-angle RMSE below `5 degrees`, residual torque below `7 mNm`, and torque-tracking RMSE below `8 mNm`. Evidence: [p2023_peperoni_self_aligning_mcp.md](../notes/papers/p2023_peperoni_self_aligning_mcp.md)
- `Peperoni 2024` shows the same MCP-centered I-Phlex line can be used in a clinical pilot workflow: the abstract reports median PROM and AROM increases of `5.88%` and `11.11%`, no major adverse event, and no statistically significant difference between exoskeleton ROM measurements and therapist goniometer measurements. Evidence: [p2024_peperoni_iphlex_mcp.md](../notes/papers/p2024_peperoni_iphlex_mcp.md)

Pending verification:
- Whether direct tapping-assist devices exist in sufficient number to displace MCP/index-finger exoskeletons as the main hardware precedent class.

Core tracker topics:
- `T008` Direct tapping-like and repetitive finger-motion devices
- `T009` Index finger and MCP-joint exoskeletons

### 3. Pinch And Thumb-Index Comparison Bucket

Scope:
- pinch grasp exoskeletons
- thumb-index opposition devices
- comparison cases rather than primary mechanism precedents

Verified synthesis:
- _No source-verified synthesis entered yet._

Pending verification:
- Current memo-level reasoning suggests these papers remain useful as comparison points, but not as the main mechanical analog for tapping-like motion.

Core tracker topics:
- `T006` Pinch grasp exoskeletons
- `T007` Thumb-index opposition support

### 4. Mechanism And Modeling Foundations

Scope:
- soft finger actuation
- variable-stiffness mechanisms
- simplified finger biomechanical models
- validation methods
- rehabilitation-device positioning

Verified synthesis:
- _No source-verified synthesis entered yet._

Pending verification:
- These topics remain important for the thesis architecture, but this guide should not promote them into writing-safe statements until the corresponding paper notes have source-verified summaries or quote banks.

Core tracker topics:
- `T001` Soft finger actuation
- `T002` Variable-stiffness mechanisms
- `T003` Finger biomechanics models
- `T004` Validation methods
- `T005` Rehabilitation positioning

## Writing-Safe Statement Bank

Add only statements that are ready to reuse in thesis drafting.

- Current direct assistive hardware for repeated finger motion appears stronger in MCP-centered and index-finger exoskeletons than in explicit Parkinson finger-tapping assistance devices. Verified support so far: [p2021_sun_self_aligning_index_finger.md](../notes/papers/p2021_sun_self_aligning_index_finger.md), [p2023_peperoni_self_aligning_mcp.md](../notes/papers/p2023_peperoni_self_aligning_mcp.md), [p2024_peperoni_iphlex_mcp.md](../notes/papers/p2024_peperoni_iphlex_mcp.md)
- An MCP-dominant abstraction is defensible as an initial thesis mechanism baseline because at least one technically rigorous exoskeleton paper and one clinical pilot in the same line both operate at that level of simplification. Verified support: [p2023_peperoni_self_aligning_mcp.md](../notes/papers/p2023_peperoni_self_aligning_mcp.md), [p2024_peperoni_iphlex_mcp.md](../notes/papers/p2024_peperoni_iphlex_mcp.md)
- The Parkinson finger-tapping literature in this repo currently supports a strong assessment track but a weak direct assistance track: the best-developed direct evidence is on task quantification, symptom decomposition, and wearable or vision-based measurement, not on tapping-specific assistive exoskeletons. Verified support: [p2020_bologna_bradykinesia_concepts.md](../notes/papers/p2020_bologna_bradykinesia_concepts.md), [p2026_paparella_bradykinesia_complex.md](../notes/papers/p2026_paparella_bradykinesia_complex.md), [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md), [p2023_ravichandran_itex_gloves.md](../notes/papers/p2023_ravichandran_itex_gloves.md), [p2024_amo_salas_pd_ft_survey.md](../notes/papers/p2024_amo_salas_pd_ft_survey.md)

## Next Audit Pass

- fill the audit status in the highest-priority paper notes first
- add exact quotes with page numbers for papers most likely to appear in the thesis framing
- promote only source-verified claims from paper notes into this guide
