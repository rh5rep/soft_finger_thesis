# Finger Biomechanics Models

## Question

What level of biomechanical finger model is sufficient for the first simulation of actuator-finger interaction?

## Field Map

Current repo work points to five broad model classes:

- joint-level lumped models with one or a few rotational degrees of freedom
- tendon-driven reduced models where actuator force is mapped into joint torque through geometry
- nonlinear passive-joint models that preserve quasi-static equilibrium but replace constant stiffness with angle-dependent constitutive laws
- kinematic hardware models that focus on self-alignment and interpretable joint variables
- higher-fidelity models such as richer multibody or continuum formulations that are likely too heavy for the first thesis pass

Working status:

- this memo is partly reasoning-driven and should not be treated as a writing-safe literature source until the linked paper notes are audited more fully

## Common Approaches

Common approaches that currently look relevant:

- `1-DOF MCP proxy` with an applied torque and a lumped passive torsional spring
- `multi-DOF reduced finger` with MCP, PIP, and possibly DIP coordinates
- `tendon-driven reduced models` where torque depends on tendon force and moment arm geometry
- `nonlinear passive torque-angle laws` used inside the same quasi-static equilibrium structure
- `hardware-centered kinematic models` that justify an MCP-dominant abstraction through self-alignment and measurable torque-angle variables

The cleanest mechanics statement for the first reduced model is:

- equilibrium is defined by `tau_act(theta, u, p) - tau_passive(theta, p) = 0`
- the main near-term improvement is to upgrade `tau_passive` from a linear to an angle-dependent law

## Tradeoffs

Important tradeoffs:

- a linear passive spring is easy to solve and interpret, but it assumes constant stiffness everywhere
- a nonlinear passive law is slightly harder numerically, but it preserves the same mechanics framework while making the passive behavior more realistic
- an MCP-only abstraction is easier to parameterize and validate, but it will hide coupling effects from PIP and DIP motion
- a tendon-driven actuator model is closer to the eventual device logic, but it adds geometric and parameter-estimation burden earlier
- a higher-fidelity finger model may look more anatomical, but it risks outrunning what can be justified and validated within thesis scope

## What Seems Realistic For This Thesis

The most realistic first modeling baseline is still:

- one effective flexion coordinate
- quasi-static torque balance
- a lumped passive joint law
- a simple actuator abstraction that can later be replaced by a geometry-aware tendon or compliant-drive model

The most defensible immediate upgrade is:

- keep the same equilibrium structure
- replace the linear passive spring with a nonlinear torque-angle law

This fits the thesis brief because it improves realism without forcing a jump to full hand modeling, FEM, or a large control stack.

## Open Gaps

Still unclear:

- which paper or paper cluster should anchor the passive torque-angle law for the first thesis model
- whether the first nonlinear law should be purely phenomenological, such as cubic, or tied more directly to a specific compliant-joint mechanism paper
- how much error is introduced by collapsing the finger to an MCP-dominant proxy for the intended validation tasks
- which outputs should be treated as primary validation targets: angle, torque, effective stiffness, ROM, or a combination
- when the actuator model should stop being a constant applied torque and become configuration-dependent

## Design Implications

Near-term implications for modeling and validation:

- keep the model organized around `kinematics`, `constitutive laws`, and `governing equations` so later extensions do not force a rewrite
- treat numerical equilibrium solving as part of the intended modeling workflow, not as a failure to find a closed form
- interpret local passive slope as both effective stiffness and a stability cue

Practical implication for the notebook track:

- the next useful derivation is a 1-DOF nonlinear equilibrium with a cubic passive law and a clear physical interpretation of every term

## Candidate Next Decision

Which passive torque-angle law is the right first thesis baseline for the 1-DOF quasi-static finger model:

- constant-stiffness linear spring
- cubic phenomenological nonlinear spring
- literature-derived nonlinear law from a specific compliant finger paper
