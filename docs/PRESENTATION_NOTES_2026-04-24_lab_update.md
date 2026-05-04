# Presentation Notes: 2026-04-24 Lab Update

## Purpose

Short lab update explaining how the thesis moved from a broad soft finger-actuator concept toward a reduced-order tendon-routing design tool.

## One-Sentence Framing

`I am using a simplified 2D finger-routing model to compare candidate tendon paths by excursion, leverage, and rough tension requirements before deciding whether the prototype needs TSA, variable transmission, or a simpler compliant tendon drive.`

## Slide 1: Thesis Scope

On-slide:
- simplified finger-actuator system
- simulation first
- bench-top mock-up validation
- variable stiffness as the design question

Speaker notes:
- This is not a full glove thesis.
- The aim is to understand actuator-finger interaction in a tractable system.
- The model is a design-screening step before hardware is frozen.

Key takeaway:
- The project is scoped around a reduced-order finger-actuator system that can be simulated and physically tested.

## Slide 2: Why Finger Tapping Is A Useful Lens

On-slide:
- amplitude
- speed
- rhythm
- decrement / sequence effect
- irregularity or halts

Speaker notes:
- Parkinson finger tapping is useful because it turns the clinical motivation into concrete movement features.
- For the current model, the strongest connection is amplitude, excursion, leverage, and tendon tension.
- Rhythm, fatigue, and sequence-effect behavior are important context but not v0 mechanics.

Key takeaway:
- The model should support movement-relevant outputs without making clinical efficacy claims.

## Slide 3: Hardware Idea

On-slide:
- distal thimble / fingertip cap
- soft rings or retainers
- dorsal or lateral routing track
- palmar side kept clear

Speaker notes:
- The physical concept is intentionally lighter than a rigid full-finger cage.
- Rings and retainers are hardware candidates, but the first model uses effective routing points.
- Comfort and palmar clearance are design constraints, not afterthoughts.

Key takeaway:
- The first prototype should preserve routing adjustability so ring count and placement can be tested.

## Slide 4: Modeling Abstraction

On-slide:
- 2D planar index finger
- MCP/PIP/DIP revolute joints
- ordered `RoutingPath`
- `entry`, `guide`, `anchor`
- straight segments between effective points

Speaker notes:
- The important shift is from literal rings to mechanically meaningful routing elements.
- A physical ring, strap, slot, or thimble feature can later map to effective points.
- v0 deliberately excludes friction, wrap, pressure, tendon stretch, and full 3D routing.

Key takeaway:
- The abstraction is simple enough to reason about, but structured enough to compare hardware layouts.

## Slide 5: Current Sanity Checks

On-slide:
- zero angle: straight along `+x`
- negative angles: physiological flexion
- flexion path shortens
- extension path lengthens
- smooth `dL/dq`

Speaker notes:
- The earlier sign-convention confusion is resolved.
- Palmar routing now behaves qualitatively as expected during flexion.
- Dorsal routing behaves in the opposite direction, which is a useful check.
- MCP currently dominates the gradient, which is plausible because proximal rotation moves all downstream elements.

Key takeaway:
- The model is internally coherent as a reduced-order routing model, but it is not yet anatomically validated.

## Slide 6: Useful Outputs

On-slide:
- path length `L(q)`
- excursion `Delta L`
- gradient `partial L / partial q`
- tendon torque per tension

Speaker notes:
- Excursion tells us required actuator stroke.
- The gradient acts like a posture-dependent moment-arm measure.
- With an assumed tendon tension, the model estimates generalized joint torque:

```text
tau_tendon = -T * partial L / partial q
```

Key takeaway:
- The model now connects geometry to actuator sizing.

## Slide 7: From Visualization To Design Screening

On-slide:
- design variables
- output metrics
- constraints
- routing scorecard

Speaker notes:
- The model should not just show that one routing is plausible.
- Candidate routings should be ranked under explicit criteria:
  - ring/routing-element count
  - element placement
  - entry and anchor location
  - excursion demand
  - tension demand
  - smoothness
  - palmar clearance
  - hardware simplicity

Key takeaway:
- A defensible thesis story is `compare alternatives -> choose prototype -> validate mismatch`.

## Slide 8: TSA And Variable Stiffness

On-slide:
- TSA is a candidate, not an assumption
- TSA is not variable stiffness by itself
- CVT/CTA only if tradeoff is needed
- route first, actuator second

Speaker notes:
- TSA may be compact and useful, but it should be selected after stroke and tension requirements are known.
- Variable transmission only matters if posture-dependent speed/stroke/torque tradeoffs show up as real requirements.
- A simpler series-stiffness tendon drive may be enough for the first validation mock-up.

Key takeaway:
- The current model gives the information needed to decide whether more complex actuation is justified.

## Slide 9: Next Steps

On-slide:
- compare routing variants
- add passive joint torque
- estimate tension requirements
- choose bench-top mock-up layout
- validate with marker/tension measurements

Speaker notes:
- Immediate next step is a routing scorecard.
- Then add passive stiffness and quasi-static equilibrium.
- The prototype should test the same outputs the model predicts: posture, excursion, tension, and repeatability.

Key takeaway:
- The next milestone is turning the current v0 model into a small routing comparison study.

## Discussion Questions

- Which routing outputs would be most convincing for the lab: excursion, tension, joint torque distribution, or fingertip trajectory?
- Is the lab more interested in a soft variable-stiffness actuator identity, or in a clean tendon-routing validation first?
- What fabrication method is most realistic for removable soft rings and a distal thimble?
- What tendon or cord load range should be assumed for the first bench-top sizing pass?

## Source And Repo Anchors

- Scope: [THESIS_BRIEF.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/THESIS_BRIEF.md)
- Current project context: [STUDY_GUIDE.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/STUDY_GUIDE.md)
- Progress narrative: [THESIS_PROGRESS.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/THESIS_PROGRESS.md)
- Routing memo: [11_tendon_routing_and_ring_placement.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/TOPIC_MEMOS/11_tendon_routing_and_ring_placement.md)
- Variable-stiffness memo: [10_variable_stiffness_design_concepts.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/TOPIC_MEMOS/10_variable_stiffness_design_concepts.md)
- Code: [v0_model.py](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/simulation_modeling/v0_model.py)
