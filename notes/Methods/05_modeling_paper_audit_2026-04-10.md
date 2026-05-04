# Modeling Paper Audit 2026-04-10

## Purpose

Compare the current reduced-order modeling notes against the strongest full-text modeling papers currently attached in the vault, then identify:

- what already aligns well
- what the papers add mathematically
- what still needs a thesis decision

This note is a `working audit`, not a writing-safe literature synthesis.

## Scope

### Audited Full-Text Papers

- `p2025_gallup_tendonhyperelasticfinger.md`
- `p2023_peperoni_self_aligning_mcp.md`
- `p2021_sun_self_aligning_index_finger.md`
- `p2010_schabowsky_hexorr_hand_exoskeleton.md`

### Current Repo Notes Compared

- [04_quasi_static_finger_modeling.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/Methods/04_quasi_static_finger_modeling.md)
- [03_finger_biomechanics_models.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/TOPIC_MEMOS/03_finger_biomechanics_models.md)

### Important Missing PDFs

The current attached full-text set is still missing some of the most thesis-relevant modeling or actuator papers:

- `p2024_zhou_tendondrivenfinger.md`
- `p2024_li_tvsafinger.md`
- `p2024_tabrizi_hapticvsa.md`
- `p2024_mccall_softpneumaticextension.md`
- `p2025_besharati_aansoftfinger.md`

That means the current audit is strongest on:

- nonlinear quasi-static finger equilibrium
- self-alignment kinematics
- kineto-static torque transfer
- rehabilitation-oriented validation metrics

It is weaker on:

- variable-stiffness mechanism math
- soft pneumatic actuator modeling
- assist-as-needed control for soft finger devices

## High-Level Verdict

The current thesis notes are directionally right.

The strongest alignment is that the notes already preserve the correct modeling skeleton:

- define generalized coordinates
- define actuator and passive contributions separately
- write equilibrium or kineto-static balance
- accept numerical solving when needed

What the papers add is not a different philosophy. They add the concrete mathematical habits that make the model defensible:

- identify constitutive laws experimentally when possible
- keep quasi-static assumptions explicit
- separate kinematics from statics
- validate angle, torque, and parasitic force metrics rather than only plotting trajectories

## What The Papers Say Mathematically

## 1. Gallup 2025

### Main Mathematical Contribution

This is the clearest local anchor for the nonlinear equilibrium idea.

Core structure:

- three rigid digits
- flexible TPU joints replaced by `hinge + nonlinear torsional spring`
- tendon tension as the input
- quasi-static balance solved through the `principle of virtual work`

The paper explicitly decomposes the model into:

1. equivalent model development
2. finger kinematics
3. quasi-static analysis
4. numerical solution of flexion

That decomposition matches the current methods note well.

### Important Mathematical Properties

- The governing equations are derived from virtual work, not from an ad hoc curve fit.
- Gravity, tendon work, and joint strain energy all appear in the balance.
- The final system is `three nonlinear equations` in the digit angles.
- The solution is obtained numerically.

### Passive Law Decision

The most useful detail is how they obtain the passive law.

They do not simply assume a nonlinear spring because it looks plausible. They:

- measure moment versus angular deflection experimentally
- fit a second-order polynomial moment-angle curve
- define equivalent torsional stiffness as the derivative of that curve

That is a very important thesis lesson:

`nonlinear stiffness should ideally come from a measured constitutive relation, not only from aesthetic preference`

### What This Changes In Your Thinking

Your current cubic-law idea is still valid as a first thesis move.

But Gallup sharpens the interpretation:

- the nonlinear law is really a surrogate for experimentally identified compliance
- the numerical solve is the normal outcome once tendon geometry and nonlinear compliance are included
- the key abstraction is not "biological finger" versus "robot finger"
  it is `rigid links + compliant joints + tendon input + quasi-static balance`

### Limits Of The Paper

It does not directly model passive human MCP tissues.

Its nonlinear passive law describes `TPU device joints`, not anatomy.

So it is a strong math anchor, but not a direct source for human passive-joint parameters.

## 2. Peperoni 2023

### Main Mathematical Contribution

This paper is less about passive tissue modeling and more about the correct reduced-order architecture for a rehab-facing MCP exoskeleton.

Core structure:

- one effective MCP flexion DOF
- closed kinematic chain between finger and exoskeleton
- direct kinematic model for angle estimation
- inverse kineto-static model for torque mapping
- impedance-based assistance layered on top

### Important Mathematical Properties

The key kineto-static equation comes from virtual work:

- SEA torque input
- return spring contribution
- MCP torque output

This gives a joint-level torque estimate from actuator-side variables.

That is exactly the kind of model progression your notes call `geometry-aware actuator model`.

### Control And Interaction Logic

