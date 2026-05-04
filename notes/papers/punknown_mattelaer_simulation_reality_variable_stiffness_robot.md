# From simulation to reality: a variable-stiffness robot

## Metadata

- Paper ID: `ZOTERO:5FMUJP7H`
- Zotero key: `5FMUJP7H`
- Topic: ``
- Status: `inbox`
- Priority: `medium`
- Source: `zotero`
- Year: `2025?`
- Venue: 
- Authors: Louise Mattelaer
- DOI: _missing_
- URL: _missing_
- PDF status: `attached`
- PDF path: /Users/rami/Zotero/storage/AE8C2X9N/Mattelaer - From simulation to reality a variable-stiffness robot.pdf
- Zotero open link: zotero://select/library/items/AE8C2X9N

## Audit Status

- Reading stage: captured
- Source verification: checked against attached PDF
- Exact quotes logged: yes
- Last audited: 2026-04-28
- Used in: `docs/TOPIC_MEMOS/10_variable_stiffness_design_concepts.md`

## Why This Paper Is In The Queue

This is a close internal precedent for the thesis because it starts from a simplified simulation of a variable-stiffness robot, validates the simulation against a physical prototype, and treats stiffness as an experimentally calibrated property rather than as a fully derived analytical model.

## Citation / Bibliographic Notes

- Title: From simulation to reality: a variable-stiffness robot
- Authors: Louise Mattelaer
- Venue: 
- Year: 2025? PDF title page says `June, 2023`, but project period and PDF creation date indicate 2025. Verify before formal citation.
- DOI: 
- URL: 
- Tracker question: How does this thesis define and operationalize variable stiffness when moving from simulation to a real prototype?

## Classification

- Type: MSc thesis
- Topic: variable-stiffness robot simulation and experimental validation
- Actuation type: twisted-string actuation with vertebra-like links
- Model type: MATLAB Simscape reduced-order dynamic model; ANN inverse dynamics for 2D bending
- Validation type: physical bending tests and impact-force tests

## Source-Verified Summary

Mattelaer characterizes a twisted-string-actuated variable-stiffness robot intended for UAV package-delivery/collision-resilience applications. The study first validates a MATLAB Simscape bending model against physical bending measurements, then extends the model to impact tests against a rigid target, and finally trains an ANN inverse-dynamics model for 2D bending. The useful thesis precedent is not the UAV application itself, but the workflow: simplify the real mechanism into a tractable simulation, calibrate the simulation using physical measurements, and use stiffness/speed tradeoffs as experimentally grounded design variables.

## One-Sentence Thesis Relevance

- Strong methodological precedent for treating variable stiffness as an effective, experimentally calibrated robot property when a full analytical model of the actuation mechanism is too complex.

## Core Definitions (Only From Source)

- Term: Variable Stiffness Robot
  - Definition: A soft robot that can modify its stiffness.
  - Support: Introduction, p. 1.
- Term: Linear stiffness
  - Definition: `K = F / delta`, where force is divided by deformation.
  - Support: Section 3.1.2, Eq. 3.1, p. 9.
- Term: Rotational stiffness
  - Definition: `K = M / theta`, where moment is divided by angular displacement.
  - Support: Section 3.1.2, Eq. 3.2, p. 9.
- Term: Twisted-string load-side stiffness
  - Definition: `S = partial F_z / partial p`, with a static helical-string expression depending on strand count, string length, motor rotation angle, unloaded strand length, and strand radius.
  - Support: Section 3.1.2, Eq. 3.3, p. 10.

## How They Operationalize Variable Stiffness

- The physical stiffness input is the amount of string twist or pulling force.
- The simulation does not model the internal twisted-string mechanics directly.
- Instead, the real pulling force is mapped to simulated revolute-joint stiffness using bending experiments.
- The relationship between pulling force `F_p` and joint stiffness `k` is fit empirically with a third-degree polynomial:

```text
k = 6.03e-6 F_p^3 - 1.69e-3 F_p^2 + 3.04e-1 F_p + 1.50
```

- This means the paper's practical definition is closer to effective stiffness calibration than independent variable-stiffness control.

## Main Claims (Only From Source)

- Claim: Low stiffness improves safer interaction, but can reduce precision.
  - Explanation: The paper frames VSRs as useful because high stiffness increases impact force, while low stiffness can hurt precision, so stiffness should vary with operational demands.
  - Support: Section 3.1.2, p. 9.
- Claim: Twisted-string actuation changes system stiffness as twist changes.
  - Explanation: The paper states that more twist makes the system more rigid and gives a static load-side stiffness expression.
  - Support: Section 3.1.2, p. 10.
