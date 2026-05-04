# CURRENT_TASK

## Primary Active Task

Build the first design-screening mechanics layer for the reduced-order index-finger tendon-routing model.

This task should connect the current routing geometry model to passive joint torque, tendon tension estimates, and underactuation mismatch so that candidate ring/thimble/sleeve layouts can be ranked before CAD and prototyping.

## Purpose

The thesis needs a defensible bridge from simulation/modeling to physical design. The current routing model already computes tendon path length and `dL/dq`; the next step is to add the mechanics layer that turns those quantities into design-relevant outputs:

- passive required torque over a target finger-tapping or flexion sweep
- tendon torque per newton for candidate routing paths
- least-squares scalar tendon tension for one independent flexion input spanning MCP/PIP/DIP, possibly through multiple side branches
- residual torque mismatch as a measure of underactuation
- stroke, sign validity, and routing smoothness metrics for candidate designs

The goal is not yet full optimization or final CAD. The goal is to make one routing candidate evaluable end-to-end, then use that evaluator for a small parameter sweep.

## Workstream Context

- Primary workstream: `Simulation Modeling`
- Parallel repo workstream: `Literature`
- Current modeling notebook: `simulation_modeling/notebooks/04_joint_trajectories.ipynb`
- Current routing model: `simulation_modeling/v0_model.py`
- Current passive torque module: `simulation_modeling/passive_joint_models.py`
- Design-reference notebook: `simulation_modeling/model_parameters.ipynb`

The broader Parkinson device landscape review is paused as the primary task, but still matters as thesis context. Literature claims should still be source-checked before entering writing-safe thesis synthesis.

## Expected Outputs

- a cleaned `04_joint_trajectories.ipynb` showing:
  - passive required MCP/PIP/DIP torque over `q_sweep`
  - flexion-path tendon torque per newton with correct units
  - least-squares input tension for one posture, then over the sweep
  - residual torque mismatch over the sweep
- tested passive torque functions in `simulation_modeling/passive_joint_models.py`
- one candidate-routing evaluator function or scratch implementation that returns:
  - tendon stroke or pull distance
  - required tendon tension estimate
  - fitted tendon torque
  - residual torque error
  - branch lengths and branch imbalance if the input splits into left/right side routes
  - sign/feasibility flags
- a small first comparison between at least two routing candidates, such as:
  - thimble-only
  - two-guide flexion path
  - high-offset two-guide flexion path
- a short note or notebook markdown block documenting assumptions, sign convention, units, and known omissions

## Constraints

- keep the model quasi-static for this stage
- keep dynamics, tapping frequency, impact/contact timing, and motor bandwidth out of v0 mechanics scoring
- keep tendon friction, slack, stretch, soft-tissue pressure, and ring deformation listed as limitations unless explicitly tested
- do not collapse actuator count, independent tension inputs, and physical routing branch count into one term
- do not treat one-input least-squares tension as independent control of MCP/PIP/DIP
- use least-squares projection as a mismatch/design-screening metric, not as proof that underactuation is solved
- for the current concept, model one flexion input that may split into multiple branches before adding an active extension input
- keep geometry units clear: routing geometry in `v0_model.py` is currently in millimeters, while passive torques are in `Nm`
- prefer small, inspectable helper functions over a large optimization framework at this stage

## Done When

- one flexion routing candidate can be evaluated from `q_sweep` to:
  - passive required torque
  - branch and total tendon torque per newton
  - least-squares required tension
  - fitted torque
  - residual torque mismatch
  - tendon stroke
  - branch imbalance, if applicable
- the notebook output is interpretable enough to explain why a routing candidate is promising or poor
- the next task can be either:
  - a small parameter sweep over ring/guide placement, or
  - source-checking literature values for tapping kinematics and passive stiffness
