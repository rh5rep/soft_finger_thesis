# Modeling And Methods

Use this file for the proposal section that justifies your modeling level, experimental variables, and validation logic.

## Best Papers For Method Justification

| Paper | What method idea it supports | Recommendation |
| --- | --- | --- |
| `Predicting the response of a tendon-driven prosthetic finger with hyperelastic joints` (O'Toole, 2025) | A reduced-order quasi-static, virtual-work-based model can be useful and experimentally defensible without jumping straight to FEM | `Core cite` |
| `Design and Validation of a Self-Aligning Index Finger Exoskeleton for Post-Stroke Rehabilitation` (Sun et al., 2021) | Kinematic compatibility analysis and kineto-static analysis as design tools for finger exoskeletons | `Core cite` |
| `Self-Aligning Finger Exoskeleton for the Mobilization of the Metacarpophalangeal Joint` (Peperoni et al., 2023) | Real-time estimation of joint angle and transferred torque; torque-tracking and residual-torque validation | `Core cite` |
| `Interpretable and granular video-based quantification of motor characteristics from the finger-tapping test in Parkinson’s disease` (Zarrat Ehsan et al., 2026) | Measurable task variables should be interpretable and decomposed, not reduced to one coarse output | `Strong supporting cite` |
| `iTex Gloves: Design and In-Home Evaluation of an E-Textile Glove System for Tele-Assessment of Parkinson’s Disease` (Ravichandran et al., 2023) | Practical sensing and protocol ideas for repeated hand-movement measurements | `Supporting cite` |
| `Computer Vision for Parkinson’s Disease Evaluation: A Survey on Finger Tapping` (Amo-Salas et al., 2024) | Overview of measurement technology families and common assessment logic for finger tapping | `Supporting cite` |

## Method Takeaways You Can Reuse In The Proposal

- A `simple but parameterized model` is defensible if it captures the main joint-actuator relationship and can be validated experimentally.
- `Kinematic compatibility` and `joint alignment` are not side issues; they are part of the device-design method.
- `Torque`, `angle`, `range of motion`, `residual interaction torque`, `tracking performance`, and `repeatability` are better proposal-level variables than vague claims about rehabilitation effectiveness.
- Task variables from Parkinson finger tapping can help choose validation outputs even if the final benchtop system is not a clinical assessment device.

## Suggested Method-Citation Spine

If you need a short method subsection, start with:

1. `O'Toole 2025` for reduced-order modeling
2. `Sun 2021` for kinematic and kineto-static device analysis
3. `Peperoni 2023` for measurable angle/torque estimation and validation
4. `Zarrat Ehsan 2026` for interpretable task-variable selection

## What To Avoid

- Do not cite `Raciti` papers as if they justify your model structure.
- Do not cite `assessment survey` papers as if they are mechanism-design papers.
- Do not let `pinch optimization` papers determine the model unless the proposal explicitly becomes pinch-centered.
