
# Presentation Recall Notes 2026-03-27

Use this file as a `quick recall sheet`, not a speaking coach.

It is organized by the current slide order in [3-26-presentation-draft.pptx](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/3-26-presentation-draft.pptx).

For each slide, keep in mind:

- `what this slide is claiming`
- `which paper/device actually supports it`
- `technical details worth recalling`
- `the clean limit / caveat`

## Slide 1. Review Question

## Claim

- There is no strong mature direct category of `Parkinson finger-tapping assist exoskeletons`.
- The literature separates more cleanly into:
  - `assessment`
  - `near-adjacent repetitive-motion hardware`
  - `stabilization / tremor suppression`

## Core Evidence Buckets

- `Assessment`: [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md), [p2023_ravichandran_itex_gloves.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2023_ravichandran_itex_gloves.md)
- `Near-adjacent hardware`: [p2023_peperoni_self_aligning_mcp.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2023_peperoni_self_aligning_mcp.md), [p2024_peperoni_iphlex_mcp.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2024_peperoni_iphlex_mcp.md), [p2021_sun_self_aligning_index_finger.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2021_sun_self_aligning_index_finger.md)
- `Stabilization`: [p2025_andong_helm_tremor.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2025_andong_helm_tremor.md)

## Fast Recall

- `Direct task literature` exists mostly as measurement/assessment.
- `Device precedent` exists mostly as MCP/index-finger rehab hardware.
- `Steady finger` is better matched by tremor-suppression papers than by tapping papers.

## Caveat

- Missing direct tapping-assist hardware is a `literature result`, not a failed search.

## Slide 2. Pinch Is Not Finger Tapping

## Claim

- `Pinch/grasp` and `finger tapping` both involve thumb-index interaction, but they are mechanically and clinically different task families.

## Pulp Pinch 2024 Recall

Source:
[p2024_andres_esperanza_pulp_pinch.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2024_andres_esperanza_pulp_pinch.md)

- Rehabilitation exoskeleton for `pulp pinch grasp` after stroke.
- `Underactuated` single-DOF design.
- Topology:
  - `eight links`
  - `two consecutive four-bar mechanisms`
  - `third inversion of a crank-slider`
- Customized from `3D scans` of the patient hand.
- Small `linear actuator`.
- Reported stable `12.45 N` fingertip force with near-constant mechanical advantage during flexion.
- Purpose: reproducible pulp-pinch movement in a `flaccid finger`.

## T-GRIP 2022 Recall

Source:
[p2022_haarman_tgrip_lateral_pinch.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2022_haarman_tgrip_lateral_pinch.md)

- Thumb exoskeleton for `lateral pinch grasp` in cervical SCI.
- Very lightweight: about `50 g` hand-mounted part.
- `Linear actuator` mounted on the `dorsal side of the hand`.
- Lever-arm / force-transmission mechanism flexes thumb toward the side of the index finger.
- Controlled via `contralateral wrist rotation`.
- Validation on `3 SCI patients`.
- Reported grip force about `7 N`.
- Single-DOF device to support lateral pinch.

## Why These Stay Comparison Papers

- Both are `grasp / opposition` devices, not tapping devices.
- They are useful for:
  - task-specific mechanism design
  - thumb-index geometry
- They are weak matches for:
  - repetitive tapping amplitude/rhythm
  - tapping-specific assistance

## Slide 3. What Finger Tapping Means Clinically

## Primary Paper

Source:
[p2026_zarrat_ehsan_npj_pd_finger_tapping.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)

## Technical Recall

- Video-based assessment framework for PD finger tapping.
- Dataset scale:
  - `446` people with Parkinson's disease
  - `4,073` video recordings
- Task abstraction:
  - repeated thumb-index tapping
  - modeled as a `1D thumb-index distance signal`
  - signal normalized by a `wrist-to-MCP reference distance`
- It does not force a full joint-level biomechanical model.
- It decomposes the task into four clinically interpretable domains:
  - `hypokinesia`
  - `bradykinesia`
  - `sequence effect`
  - `hesitation-halts`

## Why This Matters

- Best current paper for `what the tapping task actually is`.
- Good reminder that direct tapping literature often works at the `task-observable` level, not the anatomical-joint-model level.

## Caveat

- Assessment paper only, not assistive hardware.

## Slide 4. Direct Assessment Technologies

## npj PD 2026 Recall

Source:
[p2026_zarrat_ehsan_npj_pd_finger_tapping.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)

- `Vision-only` assessment.
- Core signal: normalized thumb-index distance over time.
- Strongest contribution: interpretable clinical decomposition, not just ML score prediction.
- Useful outputs:
  - amplitude-related deficit measures
  - speed/cycle-duration measures
  - within-task slope / sequence effect
  - variability/interruption measures

## iTex Gloves 2023 Recall

Source:
[p2023_ravichandran_itex_gloves.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2023_ravichandran_itex_gloves.md)

