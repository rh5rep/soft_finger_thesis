# Exo-Glove Poly II: A Polymer-Based Soft Wearable Robot for the Hand with a Tendon-Driven Actuation System

## Metadata

- Paper ID: `DOI:10.1089/soro.2018.0006`
- Zotero key: `AK9DKBWB`
- Topic: ``
- Status: `inbox`
- Priority: `medium`
- Source: `zotero`
- Year: `2019`
- Venue: Soft Robotics
- Authors: Brian Byunghyun Kang; Hyungmin Choi; Haemin Lee; Kyu-Jin Cho
- DOI: 10.1089/soro.2018.0006
- URL: https://journals.sagepub.com/doi/10.1089/soro.2018.0006
- PDF status: `attached`
- PDF path: /Users/rami/Zotero/storage/VFJB322I/Kang et al. - 2019 - Exo-Glove Poly II A Polymer-Based Soft Wearable Robot for the Hand with a Tendon-Driven Actuation S.pdf
- Zotero open link: zotero://select/library/items/VFJB322I

## Audit Status

- Reading stage: screened for mechanism/model relevance
- Source verification: checked against attached PDF text and publisher page
- Exact quotes logged: no
- Last audited: 2026-04-20
- Used in: docs/TOPIC_MEMOS/11_tendon_routing_and_ring_placement.md

## Why This Paper Is In The Queue

This is a direct precedent for the current thimble, passive thumb, tendon-routing, and actuator-slack questions. Its main value for the thesis is not the full glove architecture, but the way it converts tendon routing into a single-finger kinematic model that predicts required flexion/extension wire lengths and actuator slack across hand sizes.

## Citation / Bibliographic Notes

- Title: Exo-Glove Poly II: A Polymer-Based Soft Wearable Robot for the Hand with a Tendon-Driven Actuation System
- Authors: Brian Byunghyun Kang; Hyungmin Choi; Haemin Lee; Kyu-Jin Cho
- Venue: Soft Robotics
- Year: 2019
- DOI: 10.1089/soro.2018.0006
- URL: https://journals.sagepub.com/doi/10.1089/soro.2018.0006
- Tracker question: 

## Classification

- Type: journalArticle
- Topic: tendon routing and ring placement
- Actuation type: tendon-driven soft wearable hand robot
- Model type: single-finger kinematic wire-length and actuator-slack model
- Validation type: grasping experiments with SCI participants and underactuation tests with healthy subjects

## Source-Verified Summary

- Exo-Glove Poly II is a polymer-based soft wearable hand robot intended to restore pinch and grasp for people with spinal cord injury.
- The glove uses tendon-driven actuation for index and middle finger flexion/extension and a passive thumb structure to oppose the thumb.
- The design reduced the glove to fewer polymer components, including a body, passive thumb structure, and thimbles.
- Finger straps and thimble tendon paths are important because they define flexion wire path, moment arm behavior, and torque transmission.
- The paper includes a simplified one-finger kinematic model that predicts required flexion and extension wire-length changes from finger posture.
- The kinematic model is used to optimize pulley radius ratio and initial extension-wire slack so the antagonistic single-actuator system avoids slack and singularity problems across the tested hand sizes.

## One-Sentence Thesis Relevance

- This paper is the closest current precedent for modeling how thimble anchoring, intermediate tendon guides, hand-size parameters, pulley geometry, and actuator slack interact in a soft tendon-driven finger system.

## Core Definitions (Only From Source)

- Term:
  - Definition:
  - Support:

## Main Claims (Only From Source)

- Claim: Tendon path design is essential in tendon-driven soft wearable hand robots.
  - Explanation: The paper links tendon path design to target motion generation, friction, fatigue, robustness, and repeated actuation.
  - Support: Discussion section and kinematic model section of attached PDF.
- Claim: A passive thumb structure can improve grasping posture while reducing actuator count.
  - Explanation: The passive thumb structure opposes the thumb and allows Exo-Glove Poly II to use one actuator rather than separately actuating the thumb.
  - Support: Abstract and Design and Features section of attached PDF.
- Claim: Slack and singularity behavior must be explicitly considered when flexion and extension wires are antagonistically connected to one actuator.
  - Explanation: The model estimates required wire lengths and actuator-side wire lengths, then chooses pulley geometry and initial slack to avoid singular points and reduce operation time.
  - Support: Kinematic Model of EGP II section of attached PDF.

## Key Quotes (Only When Wording Matters)

- Quote:
  - Page:
  - Why wording matters:

