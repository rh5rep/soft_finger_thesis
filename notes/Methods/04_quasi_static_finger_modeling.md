# Quasi-Static Finger Modeling Foundations

## Purpose

Preserve the core mechanics reasoning behind the first reduced-order finger model before it gets buried in notebook cells or chat history.

This note is a `methods foundation`, not a writing-safe literature note.

## Status

- Type: working synthesis
- Safe to reuse as: modeling rationale, notebook guidance, decision prep
- Not safe to reuse as: a literature claim unless the statement is backed by a paper note in `notes/papers/`

## Core Modeling Idea

The important object is not a plotting formula. It is a torque-balance model:

`tau_net(theta) = tau_act(theta, u, p) - tau_passive(theta, p)`

Equilibrium is defined by:

`tau_net(theta) = 0`

For the current hello-world model:

- state: `theta`
- input: actuator effort or command `u`
- parameters: `p`
- passive response: joint or tissue resistance

The long-term value of the model is this separation:

1. actuator side
2. passive finger side
3. equilibrium condition

That structure should survive even as the constitutive laws get more realistic.

## Linear MCP Baseline

The current 1-DOF quasi-static MCP model can be written as:

`tau_app - k (theta - theta_0) = 0`

Interpretation:

- `tau_app` is the applied flexion torque
- `theta_0` is the neutral or preload reference angle
- `k` is a lumped passive torsional stiffness

This is a useful first model because it treats the finger as a rigid rotational degree of freedom resisted by a passive torsional element.

## Why The Nonlinear Step Matters

The linear model assumes constant stiffness:

`d tau_passive / d theta = k`

That is a local approximation, not a general description of passive finger resistance.

For thesis purposes, the reason to move beyond linear is not that nonlinear curves look better. It is that a more realistic passive law can capture:

- angle-dependent resistance
- stiffer end-range behavior
- possible preload around neutral
- future asymmetry between flexion and extension if needed

The mechanics framework stays the same. Only the passive constitutive law changes.

## Clean General Upgrade

Replace the linear passive term with a generic constitutive law:

`tau_passive(theta) = f(theta - theta_0)`

Then the same equilibrium statement becomes:

`tau_act(theta, u, p) - f(theta - theta_0) = 0`

This is the right conceptual upgrade because it preserves the same governing equation while improving the passive tissue model.

## Three-Layer View

The model is easier to scale if it is kept in three layers.

### Layer A: Kinematics

How configuration is described.

For now:

- `q = theta`

Later:

- `q = [theta_MCP, theta_PIP, theta_DIP]`
- plus actuator or tendon coordinates if needed

### Layer B: Constitutive Laws

How each element generates torque or force.

Examples:

- `tau_passive(theta)`
- `tau_act(theta, u)`
- moment arm terms such as `r(theta)`
- variable-stiffness settings such as `k_act(s)`

### Layer C: Governing Equation

How the contributions combine.

Quasi-static:

- `sum tau = 0`

Dynamic later:

- `M(q) q_ddot + C(q, q_dot) + tau_passive(q, q_dot) = tau_act(q, q_dot, u)`

## Energy View

For passive structures, an energy interpretation is often cleaner than direct curve-fitting alone.

If passive energy is `U(theta)`, then:

`tau_passive(theta) = dU / dtheta`

For a constant actuator torque, define total potential:

`Pi(theta) = U(theta) - tau_act theta`

Equilibrium satisfies:

`dPi / dtheta = 0`

This viewpoint becomes more useful as soon as the model includes more joints or more compliant elements.

## A Good First Nonlinear Law

A cubic passive law is a good first extension:

`tau_passive(theta) = k_1 (theta - theta_0) + k_3 (theta - theta_0)^3`

Why this is useful:

- it reduces to the linear model near neutral
- it creates angle-dependent stiffness
- it is still easy to interpret
- it is simple enough for parameter sweeps and fitting

The effective local stiffness becomes:

`k_eff(theta) = d tau_passive / d theta = k_1 + 3 k_3 (theta - theta_0)^2`

This gives a practical interpretation:

- near `theta_0`, stiffness is approximately `k_1`
- farther from neutral, stiffness rises if `k_3 > 0`

## Why Numerical Solving Is A Feature

The linear model gives a closed form:

`theta = theta_0 + tau_app / k`

The nonlinear model usually requires solving:

`g(theta) = tau_act(theta, u, p) - tau_passive(theta, p) = 0`

This should be treated as the gateway to more realistic models, not as a nuisance. Once the equilibrium problem is accepted as a nonlinear solve, the same structure can absorb:

- richer passive laws
- configuration-dependent actuator torque
- tendon routing
- multi-joint coordinates

## Stability Reminder

Zero net torque is not enough by itself. The equilibrium should also be locally restoring.

For a constant actuator torque:

`d tau_net / d theta = - d tau_passive / d theta`

So a positive passive slope gives local restoring behavior:

`d tau_passive / d theta > 0`

This means the passive slope is both a stiffness interpretation and a local stability check.

## Recommended Modeling Ladder

### Stage 1

1-DOF MCP, quasi-static, constant actuator torque, linear passive spring

`tau_app - k (theta - theta_0) = 0`

### Stage 2

1-DOF MCP, quasi-static, constant actuator torque, nonlinear passive spring

`tau_app - f(theta - theta_0) = 0`

### Stage 3

1-DOF MCP, quasi-static, geometry-aware actuator model

`tau_act(theta, u) - f(theta - theta_0) = 0`

### Stage 4

Multi-DOF finger, quasi-static

`tau_act(q, u) - tau_passive(q) = 0`

### Stage 5

Dynamic finger-actuator model

`M(q) q_ddot + C(q, q_dot) + tau_passive(q, q_dot) = tau_act(q, q_dot, u)`

## Working Thesis Interpretation

For this thesis, the nonlinear single-DOF step is not a side quest.

It is the cleanest bridge between:

- a minimal hello-world model
- more realistic passive finger behavior
- future variable-stiffness actuator coupling
- later bench-top validation questions

The next step should therefore be framed as:

`replace the passive constitutive law with an angle-dependent torque model while preserving the same equilibrium framework`

That is more precise than saying "make the curve nonlinear."

## Paper-Linked Hooks To Verify Before Thesis Writing

These are promising anchors, but they should be verified in the corresponding paper notes before they are promoted into writing-safe thesis text.

- `p2025_gallup_tendonhyperelasticfinger.md`
  - likely relevant for nonlinear tendon-driven equilibrium with compliant joints
- `p2024_zhou_tendondrivenfinger.md`
  - likely relevant for reduced tendon-driven finger abstraction choices
- `p2023_peperoni_self_aligning_mcp.md`
  - already useful as a hardware anchor for an MCP-dominant simplification, even though it is not the passive-law paper

## Immediate Notebook Consequence

Before adding more plots, the useful next derivation is:

1. write `g(theta) = tau_act - tau_passive(theta)`
2. substitute a cubic passive law
3. interpret each term physically
4. inspect how `k_eff(theta)` changes over the range of motion
5. only then implement numerical root-finding and parameter sweeps