This paper is especially useful because it converts mechanics into clinically meaningful control quantities:

- estimated MCP angle
- estimated MCP torque
- virtual stiffness `K_v`
- zero-torque mode as a low-impedance transparency condition

The impedance law is simple and thesis-friendly:

`tau_des = K_v (theta_des - theta_est)`

This is a strong reminder that `controllability` in your thesis should not remain vague. Papers like this operationalize it through:

- torque tracking
- residual torque
- output impedance
- motion-tracking error

### What This Changes In Your Thinking

Your current methods note is correct that the next improvement after a passive law upgrade is a more geometry-aware actuator model.

Peperoni gives the concrete form that such a step can take:

- keep one DOF
- preserve quasi-static assumptions
- estimate actuator-to-joint torque through kineto-statics
- add an interpretable impedance parameter instead of jumping straight to complex control

### Limits Of The Paper

- quasi-static validity is explicit and limited
- it is hardware-centered, not a model of passive finger tissue
- it is strongest on `interaction variables`, not on biological constitutive laws

## 3. Sun 2021

### Main Mathematical Contribution

This paper is the clearest local anchor for when a richer than 1-DOF model is justified.

Core structure:

- MCP has flexion-extension and abduction-adduction
- misalignment is modeled as `three translational offsets`
- the exoskeleton-finger system is represented as a closed spatial mechanism
- kinematic compatibility is derived explicitly
- kineto-statics is handled through the Jacobian and virtual work

### Important Mathematical Properties

The paper gives a strong modeling habit:

`separate kinematic compatibility from force transmission`

They first prove the mechanism can absorb misalignment through coordinate transforms and closed-chain constraints.

Then they differentiate to get the Jacobian and use:

`tau_q = J(q)^T tau_Gamma`

for kineto-static mapping.

This is mathematically important because it shows the next level after simple scalar torque balance:

- first write the geometry correctly
- then map generalized forces through the Jacobian

### Performance Metrics That Matter

This paper is unusually good on formal comfort metrics.

It defines:

- `SRFSS`: standardized reaction forces square sum
- `AFFP`: absolute force along the finger phalanx

That matters because it shows that a good finger-assistance model is not only about reaching the target angle. It is also about minimizing parasitic forces.

### What This Changes In Your Thinking

Sun does not say your first model must be multi-DOF.

What it does say is:

- if `self-alignment`, `wearability`, or `parasitic loads` become central thesis questions, then a pure 1-DOF scalar model will eventually be too small
- if the thesis stays focused on first actuator-finger interaction and bench-top validation, a 1-DOF model is still defensible as a first stage

### Limits Of The Paper

- ideal reaction-force cancellation depends on assumptions like frictionless behavior or equal transmitted torques
- the model is richer and harder than what you need first
- it is mainly a mechanism-compatibility paper, not a passive tissue law paper

## 4. HEXORR 2010

### Main Mathematical Contribution

This is more of a system-design and control-compensation precedent than a direct model anchor.

Useful points:

- aligned exoskeleton joints with anatomical joints
- mechanical advantage analysis across ROM
- explicit gravity and friction compensation
- torque and ROM as core validation variables

### What It Adds

It reinforces that even if the underlying biomechanical model is simple, practical devices still need:

- configuration-dependent actuation behavior
- compensation for internal device loads
- validation through ROM and torque, not only geometry

### Limit

It is weaker than Gallup, Peperoni, and Sun as a direct mathematical model template for your first notebook.

## Alignment With Current Notes

## Where The Current Notes Already Align Well

### 1. Equilibrium As The Central Object

Your note treats the core object as:

`tau_act(theta, u, p) - tau_passive(theta, p) = 0`

That is the right abstraction.

Gallup confirms this strongly, even though it writes the balance through virtual work instead of the simpler scalar equation.

### 2. Nonlinear Passive Law As A Constitutive Upgrade

Your current note says the framework stays the same and only the passive law changes.

That is correct.

Gallup is the best direct support for that claim.

### 3. Numerical Solving As A Normal Step

Your note explicitly treats nonlinear solving as a feature.

That aligns very well with Gallup and also with the broader kineto-static logic in Sun and Peperoni.

### 4. Kinematics / Constitutive Law / Governing Equation Split

This is one of the strongest features of your current note.

All three main papers effectively follow this split even when they do not state it in those exact words.

### 5. Geometry-Aware Actuator Model As The Next Upgrade

Your current modeling ladder says the next upgrade after a passive law improvement is:

`tau_act(theta, u) - f(theta - theta_0) = 0`

Peperoni strongly supports that progression.

## Where The Current Notes Need More Thought

## 1. Human Passive Tissue Versus Device Compliance

This is the biggest conceptual gap.

Right now your notes sometimes read as if one passive law can cover both:

