# Intern Research Onboarding

## Purpose

This document is a short onboarding brief for visiting research interns joining a thesis project on simplified finger-actuator systems for neurorehabilitation.

It is designed for mixed-background students and aims to do two things:

- explain the current thesis problem clearly
- provide a focused reading agenda that gets new contributors productive quickly

## Project In One Paragraph

The project studies how a simplified soft variable-stiffness actuator can interact with a finger model in a way that is useful for neurorehabilitation-oriented motion assistance. The emphasis is not on building a full wearable glove or making clinical claims. The emphasis is on understanding actuator-finger interaction, controllability, and validation in a tractable finger-scale system. Earlier literature exploration used Parkinson-related finger tapping as a motivating task because it provides a well-defined repetitive finger-motion context, but the project is now better framed more broadly around rehabilitation-relevant repetitive finger motion.

## Current Direction

The clean current direction is:

- focus on a simplified finger-actuator system rather than a full hand device
- use reduced-order modeling as the main technical starting point
- use the literature to identify meaningful motion targets, validation metrics, and mechanism tradeoffs
- keep the framing broad enough for neurorehabilitation relevance, while still learning from Parkinson finger-tapping literature where it helps define repeated finger-motion behavior

In practical terms, this means the project currently sits at the intersection of:

- hand and finger rehabilitation devices
- reduced-order biomechanical modeling
- variable-stiffness actuation concepts
- benchtop validation and interpretable performance metrics

## What The Project Is Not

To avoid confusion, this project is not currently trying to be:

- a full rehabilitation glove project
- a clinical efficacy study
- a sensing-first system
- a full anatomical or FEM hand model
- a broad survey of every rehabilitation technology

## Why This Problem Matters

Finger assistance for rehabilitation is mechanically small but scientifically dense. Even a simplified finger system raises useful questions:

- What level of model complexity is enough to say something meaningful?
- Which mechanism families are realistic for finger-scale assistance?
- How should assistance quality be evaluated beyond simple range of motion?
- What is gained when stiffness can be tuned rather than fixed?

These questions matter because rehabilitation devices often face a tradeoff between support, comfort, controllability, repeatability, and safety.

## Literature Map

The most useful literature for this project falls into five buckets.

### 1. Task Definition And Motor Impairment Framing

These papers help define what repeated finger motion means and which motion features are worth measuring.

Key value:

- separates simple slowness from richer movement deficits
- helps define clinically meaningful or task-meaningful observables
- provides a more careful language for repetitive finger motion

Representative sources:

- Bologna et al., 2020
- Paparella et al., 2026
- Zarrat Ehsan et al., 2026

### 2. Finger Tapping Assessment Technologies

These papers are useful not because they provide actuation hardware, but because they define measurement logic for repetitive finger motion.

Key value:

- identifies observable features such as amplitude, timing, variability, and interruption
- shows how repetitive finger tasks are analyzed in practice
- helps bridge engineering outputs to meaningful movement behavior

Representative sources:

- Guo et al., 2022
- Ravichandran et al., 2023
- Amo-Salas et al., 2024
- Zarrat Ehsan et al., 2026

### 3. Hand And Finger Rehabilitation Devices

These are currently the strongest mechanical precedents for the project.

Key value:

- shows how simplified single-finger or MCP-centered systems are designed
- provides examples of self-alignment, actuation layout, and validation methods
- helps identify tractable hardware abstractions for a thesis-scale system

Representative sources:

- Schabowsky et al., 2010
- Sun et al., 2021
- Peperoni et al., 2023
- Peperoni et al., 2024
- Saldarriaga et al., 2024

### 4. Variable-Stiffness And Soft Actuation Concepts

These papers matter because the thesis is not just about moving a finger. It is about whether variable stiffness changes interaction quality in a useful way.

Key value:

- compares compliant versus more structured actuation strategies
- helps identify realistic mechanism families
- supports discussion of controllability and safe interaction