- Claim: The internal twisted-string model is too complex for the target simulation workflow.
  - Explanation: Eq. 3.3 requires string parameters that may not be available and is only static, so the study uses Simscape and empirical calibration.
  - Support: Section 3.1.2, p. 10; Section 4.1.3.2, pp. 22-24.
- Claim: Pulling force can be used as an experimental proxy for simulated joint stiffness.
  - Explanation: Bending data are used to iteratively find the simulated revolute-joint stiffness that matches the physical robot angle, then polynomial-fit the relation.
  - Support: Section 4.1.3.2, pp. 22-24.
- Claim: Impact force increases approximately linearly with pulling force/stiffness and speed over the tested range.
  - Explanation: The paper uses this trend for a simple tradeoff optimization.
  - Support: Results/discussion, pp. 45-49.

## Key Quotes (Only When Wording Matters)

- Quote: "Soft robots that can modify their stiffness"
  - Page: 1
  - Why wording matters: This is the paper's compact VSR definition.
- Quote: "Depending on how much the strings have been twisted, the stiffness of the system will change."
  - Page: 10
  - Why wording matters: Establishes twist amount as the physical stiffness-setting variable.
- Quote: "the system will be simulated rather than analytically computed"
  - Page: 10
  - Why wording matters: Justifies the simulation-first, calibrated-model approach.

## Mechanistic Insights (From Paper)

- Mechanism: Twisted-string contraction
  - Description: Motor rotation twists at least two strings around each other, reducing their effective length and moving the load.
  - Support: Section 3.1.2, Fig. 3.1, p. 9.
- Mechanism: Twist-dependent stiffness
  - Description: Increasing twist increases effective rigidity at the load side, but the full analytical expression is parameter-heavy and static.
  - Support: Section 3.1.2, Eq. 3.3, p. 10.
- Mechanism: Empirical stiffness substitution in simulation
  - Description: The physical pulling force is represented in Simscape by revolute-joint stiffness and damping, with damping set by critical damping and stiffness fit from experiments.
  - Support: Section 4.1.3.2 and Chapter 4 summary, pp. 22-34.

## Observations / Results (From Paper)

- Finding: The 2D bending simulation reached small absolute angle error.
  - Description: The conclusion reports an average error of about 1.70 degrees / 11% for the bending model after fitting pulling force to joint stiffness.
  - Support: Conclusion, p. 51.
- Finding: Impact-force validation was less accurate than bending validation.
  - Description: Initial impact-force comparison showed about 30% error; after raising load-cell sampling and changing the model from 2D to 3D bending, the average error dropped to 15.85%.
  - Support: Discussion and conclusion, pp. 49-51.
- Finding: Speed and pulling force/stiffness showed near-linear relationships with impact force over the tested range.
  - Description: This enabled a simple weighted tradeoff optimization between high speed, low pulling force, and low impact force.
  - Support: Section 5.1 and conclusion, pp. 45-51.
- Finding: ANN inverse dynamics worked for the simplified 2D case.
  - Description: The ANN predicted pulling and end-effector forces from displacement and speed with 97.7% accuracy after filtering.
  - Support: Discussion and conclusion, pp. 49-51.

## What This Paper Suggests (Project Interpretation)

- Interpretation: For this thesis, variable stiffness can be defended as a calibrated mapping from a controllable setting to an effective mechanical response, not necessarily as a fully analytical model of the actuator internals.
  - Why it matters: This supports a finger-actuator model where the stiffness setting `c` maps to either `K_act(c)` or `K_series(c)` through bench calibration.
- Interpretation: The paper is a caution against claiming independent stiffness control too early.
  - Why it matters: Mattelaer's VSR changes stiffness through the same physical actuation family that also affects force/motion; this is not automatically independent control of equilibrium position and stiffness.
- Interpretation: The validation pattern is directly reusable.
  - Why it matters: Simulate first, fit stiffness proxy against measured deformation, then validate against held-out physical tests.

## Model / Mechanism / Validation Details

- System type: vertebra-like soft/continuum-inspired VSR prototype for UAV use.
- Actuation type: twisted-string actuation.
- Model type: MATLAB Simscape model using simplified joints rather than full internal string mechanics.
- Validation setup: physical bending measurements under pulling/end-effector forces; impact tests against a wall/target using load-cell data.
- Main metrics: bending angle error, pulling-force-to-joint-stiffness fit error, impact force error, ANN inverse-dynamics accuracy.

## What Matters For This Thesis

