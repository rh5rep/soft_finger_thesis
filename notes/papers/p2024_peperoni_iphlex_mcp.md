# Post-traumatic hand rehabilitation using a powered metacarpal-phalangeal exoskeleton: a pilot study

## Metadata

- Paper ID: `DOI:10.1186/s12984-024-01511-w`
- Zotero key: `2JXXMKZZ`
- Topic: `T008`
- Status: `screening`
- Priority: `medium`
- Source: `manual`
- Year: `2024`
- Venue: Journal of NeuroEngineering and Rehabilitation
- Authors: Emanuele Peperoni; Emilio Trigili; Eugenio Capotorti; Stefano Laszlo Capitani; Tommaso Fiumalbi; Foebe Pettinelli; Sara Grandi; Alberto Rapalli; Giulia Lentini; Ilaria Creatini; Nicola Vitiello; Elisa Taglione; Simona Crea
- DOI: 10.1186/s12984-024-01511-w
- URL: https://jneuroengrehab.biomedcentral.com/articles/10.1186/s12984-024-01511-w
- PDF status: `attached`
- PDF path: /Users/rami/Zotero/storage/83J5QNZ8/Peperoni et al. - 2024 - Post-traumatic hand rehabilitation using a powered metacarpal-phalangeal exoskeleton a pilot study.pdf
- Zotero open link: zotero://select/library/items/83J5QNZ8

## Audit Status

- Reading stage: quote-verified
- Source verification: checked against PDF on 2026-04-06
- Exact quotes logged: yes
- Last audited: 2026-04-06
- Used in: docs/STUDY_GUIDE.md

## Why This Paper Is In The Queue

Useful because it takes the `I-Phlex` mechanism into a real clinical pilot and shows what a simplified MCP-centered rehab workflow looks like in practice.

## Citation / Bibliographic Notes

- Title: Post-traumatic hand rehabilitation using a powered metacarpal-phalangeal exoskeleton: a pilot study
- Authors: Emanuele Peperoni; Emilio Trigili; Eugenio Capotorti; Stefano Laszlo Capitani; Tommaso Fiumalbi; Foebe Pettinelli; Sara Grandi; Alberto Rapalli; Giulia Lentini; Ilaria Creatini; Nicola Vitiello; Elisa Taglione; Simona Crea
- Venue: Journal of NeuroEngineering and Rehabilitation
- Year: 2024
- DOI: 10.1186/s12984-024-01511-w
- URL: https://jneuroengrehab.biomedcentral.com/articles/10.1186/s12984-024-01511-w
- Tracker question: Which technologies reproduce repetitive tapping-like or MCP flexion-extension motion and how are they evaluated?

## Source-Verified Summary

- This paper presents a `pilot clinical study` using the powered MCP exoskeleton `I-Phlex` in post-traumatic hand rehabilitation.
- The focus is not on inventing a new mechanism from scratch, but on testing:
  - short-term efficacy
  - experience of use
  - safety
  - whether the exoskeleton’s internal measurements are clinically useful
- The device remains `MCP-centered` and uses passive plus active-assistive mobilization paradigms.

## Model / Mechanism / Validation Details

- System type: powered finger exoskeleton for MCP rehabilitation
- Motion scope:
  - `MCP flexion-extension`
- Key device features reused from the mechanism paper:
  - self-alignment mechanism for the MCP joint
  - `remote center of motion`
  - `series elastic actuation (SEA)`
  - customized hand/finger cuffs
- Kinematic chain:
  - `RPR` configuration
  - first rotational joint implemented as a series of geared hinges
  - slider-hinge element provides MCP self-alignment
- Actuation:
  - SEA with torque measurement and compliant control
  - BLDC motor + `111:1` planetary gearbox
  - embedded spring stiffness `2.89 Nm/rad`
  - torque resolution `5 mNm`
  - peak SEA torque `1.5 Nm`
- Modeling/control:
  - direct kinematic model (DKM) estimates MCP angle and torque
  - inverse kineto-static model (IKsM) implemented with user-specific look-up table
  - hierarchical controller supports different rehabilitation paradigms
- Safety / therapy constraints:
  - predefined torque safety threshold `0.45 Nm`
  - allowed ROM overshoot limited to about `5 degrees` above or below set boundaries