- `Wearable e-textile glove` system for tele-assessment.
- Pair of gloves + embedded tablet / IoT workflow.
- Sensing:
  - one `6-DoF IMU` per glove
  - `3 flex-sensor channels`
  - ESP32-based wearable electronics
- Thumb sensor was placed between thumb and index because direct thumb placement gave low variation in tapping and closed-grip tasks.
- Finger-tapping signal logic:
  - index flexion used as main task signal
  - activity detection used to isolate actual movement windows
- Feature family includes:
  - frequency measures
  - RMS
  - zero crossings
  - spectral energy bands
  - peak/valley interval statistics
- Classification target was `pre-medication vs post-medication`, not fine-grained tapping deficit decomposition.

## Clean Comparison

- `npj 2026`: best for task definition and clinical interpretability.
- `iTex 2023`: best for wearable deployment and hand-level sensing architecture.

## Caveat

- Both are `assessment`, not assistance.

## Slide 5. I-Phlex As The Closest Hardware Precedent

## I-Phlex 2023 Mechanism Paper Recall

Source:
[p2023_peperoni_self_aligning_mcp.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2023_peperoni_self_aligning_mcp.md)

- Device purpose: mobilization of the `MCP joint` of long fingers.
- Architecture:
  - rigid exoskeleton
  - `remote center of motion`
  - self-aligning `RPR` kinematic chain
- Key novelty:
  - first rotational DOF is spread into a `series of geared hinges`
  - acts as a virtual hinge to reduce dorsal encumbrance during finger flexion
- Final `P-R` section transfers forces more perpendicularly to the phalanx to reduce parasitic loading / shear.
- Actuation:
  - `series elastic actuator (SEA)`
  - compliant human-robot interaction
- Embedded modeling:
  - real-time estimation of `MCP joint angle` and `transferred torque`
- Bench results:
  - angle-estimation RMSE `< 5 degrees`
  - residual MCP torque `< 7 mNm`
  - torque-tracking RMSE `< 8 mNm`
- Preliminary human testing: `8 subjects`

## I-Phlex 2024 Pilot Study Recall

Source:
[p2024_peperoni_iphlex_mcp.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2024_peperoni_iphlex_mcp.md)

- Clinical pilot in post-traumatic hand rehab.
- `6 subjects` with trauma-related right-hand conditions.
- Motion target still `MCP flexion-extension`.
- Device can support `active-assistive` and `passive` mobilization.
- Short-term median changes:
  - `PROM +5.88%`
  - `AROM +11.11%`
- Device ROM measurements were in line with therapist goniometer measurements.
- No major adverse event reported.

## Why It Is The Closest Hardware Match

- Dominant single-joint simplification.
- Repetitive MCP motion is closer to tapping-like motion than pinch posture devices.
- Self-alignment + torque/angle estimation make it stronger technically than a generic rehab glove.

## Caveat

- Still not a Parkinson tapping exoskeleton.
- Orthopaedic/post-traumatic framing, not PD-specific.

## Slide 6. Assistance Vs Stabilization Are Different Design Problems

## Sun 2021 Recall

Source:
[p2021_sun_self_aligning_index_finger.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2021_sun_self_aligning_index_finger.md)

- `Index-finger exoskeleton` for post-stroke rehab.
- `Three motors`.
- Supports:
  - MCP `flexion/extension`
  - MCP `abduction/adduction`
  - finger training with richer kinematics than MCP-only devices
- Uses a `self-aligning spatial mechanism` with passive DOFs for MCP alignment.
- Authors emphasize reduction of reaction forces / improved comfort.
- Reported standardized reaction-force square-sum reduction of `65.8%` versus a state-of-the-art comparison exoskeleton.

## HELM 2025 Recall

Source:
[p2025_andong_helm_tremor.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/papers/p2025_andong_helm_tremor.md)

- Wearable hand exoskeleton for `pathological finger tremor suppression`.
- Actuation:
  - `five miniature linear motors`
  - one per finger
- Modes:
  - `passive mode` for tremor suppression / holding desired positions
  - `active mode` for motion / grasp assistance
- Main body weight about `213 g`
- Validation:
  - `2` healthy subjects with simulated tremor
  - `1` Parkinson's patient with actual finger tremor
- Reported tremor reduction:
  - `>80%` and `>90%` in healthy-subject tests
  - `>70%` in the PD patient
- Important limitation:
  - passive suppression mode is useful for `posture/rest tremor`
  - not a good fit for `kinetic tremor` or rapid voluntary tapping because it resists motion

## Clean Distinction

- `Sun 2021`: help intended motion with richer finger kinematics.
- `HELM 2025`: suppress unintended oscillatory motion.

## Slide 7. Pinch/Grasp Hardware As Comparison Only

## Technical Recall

- `Pulp pinch 2024`:
  - underactuated
  - single-DOF
  - six-bar-like multi-link grasp mechanism
  - built specifically around pulp pinch trajectory
