## What I would show today

Main presentation packet:

- [PRESENTATION_NOTES_2026-04-24_lab_update.md](../../docs/PRESENTATION_NOTES_2026-04-24_lab_update.md)

### Slide 1 — Problem / concept

- finger assistance / tapping
- soft ring-based routing concept
- why reduced-order modeling is needed

### Slide 2 — 3D concept animation

Show:

- finger through ring
- routing on top/bottom
- radial/ulnar slot idea
- flexion/extension path intuition

Goal:  
**make the mechanism understandable**

### Slide 3 — 2D effective model

Show:

- phalanges
- joints
- effective guide points / anchor
- flexor and extensor paths

Goal:  
**show the abstraction**

### Slide 4 — Preliminary outputs

Best plots:

- tendon length L(q)L(q)L(q)
- excursion ΔL(q)\Delta L(q)ΔL(q)
- maybe dL/dqdL/dqdL/dq or effective moment arm
- maybe flexor vs extensor comparison

Goal:  
**show that the model already produces useful quantities**

### Slide 5 — Torque estimate

Only if simple and defensible.

Something like:

τtendon=−T∂L∂q\tau_{tendon} = -T \frac{\partial L}{\partial q}τtendon​=−T∂q∂L​

Then say:

- with an assumed required joint torque range,
- this implies a rough tendon tension requirement,
- which helps evaluate actuator options like TSA.

Goal:  
**link mechanics to actuation**

### Slide 6 — TSA / variable stiffness implication

Present this as:

- a candidate actuation architecture
- not yet fully modeled
- potentially useful for force density / compactness / transmission adaptability
- but not an assumption for v0 before routing stroke and tension requirements are known
