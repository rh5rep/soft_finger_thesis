# Device Comparison Crib Sheet 2026-03-27

Use this as a one-page hardware comparison sheet.

## Core Comparison

| Device / paper | Task target | Architecture / actuation | Strongest technical point | Main limitation for this thesis |
| --- | --- | --- | --- | --- |
| `I-Phlex 2023` | MCP flexion-extension rehab | Rigid MCP exoskeleton, self-aligning `RPR` chain, geared virtual hinge, `SEA` | Joint-level `angle/torque` estimation with low residual torque and good tracking | Not PD-specific, not tapping-specific, not variable-stiffness |
| `I-Phlex 2024` | Post-traumatic MCP rehab | Same platform in pilot clinical use; passive + active-assistive | Shows MCP simplification can be clinically deployable and measured against goniometer | Small pilot, orthopaedic context, not PD |
| `Sun 2021` | Richer index-finger rehab | `3 motors`; MCP `f/e`, MCP `a/a`, PIP `f/e`; self-aligning spatial mechanism | Strong treatment of `self-alignment` and reaction-force reduction for richer kinematics | More complex than a first simplified thesis model |
| `HELM 2025` | Finger tremor suppression / steadiness | Five-finger exoskeleton, `5 linear motors`, passive suppression + active assist modes | Clearest hardware precedent for `steady finger` / tremor suppression | Solves steadiness, not tapping assistance; tiny validation |
| `Pulp pinch 2024` | Pulp pinch grasp rehab | Underactuated single-DOF, eight-link pinch mechanism, small linear actuator | Strong example of `task-specific mechanism synthesis` for pinch | Grasp posture, not repetitive tapping |
| `T-GRIP 2022` | Lateral pinch grasp assist | Thumb-only, dorsal micro linear actuator, lever arm, one DOF | Minimal hardware can restore a useful thumb-index grasp | SCI grasp device, not tapping device |

## Quick Numbers

- `I-Phlex 2023`: angle RMSE `< 5 deg`, residual torque `< 7 mNm`, torque-tracking `< 8 mNm`
- `I-Phlex 2024`: `PROM +5.88%`, `AROM +11.11%`, `6` subjects
- `Sun 2021`: reaction-force square-sum reduction `65.8%`
- `HELM 2025`: tremor reduction `>70%` in `1` PD patient
- `Pulp pinch 2024`: fingertip force about `12.45 N`
- `T-GRIP 2022`: device weight about `50 g`, grip force about `7 N`, `3` SCI patients

## What Actually Motivates The Thesis

## 1. Why a simplified first model is defensible

- `I-Phlex 2023/2024` is the strongest argument that a `dominant MCP abstraction` is not arbitrary.
- The device is mechanically credible, measurable, and clinically legible.
- This supports your thesis starting with:
  - one main finger DOF
  - explicit torque/angle variables
  - interpretable actuation-finger interaction

## 2. Why self-alignment should stay visible

- `I-Phlex` and `Sun 2021` both treat `self-alignment` as central, not optional.
- That means even a simplified thesis model should keep alignment / compatibility in mind conceptually.
- Future work implication:
  - if the mock-up later becomes wearable, alignment and parasitic loads will matter immediately

## 3. Why tapping is not the same as pinch

- `Pulp pinch` and `T-GRIP` show that thumb-index tasks can have highly optimized mechanisms.
- But those mechanisms are optimized for `grasp formation / hold`, not `rapid rhythmic tapping`.
- Thesis implication:
  - pinch papers are useful for comparison and inspiration
  - they should not define the core task abstraction

## 4. Why steadiness may need a separate branch

- `HELM 2025` shows that `steady finger` and `assist motion` are not the same problem.
- Its passive suppression mode is fundamentally different from a device meant to enable rapid voluntary movement.
- Thesis implication:
  - if supervisors want both movement support and steadiness, those may need to be treated as separate design roles
  - future work could compare assistance and stabilization as distinct controller / device families

## 5. Why richer kinematics remain relevant

- `Sun 2021` is your best reminder that a single MCP hinge is a simplification, not the whole story.
- It preserves MCP `a/a` and PIP motion and still treats comfort / alignment carefully.
- Thesis implication:
  - first model can stay simple
  - future work can add richer finger kinematics once the reduced-order baseline is stable

## Suggested Thesis Narrative

- `Assessment papers` define the tapping task.
- `I-Phlex` motivates the simplest credible hardware abstraction.
- `Sun 2021` marks the next level of kinematic richness if needed.
- `HELM` keeps steadiness as a distinct comparison track.
- `Pulp pinch` and `T-GRIP` stay as comparison mechanisms showing how mature thumb-index grasp hardware already is.

## Best Current Engineering Direction

If you need one clean line:

`The literature best supports starting with a simplified, MCP-dominant, self-aligned finger-assistance model, while keeping richer index-finger kinematics, steadiness control, and pinch-specific mechanisms as explicit future comparison tracks.`