- `T-GRIP 2022`:
  - thumb-specific
  - dorsal linear actuator
  - lever-arm force transmission
  - lateral pinch support

## Why They Matter

- Strong evidence that task-specific mechanism design for thumb-index tasks is feasible.
- Useful for:
  - geometry
  - linkage design logic
  - underactuation ideas

## Why They Stay Secondary

- The target motion is `grasp formation / hold`, not fast repetitive tapping.
- Clinical objective is different.

## Slide 8. What This Means For The Thesis Direction

## Strongest Synthesis

- `Assessment track` defines the task most clearly.
- `I-Phlex / Sun` provide the best near-adjacent mechanism precedents.
- `HELM` shows steadiness is a distinct control problem.

## Broader PD Robotic-Rehab Context

- `AMADEO` PD hand-robot rehab paper exists:
  [Exploring the Impact of Robotic Hand Rehabilitation.pdf](/Users/rami/Downloads/OneDrive_1_3-27-2026/Exploring%20the%20Impact%20of%20Robotic%20Hand%20Rehabilitation.pdf)
- What it is:
  - commercial `end-effector` finger-hand rehab robot
  - hand/forearm on platform
  - wrist secured
  - each finger attached individually to robotic guidance / actuator system
  - passive, active-assisted, and active mobilization
  - programmable control of `ROM`, `speed`, and `force`
  - real-time measurement of strength, ROM, and coordination
- PD RCT context:
  - hand-specific PD rehab beyond pure assessment exists
  - but this is `clinical hand rehabilitation`, not a soft variable-stiffness tapping exoskeleton
- Neuroplasticity nuance:
  - paper discusses neuroplasticity as rationale / possible mechanism
  - it does `not` directly measure neuroplasticity

## Broader PD Meta-Analysis Context

- [Effect of robot-assisted rehabilitation of patients with PD.pdf](/Users/rami/Downloads/OneDrive_1_3-27-2026/Effect%20of%20robot-assisted%20rehabilitation%20of%20patients%20with%20PD.pdf)
- Scale:
  - `22 studies`
  - `819 participants`
- Use this only as broad context.
- Main limitation:
  - dominated by `gait`, `balance`, and mobility outcomes
  - weak direct support for finger-specific hardware decisions

## Clean Thesis Implication

- The simulation-first thesis should stay focused on:
  - simplified finger-actuator interaction
  - variable stiffness
  - controllability / biomechanical interaction
- Current literature suggests the most defensible engineering track is:
  - tapping task defined by assessment papers
  - mechanism ideas informed by near-adjacent MCP / index-finger devices

## Optional Alternate Slide. AMADEO

Use this only if you dedicate a separate slide to it.

## Technical Description

- `End-effector finger-hand rehabilitation robot`, not a soft exoskeleton
- hand and forearm on support platform
- wrist strapped to reduce proximal compensation
- fingers attached individually, magnet-based guidance described in the stroke paper
- passive, active-assisted, and active finger mobilization
- force/ROM measurement built into the device
- visual / game interface for task engagement

## Why It Belongs

- It proves `PD hand robotic rehabilitation` exists beyond assessment.

## Why It Is Not A Core Mechanism Precedent

- commercial rehabilitation platform
- not soft
- not variable stiffness
- not tapping-specific
- paper descriptions are light on deep actuator/transmission architecture

## Slide 9. References

## Main References To Recall

1. `npj PD 2026` for task definition and dataset scale.
2. `iTex 2023` for wearable hand-level assessment architecture.
3. `I-Phlex 2023` for self-aligning MCP mechanism + angle/torque estimation.
4. `I-Phlex 2024` for early clinical use of the MCP device.
5. `Sun 2021` for richer self-aligning index-finger assistance.
6. `HELM 2025` for finger steadiness / tremor suppression.
7. `Pulp pinch 2024` and `T-GRIP 2022` as comparison-only pinch/opposition devices.

## One-Line Limits To Keep Straight

- `npj 2026`: best task-definition paper, not a hardware paper.
- `iTex 2023`: wearable assessment, not assistance.
- `I-Phlex`: closest near-adjacent hardware, not direct PD tapping hardware.
- `Sun 2021`: richer index-finger assistance, not simplified MCP-only.
- `HELM 2025`: steadiness/tremor suppression, not tapping assistance.
- `Pulp pinch` and `T-GRIP`: grasp/opposition devices, not tapping devices.
- `AMADEO`: PD hand robot rehab context, not a soft variable-stiffness precedent.



assistive or contorl devices for parkinsons 
start formulating research questions
assessment POV there might be some gap
Erasmus students 

Bo Biering-Sørensen <bo.biering-soerensen@regionh.dk>

- when writing to the doctor, try proposing to the doctor days eg. Tuesday april 14th

	- emial matteo aobut signing NDA and learning about the device  