Representative sources:

- Shi et al., 2020
- McCall et al., 2024
- Li et al., 2024
- Tabrizi et al., 2024
- Besharati et al., 2025

### 5. Broader Neurorehabilitation And Parkinson Context

These papers are useful mainly as positioning sources, not direct mechanism templates.

Key value:

- clarifies symptom-specific and task-specific design logic
- separates assistance from stabilization or suppression
- provides context for why repeated finger motion matters in neurological rehabilitation

Representative sources:

- Raciti et al., 2022
- Yi et al., 2025
- Raciti et al., 2025

## Current Interpretation Of The Literature

Three points are especially important for new interns.

### 1. The direct hardware literature is stronger for rehabilitation devices than for disease-specific tapping assistance

The strongest direct mechanical precedents are not highly specific Parkinson finger-tapping exoskeletons. They are rehabilitation-oriented finger devices, especially MCP-centered or index-finger systems. This matters because it suggests the project should be grounded in the clearest hardware evidence rather than forced into an overly narrow disease-specific mechanism story.

### 2. The assessment literature is stronger than the direct assistance literature for repeated finger motion

Repeated finger tasks such as tapping are well studied as assessment tasks. That literature is useful because it helps define motion observables and task-level metrics. It is less useful as a direct actuation blueprint.

### 3. A reduced-order model is a strength, not a weakness

The current direction favors a model that is simple enough to interpret and validate. A well-designed reduced-order model can still support meaningful questions about torque balance, passive behavior, effective stiffness, controllability, and repeated-motion performance.

## Technical Questions That Matter Most

New contributors should keep the following questions in mind while reading:

1. What is the simplest useful biomechanical finger model for this problem?
2. Which actuator representations are realistic without making the model too complex too early?
3. Which output variables best describe repeated finger-motion quality?
4. How should variable stiffness be justified: through controllability, safety, repeatability, disturbance handling, or another benefit?
5. Which validation methods translate cleanly from simulation to benchtop experiments?

## Recommended Reading Agenda

The reading agenda below is intentionally staged. The first goal is orientation, not exhaustive coverage.

### Stage 1: Understand The Motion Problem

Read first:

1. Bologna, Paparella, Fasano, Hallett, and Berardelli. 2020. *Evolving concepts on bradykinesia*. *Brain*. DOI: `10.1093/brain/awz344`
2. Paparella et al. 2026. *Analyzing the ‘Bradykinesia Complex’ in Parkinson's Disease*. *Movement Disorders*. DOI: `10.1002/mds.70082`
3. Zarrat Ehsan et al. 2026. *Interpretable and granular video-based quantification of motor characteristics from the finger-tapping test in Parkinson’s disease*. *npj Parkinson's Disease*. DOI: `10.1038/s41531-026-01307-w`

Goal:

- understand how repeated finger motion can be decomposed into more than just speed

### Stage 2: Understand How The Task Is Measured

Read next:

1. Guo et al. 2022. *Vision-Based Finger Tapping Test in Patients With Parkinson’s Disease via Spatial-Temporal 3D Hand Pose Estimation*. *IEEE JBHI*. DOI: `10.1109/JBHI.2022.3162386`
2. Ravichandran et al. 2023. *iTex Gloves: Design and In-Home Evaluation of an E-Textile Glove System for Tele-Assessment of Parkinson’s Disease*. *Sensors*. DOI: `10.3390/s23062877`
3. Amo-Salas et al. 2024. *Computer Vision for Parkinson’s Disease Evaluation: A Survey on Finger Tapping*. *Healthcare*. DOI: `10.3390/healthcare12040439`

Goal:

- understand what kinds of signals and features are used to characterize repeated finger motion

### Stage 3: Understand The Strongest Hardware Precedents

Read next:

