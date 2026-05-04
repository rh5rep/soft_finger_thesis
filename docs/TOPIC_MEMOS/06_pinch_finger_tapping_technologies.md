# Finger Tapping and Adjacent Finger-Motion Technologies

## Question

Which current hand and finger exoskeleton technologies are most relevant to finger tapping or tapping-like repetitive finger motion, and how do they work?

This memo should compare all relevant technology families, not only soft robotics.

## Field Map

Use this memo to separate the literature into four buckets:

- direct finger-tapping devices or systems
- near-adjacent index-finger or MCP flexion-extension exoskeletons
- tremor suppression or movement-stabilization devices
- Parkinson finger-tapping assessment systems
- far-adjacent pinch/opposition devices
- background reviews and task-framing papers that help classify the technology space

Within each bucket, note whether the device is:

- soft
- rigid-link
- tendon/cable-driven
- linkage-based
- hybrid

## Common Approaches

- Direct finger-tapping assistive/exoskeleton devices appear sparse.
- Across the literature surface reviewed so far, Parkinson finger tapping is treated much more often as an `assessment task` than as an `assistive movement target`.
- The stronger near-adjacent hardware literature centers on index-finger exoskeletons, MCP mobilization devices, and repetitive flexion-extension mechanisms.
- A separate but relevant hardware bucket exists for tremor suppression or finger stabilization, which is closer to "keeping the finger steady" than the MCP mobilization papers.
- A strong assessment bucket exists for Parkinson finger tapping, including phone apps, wearable gloves, sensor systems, and computer-vision pipelines.
- Assessment and task-definition papers are much easier to find than direct tapping-assist devices.
- Pinch/opposition devices are well represented but are mechanically and functionally different from tapping-oriented motion.

## Tradeoffs

- MCP-centered rehabilitation devices are closer to a simplified repetitive-motion proxy, but they do not address tremor or steadiness directly.
- Tremor-suppression devices address steadiness directly, but they may resist voluntary motion and therefore are not automatically relevant to tapping assistance.
- Assessment systems define the direct task much better than the exoskeleton papers, but they do not solve the assistance or stabilization problem.
- Broader index-finger exoskeletons preserve richer kinematics, but they are mechanically more complex and may be harder to justify as simplified task-specific precedents.

## What Seems Realistic For This Thesis

- A tapping-oriented or tapping-like simplified system may need to be framed through dominant index-finger or MCP motion rather than through pinch posture.
- Near-adjacent index-finger and MCP exoskeletons currently look more relevant than pinch devices for informing mechanism ideas.
- If the supervisors' wording about keeping the finger steady remains important, then tremor-suppression devices should be reviewed as a separate category rather than being forced into the tapping bucket.
- If the supervisors care about Parkinson finger tapping specifically, then a compact assessment-track subsection is necessary because that is where the direct task literature is strongest.
- Pinch/opposition devices remain useful only as comparison points or as examples of movement-specific design.

## Open Gaps

- Direct exoskeletons designed explicitly around the finger-tapping task appear limited.
- No strong direct category of `Parkinson finger-tapping exoskeleton` papers has emerged from the current search.
- It is still unclear whether the review should present finger tapping as the main device category or as a task whose closest hardware precedents are repetitive finger-motion devices.
- More evidence is needed on whether single-DOF dominant-MCP simplifications are common in device design for tapping-like tasks.
- It is also unclear whether the supervisor's "steady finger" framing is better addressed through tremor-suppression literature than through tapping literature.
- The review still needs a clear decision on how much space the direct Parkinson assessment literature should get relative to the exoskeleton hardware literature.

## Design Implications

- The review should prioritize repeated index-finger and MCP motion devices over pinch devices.
- A movement-specific review should distinguish direct evidence from near-adjacent and far-adjacent evidence rather than treating all thumb-index tasks as equivalent.
- A careful review should also distinguish `assist motion` from `suppress unwanted motion`, because those goals may lead to different device families and control strategies.
- It should also distinguish `assist/stabilize hardware` from `task measurement systems`, because the latter are currently the clearest direct literature for Parkinson finger tapping.
- If the target task remains finger tapping, then assessment literature may define the motion while exoskeleton literature supplies only approximate mechanical precedents.
- The lack of a direct Parkinson tapping-assist paper should be presented as a literature result, not as a failure of the review.

## Assessment Synthesis

