# Predicting the response of a tendon-driven prosthetic finger with hyperelastic joints

## Metadata

- Paper ID: `DOI:10.1016/j.rineng.2025.106979`
- Zotero key: `B96LN626`
- Topic: `T003`
- Status: `shortlist`
- Priority: `high`
- Source: `manual`
- Year: `2025`
- Venue: Results in Engineering
- Authors: Lucas Gallup; Mohamed Trabia; Brendan O'Toole
- DOI: 10.1016/j.rineng.2025.106979
- URL: https://doi.org/10.1016/j.rineng.2025.106979
- PDF status: `attached`
- PDF path: /Users/rami/Zotero/storage/GJTAQXZU/O'Toole - 2025 - Predicting the response of a tendon-driven prosthetic finger with hyperelastic joints.pdf
- Zotero open link: zotero://select/library/items/GJTAQXZU

## Why This Paper Is In The Queue

This is a strong candidate to anchor the first model-class decision.

## Citation / Bibliographic Notes

- Title: Predicting the response of a tendon-driven prosthetic finger with hyperelastic joints
- Authors: Lucas Gallup; Mohamed Trabia; Brendan O'Toole
- Venue: Results in Engineering
- Year: 2025
- DOI: 10.1016/j.rineng.2025.106979
- URL: https://doi.org/10.1016/j.rineng.2025.106979
- Tracker question: What level of finger biomechanical model is sufficient for a first simulation of actuator-finger interaction?

## Abstract / Summary

- This paper develops a quasi-static virtual-work model for a tendon-driven prosthetic finger with three rigid digits connected by hyperelastic TPU joints.
- Each compliant joint is represented as an equivalent `hinge + nonlinear torsional spring`.
- The nonlinear joint law is identified experimentally from moment-angle tests on printed joint specimens.
- The resulting model solves three coupled nonlinear equilibrium equations to predict digit angles from tendon tension.
- Reported overall model error versus experiment is below `5.5%` under the tested quasi-static loading conditions.

## Model / Mechanism / Validation Details

- System type: tendon-driven prosthetic or robotic finger with three rigid digits
- Actuation type: single inextensible tendon under tensile load
- Model type:
  - reduced-order rigid-link model
  - each TPU joint replaced by a hinge plus nonlinear torsional spring
  - kinematics plus quasi-static equilibrium through the principle of virtual work
  - three nonlinear equations solved numerically for the joint angles
- Validation setup:
  - moment-angle characterization of printed proximal and middle or distal TPU joints
  - nine quasi-static finger-flexion experiments under tendon loading
  - marker-based comparison between model-predicted and measured positions
- Main metrics:
  - fitted moment-angle relationship for each joint type
  - equivalent torsional stiffness as derivative of the fitted moment-angle curve
  - geometric prediction error between experiment and model
  - reported maximum overall error below `5.5%`

## What Matters For This Thesis

- This is currently the strongest local paper for justifying a nonlinear quasi-static finger model.
- It shows that the right mechanics upgrade is not to abandon equilibrium, but to preserve the same balance framework while improving the passive constitutive law.
- It also shows that nonlinear joint behavior should ideally be tied to experimentally identified compliance rather than treated as a purely aesthetic curve choice.
- The paper is especially relevant if the thesis wants to move from a constant-torque hello-world MCP model toward a tendon-driven reduced model without jumping directly to full dynamics.

## Limitations

- The nonlinear passive law represents `TPU device joints`, not passive human finger tissues.
- The model is quasi-static and therefore intended for slow motion only.
- Each compliant joint is reduced to a hinge plus torsional spring, so axial deformation and richer distributed compliance are neglected.
- Contact with external objects and gripping forces are not included.

## Decision Impact

- Strong support for keeping the first thesis model quasi-static.
- Strong support for treating a nonlinear passive law as the next realistic upgrade after the linear MCP baseline.
- Suggests that a cubic or other low-order nonlinear passive law is acceptable as a first phenomenological thesis model, but the long-term target should be an experimentally identified constitutive law.

## Quotes / Data To Reuse Later

- Modeling summary from the paper:
  - the model includes gravity loads, joint stiffness, and tendon forces
  - the final system is three nonlinear equations solved simultaneously for the digit angles
- Passive-law identification logic:
  - the moment-angle curve is fit with a second-order polynomial
  - equivalent torsional stiffness is taken as the derivative of that fit
- Limitation to remember:
  - the hinge-plus-torsional-spring representation neglects axial extension effects in the TPU joint

## Mechanistic Insights

- The paper separates the problem cleanly into:
  - equivalent compliant-joint representation
  - kinematic constraints
  - virtual-work balance
  - numerical nonlinear solve
- This is a very reusable template for thesis modeling.
- A key mathematical choice is that the passive law enters through `strain energy` and its derivative, not only through a direct force-balance guess.

## Clean Takeaway

- Gallup 2025 is the strongest current local anchor for the statement that a reduced finger model can remain quasi-static and low order while still using experimentally grounded nonlinear passive joint behavior.

## Next Action

- Use this paper as the primary anchor when refining the first thesis decision on passive torque-angle law selection.
- If needed later, extract the exact virtual-work form and parameter symbols into the notebook notes.
