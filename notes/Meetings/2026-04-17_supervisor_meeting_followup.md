# Supervisor Meeting Follow-Up 2026-04-17

## Core Takeaway

The next step is not to lock the final prototype immediately. The first priority is to clarify what movement or use case the design is meant to support, then compare simple design options against feasibility and accessibility before choosing the first build direction.

## Meeting Notes

### 1. Movement Target Needs Sharpening

- Moving one finger is not the same as moving all the joints in a useful way.
- A design can move the finger globally without producing the desired MCP/PIP/DIP coordination.
- Once a design branch exists, the target movement should be stated explicitly:
  - which joints should move
  - which joints may be constrained
  - whether the goal is tapping, grasping, stabilization, assessment, or another use case
- The "9 ball game" was mentioned as a possible analogy or example to revisit.

### 2. Keep The Design Screening Simple

Silvia's guidance was to keep the comparison as simple as possible at first.

Recommended screening table:

| Dimension | Purpose |
|---|---|
| `Accessibility` | Who could use or tolerate the design? Which patients or use cases does it fit? |
| `Feasibility` | Can it realistically be modeled, fabricated, and tested within the thesis timeline? |
| `Design branch` | Which mechanism concept follows from the comparison? |
| `Use case` | What patient group or task would this design plausibly support? |

The output should be a design choice plus a small set of proposed use cases, not an open-ended device concept.

### 3. Use Designs To Ask Better Clinical Questions

- Once there is a concrete design, show it to relevant people and ask what they think.
- A design may help one patient group but not another.
- Different designs may correspond to different patient needs:
  - one design may help one group of patients
  - another design may help a different group
- This supports using clinical input after a design concept exists, instead of asking broad abstract questions too early.

### 4. OpenSim And Parallel Student Work

- If considering OpenSim, coordinate with `Samuela`, who is working on that.
- `Phillip` is working on actuator design and CAD.
- Their work should be treated as useful context and possible collaboration input, not as something to duplicate blindly.

## Action Items

1. Build a concise design-screening table with `accessibility`, `feasibility`, `design branch`, and `use case`.
2. Define the target movement for each candidate design branch before evaluating it.
3. Decide whether OpenSim is useful enough to involve now, and if so, coordinate with Samuela.
4. Coordinate with Phillip on actuator design and CAD context.
5. Compile a briefing list for the Erasmus students.

## Erasmus Student Briefing List

Purpose: prepare Erasmus students joining or helping from `May` to `July` so they understand the thesis context and where their work fits.

Briefing should cover:

- thesis scope and current project framing
- what the simplified finger-actuator system is trying to study
- what is already known from the Bo and Silvia meetings
- current design branches under discussion
- current simulation status and limitations
- what Phillip is doing on actuator design/CAD
- whether Samuela's OpenSim work is relevant
- expected contribution window from May to July
- practical collaboration context with the colleagues
- what decisions are still open and what should not be assumed fixed

## Open Questions

- What exact movement should the first design target: one-finger flexion, coordinated MCP/PIP/DIP tapping, stabilization, or another task?
- Should the next supervisor update show a design-screening table before any detailed CAD?
- Which patient groups are most relevant for each design branch?
- Is OpenSim needed for this thesis stage, or is the current reduced-order model enough for first design screening?