1. Schabowsky et al. 2010. *Development and pilot testing of HEXORR: Hand EXOskeleton Rehabilitation Robot*. *Journal of NeuroEngineering and Rehabilitation*. DOI: `10.1186/1743-0003-7-36`
2. Sun, Li, and Cheng. 2021. *Design and Validation of a Self-Aligning Index Finger Exoskeleton for Post-Stroke Rehabilitation*. *IEEE TNSRE*. DOI: `10.1109/TNSRE.2021.3097888`
3. Peperoni et al. 2023. *Self-Aligning Finger Exoskeleton for the Mobilization of the Metacarpophalangeal Joint*. *IEEE TNSRE*. DOI: `10.1109/TNSRE.2023.3236070`
4. Peperoni et al. 2024. *Post-traumatic hand rehabilitation using a powered metacarpal-phalangeal exoskeleton: a pilot study*. *Journal of NeuroEngineering and Rehabilitation*. DOI: `10.1186/s12984-024-01511-w`

Goal:

- understand what a tractable single-finger hardware precedent looks like

### Stage 4: Understand Soft And Variable-Stiffness Directions

Read after the first three stages:

1. Shi et al. 2020. *Verification of Finger Joint Stiffness Estimation Method With Soft Robotic Actuator*. *Frontiers in Bioengineering and Biotechnology*. DOI: `10.3389/fbioe.2020.592637`
2. McCall, Buckner, and Kamper. 2024. *Soft pneumatic actuators for pushing fingers into extension*. *Journal of NeuroEngineering and Rehabilitation*
3. Saldarriaga, Gutierrez-Velasquez, and Colorado. 2024. *Soft Hand Exoskeletons for Rehabilitation: Approaches to Design, Manufacturing Methods, and Future Prospects*. *Robotics*. DOI: `10.3390/robotics13030050`
4. Besharati et al. 2025. *Assist-as-needed control of a soft rehabilitation robot for the finger using an interaction torque observer*. *European Journal of Control*

Goal:

- understand why variable stiffness and compliant interaction may matter, and where the evidence is still thinner

## How To Read Efficiently

For each paper, interns should try to answer the same short set of questions:

- What motion is the system targeting?
- Is the paper about assessment, assistance, stabilization, or control?
- What mechanism family is used?
- What variables are measured?
- What makes the result useful for this project?
- What does the paper not solve?

## Good Output From A New Intern

A useful early contribution is not a broad summary of everything. A useful early contribution is a sharp synthesis such as:

- a comparison of three finger-device mechanism families
- a summary of repeated finger-motion metrics across assessment papers
- a shortlist of validation variables that appear consistently across the literature
- a summary of where variable stiffness appears to help, and where that claim is still weak

## Two Open Directions Worth Watching

The current direction is intentionally clean, but two design questions remain worth keeping in view:

- Should the project frame its main task as finger tapping specifically, or more generally as rehabilitation-relevant repetitive finger motion?
- Which benefit of variable stiffness will ultimately be the strongest one to defend: controllability, comfort, repeatability, or interaction quality?

These are not reasons to widen the project. They are simply the main questions that will sharpen the final thesis framing.

## Suggested Starter Zotero Collection

If a shared Zotero collection is created for interns, it should stay small at first. A good starter collection would contain:

- the three motion-framing papers from Stage 1
- the three assessment papers from Stage 2
- the four hardware papers from Stage 3
- two to four soft or variable-stiffness papers from Stage 4

That produces a collection of roughly `12 to 14` papers, which is enough for onboarding without becoming a full literature dump.

## Short Closing Summary

The project is best approached as a simplified, interpretable study of finger-actuator interaction for rehabilitation-relevant repeated motion. The clearest immediate literature value comes from combining:

- movement-definition papers
- assessment papers that define meaningful outputs
- finger rehabilitation hardware papers that offer realistic mechanism precedents

That combination should give new interns a strong enough foundation to contribute without needing the entire backstory of the thesis.