## Mechanistic Insights (From Paper)

- Mechanism: Distal thimble as anchor and tendon-path element.
  - Description: The thimble fixes the glove to the fingertip, forms wire paths for flexion and extension, and increases friction with grasped objects while needing to remain thin enough not to interfere with grasping.
  - Support: Design and Features section of attached PDF.
- Mechanism: Finger straps as moment-arm-defining tendon guides.
  - Description: The finger body connects the dorsal body to the thimble, while straps on the side of the finger body determine flexion moment arm length for the joints.
  - Support: Body subsection of attached PDF.
- Mechanism: Kinematic wire-length model.
  - Description: The model treats the phalanges as rectangular segments with MCP/PIP/DIP joint angles and guide/strap points; changing posture changes the flexion and extension wire path lengths.
  - Support: Kinematic Model of EGP II section of attached PDF.

## Observations / Results (From Paper)

- Finding:
  - Description:
  - Support:

## What This Paper Suggests (Project Interpretation)

- Interpretation: The thesis can borrow the kinematic structure without borrowing the full glove.
  - Why it matters: A simplified index-finger model with movable guide points and a thimble can answer the current routing question before a full sleeve/glove design is chosen.
- Interpretation: Slack is a design variable, not an afterthought.
  - Why it matters: If the prototype uses tendon return, antagonistic routing, or series compliance, the model should track tendon stroke and slack from the beginning.
- Interpretation: Passive thumb support is a defensible first step.
  - Why it matters: It allows pinch-like evaluation while keeping the active modeling problem focused on the index finger.

## Model / Mechanism / Validation Details

- System type: polymer soft wearable hand robot
- Actuation type: tendon-driven, single actuator with underactuation and dual-slack enabling mechanism
- Model type: planar single-finger kinematic path-length model
- Validation setup: object grasping experiments with SCI subjects; underactuation tests with healthy subjects
- Main metrics: required flexion/extension wire lengths, pulley radius ratio, initial slack, singularity avoidance, grasping performance, object normal force in underactuation testing

## What Matters For This Thesis

- Use thimble anchoring as a geometric input to the model.
- Treat ring/strap positions as tendon guide points that define moment arms.
- Compare hand-size/finger-length variants using normalized guide positions.
- Track tendon stroke and slack explicitly.
- Keep a passive thumb pad or passive thumb support as the first pinch-contact option.

## Relevance To Finger Tapping / Thesis

- Direct relevance: strong for tendon routing, thimble anchoring, passive thumb opposition, and kinematic wire-length modeling.
- Indirect relevance: the paper targets grasp/pinch assistance for SCI, not Parkinson finger tapping or a simplified single-index validation rig.

## Control-System Interpretation (Project Interpretation)

- Controller:
- Plant:
- Feedback:
- Reference:
- Notes:

## Exact Quotes / Evidence Bank

- Quote:
- Page:
- Section or figure:
- Why it matters:
- Reusable in:

## Claims Safe To Reuse Later

- Claim:
- Support:
- Confidence:

## What This Paper Does Not Answer

- Gap: It does not directly optimize removable ring count for a single-index-finger mock-up.
- Gap: It does not provide a thesis-ready passive human finger stiffness model.
- Gap: It targets ADL grasping rather than tapping-like repeated flexion/extension.
- Gap: It does not isolate fingertip force and curvature sensitivity to ring placement in the way the current thesis simulation needs.

## Open Questions

- How many intermediate guides are needed before the routing gives acceptable MCP/PIP/DIP angle distribution?
- Can a lateral or palmar-lateral ring path preserve enough palmar clearance for pinch/tapping contact?
- Should the first passive thumb interface be a fixed pad, a reshaped passive thumb splint, or no thumb component?
- How much of Exo-Glove Poly II's slack analysis matters if this thesis uses one flexion tendon plus passive return instead of an antagonistic single-pulley system?

## Limitations

- Full paper note still needs page-level exact quote extraction before use in thesis prose.
- Current screening focused on mechanism/model relevance, not clinical results or detailed manufacturing.

## Tags

- tendon-routing
- thimble
- passive-thumb
- kinematic-model
- actuator-slack
- soft-glove

## Decision Impact

- Which memo or decision this should affect: tendon routing/ring placement model; first prototype architecture decision
- What it changes: supports modeling the thimble, guide/ring points, tendon stroke, and slack before choosing the prototype routing.

## Next Action

Extract the kinematic model equations into a small Python routing sandbox and compare two-ring, three-ring, and thimble-only index-finger tendon paths.
