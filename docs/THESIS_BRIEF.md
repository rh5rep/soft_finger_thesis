# THESIS_BRIEF

## Official Thesis Statement

**Title:** Biomechanical Modeling and Experimental Validation of a Soft Variable-Stiffness Finger Actuation System for Neurorehabilitation

**Project window:** March 6, 2026 to August 6, 2026

**Official description:** This thesis investigates the design, modeling, and experimental evaluation of a soft variable-stiffness actuation system for finger movement assistance. The main aim is to study how variable stiffness can improve controllability and biomechanical interaction in a simplified finger system relevant to hand rehabilitation. The planned sequence is literature review, simulation of a biomechanical finger model, implementation of a physical finger-actuator mock-up, and bench-top validation.

## Thesis Objective In Plain Language

Build a defensible first-principles understanding of how a soft variable-stiffness actuator interacts with a simplified finger model, then validate the most useful parts of that understanding with a benchtop mock-up.

## Active Workstreams

The repo currently supports two explicit thesis workstreams.

### Literature

This workstream covers:

- finding new papers and adjacent technologies
- maintaining recurring search topics and automation-ready search workflows
- syncing Zotero metadata into the tracker
- screening, reading, and distilling papers into memos, decisions, and future tasks

### Simulation Modeling

This workstream covers:

- simplified biomechanical finger models
- reduced-order actuator-finger interaction models
- notebook-based exploration, parameter sweeps, and plots
- migration of stable model pieces into reusable Python components when justified

## Current Literature Review Focus

The immediate literature-review task is narrower than the full thesis. The current priority is to understand how hand and finger exoskeleton technologies address, reproduce, or support task-specific motions related to:

- pinch grasp
- thumb-index opposition
- repetitive finger tapping or tapping-like flexion/extension tasks

The goal of this review is not yet to settle the full thesis architecture. The goal is to identify current technologies, how they work, what motion they target, and which design families are closest to a pinch/tapping use case.

This review should not be restricted to soft robotics. It should include any relevant technology family, including:

- soft robotic devices
- rigid-link exoskeletons
- tendon-driven mechanisms
- cable-driven or linkage-driven orthoses
- hybrid or wearable assistive devices
- task-specific assessment or rehabilitation devices when they clarify the target motion

## In Scope

- Soft finger actuation concepts relevant to rehabilitation assistance
- Non-soft exoskeleton or orthosis concepts when they are relevant to pinch grasp, thumb-index opposition, or tapping-like motion
- Variable-stiffness mechanisms and their design trade-offs
- Simplified biomechanical finger modeling for simulation-first studies
- Task-specific hand/finger exoskeleton technologies relevant to pinch grasp and finger tapping
- Disease-specific or rehabilitation-specific contexts only when they help define the target movement and evaluation context
- Bench-top mock-up design and experimental validation
- Metrics such as range of motion, controllability, repeatability, response behavior, robustness, and force-displacement behavior

## Out Of Scope

- Full glove or multi-finger system as the main deliverable
- Embedded elastomeric sensing as a central research axis
- Clinical studies or patient-facing claims
- Full FEM unless later justified by evidence and thesis needs
- Broad rehabilitation-device surveys with no impact on modeling or validation choices

## Core Research Questions

1. What level of finger biomechanical model is sufficient for a first simulation of actuator-finger interaction?
2. Which variable-stiffness actuation concepts are realistic for a thesis-scale simplified finger system?
3. Which hand/finger exoskeleton technologies currently target pinch grasp, thumb-index opposition, or tapping-like finger motion, and how do they work?
4. Which simulation outputs and physical measurements best support validation of the chosen abstraction?
5. How should controllability and biomechanical interaction be evaluated in a simplified rehabilitation-relevant setup?

## Current Architecture Hypothesis

The thesis will likely converge on a reduced-order finger model coupled to a simplified soft variable-stiffness actuator or compliant tendon-transmission representation, with a benchtop mock-up designed to reproduce the key interaction variables needed for validation rather than the full complexity of a wearable rehabilitation device.

Near-term architecture assumption as of `2026-04-24`: compare routing geometry first, then choose the actuator/transmission architecture. TSA, CVT/CTA-style transmission, soft pneumatic actuation, and adjustable series stiffness remain candidate branches, but the first decision should be informed by estimated tendon stroke, posture-dependent leverage, rough tension demand, palmar clearance, and prototype complexity.

## Current Modeling Hypothesis

The first modeling pass should favor a low-order, interpretable, parameterized model over high-fidelity simulation. Likely useful ingredients are joint-level kinematics, tendon-routing path length, tendon excursion, posture-dependent `dL/dq`, passive stiffness, actuator input-output characterization, and a limited set of interaction variables that can be recreated physically.

The current multi-joint baseline is a 2D planar index-finger routing model with effective routing elements. It should be used as a design-screening tool, not only as a visualization.

## Planned Validation Path

1. Review literature and extract viable model classes, actuation concepts, and evaluation metrics.
2. Build a simplified simulation model of the finger-actuator system.
3. Choose a tractable mock-up architecture consistent with the model assumptions.
4. Run benchtop experiments to compare physical behavior with simulation predictions.
5. Document mismatches, limitations, and implications for future assistive hand devices.

## Success Criteria

- A clear thesis framing grounded in literature and design trade-offs
- A simplified biomechanical finger model that is justified and analyzable
- A variable-stiffness actuation concept narrowed to a defensible thesis-scale implementation
- A bench-top validation setup that tests the most important modeled behaviors
- A written trail from literature to decisions to implementation choices

## Biggest Unknowns

- Which finger modeling abstraction is strong enough without becoming too complex
- Which variable-stiffness mechanism family is realistic within thesis constraints
- Whether the most useful task framing for the next review is pinch grasp, finger tapping, thumb-index opposition, or a closely related movement family
- Which technology families are actually most relevant once the search is widened beyond soft robotics
- Which validation metrics are both meaningful and practical for benchtop testing
- How to position the work relative to rehabilitation robotics without overreaching clinically

## Near-Term Milestones

1. Build a task-specific field map around pinch grasp, thumb-index opposition, and finger tapping technologies.
2. Produce a review-ready memo on current technologies and how they work.
3. Identify which technologies are most relevant to a simulation-first simplified finger-actuator study.
4. Continue the first simulation notebook from the 1-DOF quasi-static MCP hello-world model toward a defensible reduced-order modeling baseline.
5. Log the first architecture and modeling decisions after the task framing is clearer.