## Clinical Protocol Recall

- Participants:
  - `6 subjects`
  - trauma-related illnesses of the `right hand`
- Main measurements:
  - therapist goniometer `PROM` and `AROM`
  - exoskeleton-estimated PROM and AROM
  - pain via `NPRS`
  - usability / experience questionnaires
  - adverse events
- Rehabilitation modes:
  - `passive`
  - `active-assistive`
- Passive exercises included:
  - reduced ROM
  - incremental ROM
  - full ROM
  - hold at full ROM
- Active-assistive exercises included:
  - full ROM
  - hold at full ROM

## Main Metrics / Results

- Median `PROM` increase: `5.88%`
- Median `AROM` increase: `11.11%`
- In absolute terms, median ROM increase about `6 degrees` for both PROM and AROM
- Usability/experience median scores:
  - `93.83` and `80.00` depending on questionnaire block
- No increase in median `NPRS`
- No major adverse event or patient injury
- One device malfunction:
  - broken transmission cable
  - no reported injury or discomfort
- No statistically significant difference between exoskeleton ROM measures and therapist goniometer measures
- Exoskeleton performance metrics:
  - passive mode angle RMSE about `8.12 deg`
  - passive mode torque RMSE about `2.50 mNm`
  - active-assistive angle RMSE about `6.86 deg`
  - active-assistive torque RMSE about `1.80 mNm`

## What Matters For This Thesis

- This paper shows what happens when a simplified MCP-centered device is used in an actual rehab workflow.
- It is useful because it links:
  - simplified mechanism
  - ROM-based therapy protocol
  - clinical goniometer comparison
  - patient usability and safety
- It supports the idea that a reduced-order finger device can still produce clinically legible outputs like:
  - PROM
  - AROM
  - torque
  - smoothness / interaction measurements
- It is one of the clearest examples of a `tractable, bench-to-clinic` path for a small joint-focused exoskeleton.

## Limitations

- Post-traumatic / orthopaedic context, not Parkinson-specific.
- Single-session pilot, not long-term rehabilitation evidence.
- Small sample size (`6` subjects).
- No control group.
- Not a variable-stiffness device.
- Still not a tapping-specific device.

## Decision Impact

- Keep as the `clinical follow-through` companion to the 2023 I-Phlex mechanism paper.
- Use it to show that MCP simplification is not only mechanically plausible but also clinically deployable in principle.
- Helpful when arguing that a thesis can start with a simple abstraction and still connect to meaningful physical evaluation later.

## Exact Quotes / Evidence Bank

- Quote: "mobilize the metacarpal-phalangeal joint"
- Page: 1
- Section or figure: abstract
- Why it matters: confirms the device remains explicitly MCP-centered in the clinical pilot.
- Reusable in: task/mechanism framing

- Quote: "5.88% and 11.11%"
- Page: 1
- Section or figure: abstract results
- Why it matters: gives the headline PROM and AROM change reported in the pilot.
- Reusable in: outcome summary

- Quote: "No major adverse event"
- Page: 1
- Section or figure: abstract results
- Why it matters: supports the basic safety claim for this pilot deployment.
- Reusable in: validation and safety framing

- Quote: "No statistical significance"
- Page: 1
- Section or figure: abstract results
- Why it matters: prevents overstating the clinical effect and preserves the pilot-study limitation.
- Reusable in: limitation discussion

## Claims Safe To Reuse Later

- Claim: Peperoni 2024 is the clinical follow-through paper for the MCP-centered I-Phlex architecture.
- Support: abstract pp.1-2 and kinematic-chain description p.3
- Confidence: high

- Claim: The pilot suggests short-term ROM gains and acceptable usability/safety, but not definitive efficacy.
- Support: p.1 reports 5.88% and 11.11% median PROM/AROM increases, no major adverse event, and no statistical significance versus therapist goniometer comparison
- Confidence: high

## Clean Takeaway

- `I-Phlex 2024` is the practical clinical companion to the 2023 mechanism paper: same MCP-centered logic, but now tested as a usable pilot rehabilitation tool.

## Next Action

- Keep this paired with the 2023 paper whenever presenting `I-Phlex`.
- If needed later, extract the exact exercise block diagram and ROM protocol for validation planning.