- The strongest direct literature for Parkinson finger tapping currently sits on the assessment side rather than the assistive-hardware side.
- `npj PD 2026` is the clearest paper for understanding the task itself: repeated thumb-index tapping can be reduced to a task-level signal and decomposed into multiple clinically meaningful deficit families.
- `iTex Gloves 2023` is the clearest paper for understanding wearable deployment: finger tapping can be captured with glove-based sensing, task segmentation, and engineered features in home-use conditions.
- These papers complement each other rather than duplicate each other:
  - `npj PD 2026`: what the task means and what deficits matter
  - `iTex Gloves 2023`: what a wearable system for collecting the task can look like

## Candidate Next Decision

- Should the thesis review center on `finger tapping` directly, on `tapping-like repetitive index-finger / MCP motion`, or split the review into `movement assistance`, `movement stabilization`, and `assessment` categories?

## Reserve / Non-Core Leads

These may be useful to keep documented, but they should not drive the main presentation narrative unless a supervisor asks for them:

- distal finger tapping web-based tests
- dysrhythmia-focused tapping assessment papers
- digitography / ReTap-style tapping references
- additional wearable tremor-suppression papers beyond HELM
- pinch/opposition papers already screened and classified as far-adjacent

## Seed Papers To Screen First

- `Design and Validation of a Self-Aligning Index Finger Exoskeleton for Post-Stroke Rehabilitation` (IEEE TNSRE 2021, DOI: `10.1109/TNSRE.2021.3097888`)
- `Self-Aligning Finger Exoskeleton for the Mobilization of the Metacarpophalangeal Joint` (IEEE TNSRE 2023, DOI: `10.1109/TNSRE.2023.3236070`)
- `Post-traumatic hand rehabilitation using a powered metacarpal-phalangeal exoskeleton: a pilot study` (JNER 2024, DOI: `10.1186/s12984-024-01511-w`)
- `A hand exoskeleton with linear motors (HELM) for pathological tremor suppression of fingers` (Intelligent Sports and Health 2025, DOI: `10.1016/j.ish.2025.03.002`)
- `Vision-Based Finger Tapping Test in Patients With Parkinson's Disease via Spatial-Temporal 3D Hand Pose Estimation` (IEEE JBHI 2022, DOI: `10.1109/JBHI.2022.3162386`) as a task-definition paper rather than a technology anchor
- `Interpretable and granular video-based quantification of motor characteristics from the finger-tapping test in Parkinson’s disease` (npj Parkinson's Disease 2026, DOI: `10.1038/s41531-026-01307-w`)
- `Computer Vision for Parkinson's Disease Evaluation: A Survey on Finger Tapping` (Healthcare 2024, DOI: `10.3390/healthcare12040439`)
- `iTex Gloves: Design and In-Home Evaluation of an E-Textile Glove System for Tele-Assessment of Parkinson's Disease` (Sensors 2023, DOI: `10.3390/s23062877`)
- `Objective assessment of bradykinesia in Parkinson's disease using evolutionary algorithms: clinical validation` (Translational Neurodegeneration 2018, DOI: `10.1186/s40035-018-0124-x`)
- `A Validation Study of a Smartphone-Based Finger Tapping Application for Quantitative Assessment of Bradykinesia in Parkinson's Disease` (PLOS ONE 2016, DOI: `10.1371/journal.pone.0158852`)
- `Design and Optimization of a Custom-Made Six-Bar Exoskeleton for Pulp Pinch Grasp Rehabilitation in Stroke Patients` (Biomimetics 2024, DOI: `10.3390/biomimetics9100616`)
- `Design and feasibility of the T-GRIP thumb exoskeleton to support the lateral pinch grasp of spinal cord injury patients` (ICORR 2022, DOI: `10.1109/ICORR55369.2022.9896595`)
- `Soft Hand Exoskeletons for Rehabilitation: Approaches to Design, Manufacturing Methods, and Future Prospects` (Robotics 2024, DOI: `10.3390/robotics13030050`)

## Review Angle

The next review should likely answer:

1. Do direct finger-tapping devices exist, or is the literature mainly near-adjacent?
2. Which index-finger or MCP exoskeletons are closest to tapping-like repetitive motion?
3. Which papers are only far-adjacent pinch/opposition comparisons?
4. What mechanism family is used in each bucket?
5. What measurements or outcomes are reported?