- The most transferable idea is effective stiffness: measure how the prototype responds to a controllable stiffness setting, then use that mapping in the simulation.
- A finger thesis can define stiffness at the joint, tendon transmission, or fingertip/end-effector level; the definition must state which level is being used.
- The paper supports avoiding full FEM or full twisted-string analytical modeling unless the simplified model fails validation.
- The paper's VSR is not finger-specific and not rehabilitation-specific; use it as a modeling/validation precedent, not a direct device precedent.

## Relevance To Finger Tapping / Thesis

- Direct relevance: Low. The device is a UAV-oriented VSR, not a finger rehabilitation or tapping device.
- Indirect relevance: High for the simulation-to-reality workflow and for defining variable stiffness as an experimentally calibrated input-output relation.

## Control-System Interpretation (Project Interpretation)

- Controller: Not the main contribution; simple simulation sweeps and ANN inverse dynamics are emphasized.
- Plant: Twisted-string VSR with bending and impact dynamics.
- Feedback: Experimental measurements of bending angle and impact force are used to validate/calibrate the simulation.
- Reference: Desired bending displacement/speed for ANN inverse dynamics; speed and pulling-force settings for impact optimization.
- Notes: The work is closer to characterization and model calibration than closed-loop variable-stiffness control.

## Exact Quotes / Evidence Bank

- Quote: "A VSR can change the stiffness depending on the varying operational demands."
- Page: 9
- Section or figure: Section 3.1.2
- Why it matters: Connects variable stiffness to task-dependent tradeoffs.
- Reusable in: variable-stiffness definition discussion

- Quote: "The more the strings are twisted, the more rigid the system."
- Page: 10
- Section or figure: Section 3.1.2
- Why it matters: Identifies the mechanism-level stiffness setting.
- Reusable in: twisted-string actuator discussion

- Quote: "The stiffness is only computed in steady state"
- Page: 24
- Section or figure: Section 4.1.4
- Why it matters: Their displayed stiffness is quasi-static/effective, not a full dynamic stiffness law.
- Reusable in: limitations section

## Claims Safe To Reuse Later

- Claim: Mattelaer defines variable stiffness in practical mechanical terms: a robot can modify stiffness, and stiffness can be measured as force/deformation or moment/angular displacement.
- Support: Sections 1.1 and 3.1.2, pp. 1 and 9.
- Confidence: high

- Claim: In this VSR, the stiffness setting is coupled to twisted-string actuation/pulling force and is calibrated into the simulation through an empirical polynomial.
- Support: Sections 3.1.2 and 4.1.3.2, pp. 10 and 22-24.
- Confidence: high

- Claim: The paper supports a reduced-order simulation-first workflow followed by physical calibration and validation.
- Support: Abstract, Sections 4-5, Discussion, Conclusion.
- Confidence: high

## What This Paper Does Not Answer

- Gap: It does not provide a finger biomechanics model or rehabilitation interaction model.
- Gap: It does not show independent control of equilibrium position and stiffness.
- Gap: It does not establish whether stiffness modulation improves human-device comfort, motor learning, or clinical outcomes.
- Gap: It does not validate high-speed/high-force nonlinear contact beyond the tested range.

## Open Questions

- Question: For this thesis, should stiffness be defined at the actuator, tendon/transmission, joint, or fingertip level?
- Question: Can the planned prototype vary stiffness independently enough from movement input to make a clean variable-stiffness claim?
- Question: What is the equivalent calibration experiment for a finger device: fingertip force-displacement, joint torque-angle, tendon force-excursion, or actuator free deformation?

## Limitations

- Bibliographic year is inconsistent in the PDF metadata/title matter and should be verified before citation.
- The VSR application is UAV collision resilience, so relevance to neurorehabilitation is methodological rather than clinical.
- The stiffness treatment is quasi-static/effective in key parts of the model.
- The empirical polynomial is system-specific and should not be reused numerically for the finger thesis.

## Tags

- `variable-stiffness`
- `twisted-string-actuation`
- `sim-to-real`
- `model-calibration`
- `effective-stiffness`

## Decision Impact

- Which memo or decision this should affect: `docs/TOPIC_MEMOS/10_variable_stiffness_design_concepts.md`; later actuator abstraction decision.
- What it changes: Supports defining variable stiffness as a calibrated effective stiffness map, while explicitly avoiding claims of independent stiffness control unless the prototype demonstrates that separation.

## Next Action

Use this paper when drafting the thesis definition of variable stiffness. Phrase it as effective stiffness modulation unless a later mechanism provides independent stiffness control.
