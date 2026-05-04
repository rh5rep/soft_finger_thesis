# Device And Mechanism Precedents

Use this file for the related-work section that explains what kinds of finger or hand devices already exist and which ones are actually close to the thesis mechanism problem.

## Direct Thesis-Relevant Hardware Precedents

| Paper | Mechanism value | What to cite it for | Recommendation |
| --- | --- | --- | --- |
| `Design and Validation of a Self-Aligning Index Finger Exoskeleton for Post-Stroke Rehabilitation` (Sun et al., 2021) | Self-aligning rigid-link index-finger exoskeleton with kinematic compatibility and kineto-static analysis | Strong direct precedent for finger-joint alignment, interpretable linkage design, and validation logic | `Core cite` |
| `Self-Aligning Finger Exoskeleton for the Mobilization of the Metacarpophalangeal Joint` (Peperoni et al., 2023) | MCP-focused self-aligning exoskeleton with series-elastic architecture and joint-angle/torque estimation | Very strong precedent for simplified MCP-centered actuation and measurable interaction variables | `Core cite` |
| `Post-traumatic hand rehabilitation using a powered metacarpal-phalangeal exoskeleton: a pilot study` (Peperoni et al., 2024) | Powered MCP exoskeleton taken closer to pilot rehabilitation use | Good bridge from benchtop/device design to early validation in people | `Strong supporting cite` |
| `A hand exoskeleton with linear motors (HELM) for pathological tremor suppression of fingers` (Yi et al., 2025) | Finger tremor suppression with a lightweight linear-motor exoskeleton | Best attached paper if the proposal keeps a `steady finger` or suppression angle | `Core cite if stabilization matters` |

## Near-Adjacent But Not Main Precedents

| Paper | Why it is useful | Why it is not the main anchor | Recommendation |
| --- | --- | --- | --- |
| `Design and feasibility of the T-GRIP thumb exoskeleton to support the lateral pinch grasp of spinal cord injury patients` (van der Kooij et al., 2022) | Very clean example of a low-hardware, single-DOF, task-specific thumb device | It is thumb lateral pinch, not tapping-like index/MCP motion | `Comparison cite` |
| `Design and optimization of a custom-made six-bar exoskeleton for pulp pinch grasp rehabilitation in stroke patients` (Roda-Casanova et al., 2024) | Good example of underactuated linkage design, optimization, and custom-fit rehab hardware | It is pinch-rehab specific and mechanically farther from tapping | `Comparison cite` |

## Parkinson-Specific Device Positioning Papers

| Paper | What it contributes | Recommendation |
| --- | --- | --- |
| `Improving Upper Extremity Bradykinesia in Parkinson’s Disease: A Randomized Clinical Trial on the Use of Gravity-Supporting Exoskeletons` (Raciti et al., 2022) | Parkinson-specific exoskeleton rehab positioning, but upper limb rather than isolated finger | `Use for disease positioning, not mechanism design` |
| `Exploring the impact of robotic hand rehabilitation on functional recovery in parkinson’s disease: a randomized controlled trial` (Raciti et al., 2025) | Hand-focused Parkinson robotic rehabilitation context | `Use for disease positioning, not main hardware logic` |

## Best Mechanical Story For The Proposal

If you want the cleanest mechanism story, cite in roughly this order:

1. `Sun 2021` for self-aligning finger exoskeleton design
2. `Peperoni 2023` for MCP-specific self-alignment and torque/angle estimation
3. `Yi 2025` if you need the distinction between assistance and unwanted-motion suppression
4. `Peperoni 2024` for early application/validation relevance
5. `van der Kooij 2022` and `Roda-Casanova 2024` only as comparison devices for task-specific minimal-DOF or underactuated design

## Recommendation For Proposal Writing

Treat `Sun 2021` and `Peperoni 2023` as your main device precedents.

Treat `Yi 2025` as the paper that lets you acknowledge the alternative design objective of `stabilization/suppression`.

Treat pinch papers as useful comparison points, not as the center of the proposal, unless your supervisors want the proposal framed explicitly around pinch.