- passive finger tissues
- compliant actuator or exoskeleton joints

The papers suggest these should be kept distinct.

Gallup models compliant `device joints`.
Your thesis likely wants at least one passive law for the `finger side`.

That means you should decide whether the reduced model is:

- a human finger model with passive tissue resistance
- a device model with compliant joints
- or a coupled human-device model with both

## 2. Why Choose Cubic Specifically

The cubic law is still a good first choice, but right now the note presents it mostly as a convenient nonlinear shape.

The papers suggest a stronger justification:

- use cubic first because it is the simplest low-order law that gives angle-dependent stiffness
- but treat it as a `phenomenological surrogate`
- and plan to replace it with a measured law once data exists

That makes the choice mathematically cleaner.

## 3. Stability Is Theoretically Good But Not Yet Paper-Anchored

Your note’s local stability discussion is mathematically sound.

But the currently audited papers do not make stability a central explicit topic in the same scalar way. They are more focused on:

- equilibrium existence
- quasi-static validity
- parasitic force minimization
- torque transfer

So keep the stability section, but recognize that it currently comes more from general mechanics theory than from these specific papers.

## 4. Validation Targets Need To Be Broader Than Angle Alone

The papers strongly suggest that a good thesis model should be evaluated against more than angle prediction.

Useful candidate outputs:

- joint angle
- joint torque
- effective stiffness
- residual torque in transparency mode
- output impedance
- parasitic reaction forces or shear force
- ROM coverage

Your current note hints at this, but the audit makes it much sharper.

## 5. Quasi-Static Needs A Concrete Domain Of Validity

All of the most relevant papers rely on low-speed or quasi-static assumptions somewhere.

So the thesis model should state explicitly:

- what motion-speed regime is intended
- what inertial or viscous effects are ignored
- what failure mode would trigger a move to dynamics

## Best Mathematical Lessons To Keep

## 1. Virtual Work Is Extremely Useful

It is the cleanest bridge between:

- geometry
- actuator effort
- spring or passive energy
- joint torque

You do not need to build the whole thesis around virtual work notation, but you should understand it well because both Gallup and Peperoni lean on it heavily.

## 2. Derivatives Give Physical Meaning

These derivatives are especially important:

- `d tau_passive / d theta`
  effective stiffness
- `d theta / d u`
  input sensitivity or controllability in a local sense
- Jacobian terms
  mapping between actuator space and joint space

If you understand those well, a lot of the thesis becomes more transparent.

## 3. Good Reduced Models Are Honest About What They Lump

The papers do not pretend to model everything.

They lump aggressively, but they say what is lumped:

- hinge plus torsional spring
- one effective MCP degree of freedom
- passive offsets treated as calibration parameters
- low-speed quasi-static approximation

That is the standard you want.

## 4. Good Models Are Paired With Measurable Variables

A strong rehab-oriented model is not just elegant.

It should connect to quantities you can actually estimate or measure:

- angle
- torque
- force
- stiffness
- ROM
- parasitic load

## Working Thesis Decisions Suggested By This Audit

## Decision 1

The first reduced-order thesis model should stay `1-DOF` and `quasi-static`.

Reason:

- Gallup and Peperoni both show that serious, useful modeling can happen in that regime
- it fits your current notebook and bench-top ambitions

## Decision 2

The passive law should be treated as a `phenomenological constitutive law` first, not yet as an anatomically exact tissue model.

Reason:

- that is mathematically honest
- it keeps the first model tractable
- it creates a clean path for later parameter identification

## Decision 3

The next model upgrade after the passive law should be a `geometry-aware actuator torque mapping`, not an immediate jump to multi-DOF anatomy.

Reason:

- Peperoni shows that this is where controllability and interaction start becoming concrete

## Decision 4

Validation planning should include at least one interaction metric beyond angle.

Candidate choices:

- torque prediction
- residual torque or transparency
- effective stiffness
- parasitic force proxy

## Immediate Next Questions

1. Is the first passive law meant to represent the `human finger`, the `device`, or the `combined finger-device system`?
2. Should the first nonlinear law be a cubic surrogate or a measured polynomial fit anchored to available experiments or literature?
3. Which validation outputs matter most for the thesis claim:
   angle only, angle plus torque, or angle plus torque plus impedance-like behavior?
4. At what point would self-alignment or parasitic-force considerations justify moving beyond the 1-DOF MCP proxy?

## Concrete Next Step

The next useful notebook derivation is still:

1. write the 1-DOF equilibrium explicitly
2. define the passive law as linear and cubic variants
3. compute `k_eff(theta)`
4. add a simple geometry-aware actuator torque term
5. inspect local sensitivity and equilibrium branches

After that, the next paper gap to fill is not another broad review.

It is one of the missing full-text actuator or variable-stiffness papers.
