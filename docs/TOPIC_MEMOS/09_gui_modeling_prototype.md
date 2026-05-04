# GUI Modeling Prototype

## Status

As of `2026-04-24`, this memo describes the GUI/prototype track, but the newer routing-model work in `simulation_modeling/v0_model.py` has moved beyond the original straight-line tendon abstraction. Treat the sections below as the GUI baseline plus upgrade target, not as the full current state of the modeling branch.

## Purpose

Create a small visualization-first interface for the simulation-modeling workstream so reduced-order finger-actuator assumptions can be explored without editing notebook cells every time.

The current implementation uses a Streamlit browser GUI with Plotly visualizations.

## Recommended First Scope

- keep the original 1-DOF model as the torque-balance baseline
- add a 3-link index-finger kinematic/passive mode for MCP, PIP, and DIP exploration
- support two reduced templates: `Index MCP proxy` and `Thumb flexion proxy`
- support two passive laws: linear and cubic
- support two actuator abstractions:
  - direct joint torque
  - a tendon-like line of action with a fixed base anchor and moving distal attachment
- support a preliminary 3-link index model with:
  - proximal, middle, and distal phalanx lengths
  - MCP/PIP/DIP joint angles
  - MCP/PIP/DIP neutral angles and passive stiffness
  - optional hard DIP-PIP coupling
- visualize:
  - current geometry
  - actuator torque, passive torque requirement, and net torque versus angle
  - equilibrium angle versus actuator input sweep
  - 3-link index-finger geometry
  - passive torque and local stiffness at MCP/PIP/DIP

## Why This Scope Fits The Thesis

- it stays aligned with the repo's current reduced-order quasi-static modeling baseline
- it adds actuator placement effects without forcing a full hand model or FEM
- it is simple enough to support parameter reasoning, supervisor discussion, and eventual benchtop mock-up planning

## Current Assumptions

- one effective flexion coordinate per digit template in the 1-DOF mode
- planar MCP/PIP/DIP kinematics in the 3-link index mode
- quasi-static torque balance only in the 1-DOF mode
- passive joint-load visualization only in the 3-link mode
- no contact, no tendon wrapping, no friction, no inertia
- thumb and index are represented as reduced proxies, not anatomical multi-joint reconstructions
- tendon routing is approximated by a straight line from fixed anchor to moving attachment
- DIP-PIP coupling is optional and currently hard kinematic coupling only, not soft anatomical coupling

## Current Routing Model Update

The standalone v0 routing model now uses a more appropriate abstraction than the original single straight-line tendon in the GUI:

- `FingerGeometry` and `FingerKinematics` define the planar three-link finger.
- `RoutingElement` represents mechanically meaningful routing features with a `kind`, currently `entry`, `guide`, or `anchor`.
- `RoutingPath` represents an ordered sequence of routing elements attached to world, proximal, middle, or distal frames.
- `tendon_path_length()` computes the full routed path as straight segments between effective points.
- `tendon_excursion()` computes path-length change relative to neutral.
- `tendon_gradient()` computes posture-dependent `dL/dq` with central differences.
- `tendon_torque()` maps assumed tendon tension into generalized joint torque through `tau_tendon = -T * dL/dq`.
- `coordinated_flexion_sweep()` and `evaluate_path_over_sweep()` separate sweep generation from plotting.

The important conceptual change is that `guide` should no longer be read as a literal physical ring by default. In the model, routing elements are effective path-redirection or attachment points. A single soft ring, thimble slot, strap, or dorsal retainer may be represented by one or more effective routing elements later, but v0 intentionally avoids that local contact detail.

## Main Limitations

- the tendon model is still not a full musculoskeletal routing model
- the GUI does not yet expose the full `RoutingElement`/`RoutingPath` model from `v0_model.py`
- multiple equilibrium branches can exist, but the sweep view currently follows only one continuation branch
- the 3-link mode does not yet solve multi-joint equilibrium with an actuator
- the 3-link mode does not yet include tendon moment arms, dorsal zig-zag actuation, or antagonistic flexion/extension paths
- the GUI is an exploration tool, not yet a validated simulation package
- the current templates are placeholders for thesis reasoning and should be replaced by literature-backed parameter sets later
- the current app is optimized for exploration and discussion, not packaged deployment

## Next Useful Upgrades

- expose the `RoutingElement`/`RoutingPath` abstraction in the GUI
- add flexion and extension routing presets that reproduce the v0 sanity-check plots
- add summary plots for path length, excursion, gradient, and torque-per-newton over a coordinated sweep
- connect the 3-link index model to a tendon or dorsal zig-zag actuator branch
- add multi-joint equilibrium solving for MCP/PIP/DIP under actuator torques
- add soft DIP-PIP coupling as a passive penalty term rather than only hard kinematic coupling
- add thumb-index opposition distance or pinch gap as an output variable
- add import/export of parameter presets for literature-backed model variants
- connect the GUI controls to validation datasets once benchtop measurements exist
