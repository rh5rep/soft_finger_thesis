# A hand exoskeleton with linear motors (HELM) for pathological tremor suppression of fingers

## Metadata

- Paper ID: `DOI:10.1016/j.ish.2025.03.002`
- Zotero key: `MYYMFLDA`
- Topic: `T009`
- Status: `screening`
- Priority: `high`
- Source: `manual`
- Year: `2025`
- Venue: Intelligent Sports and Health
- Authors: Andong Yi; Bin Zhang; Nathan Lau; Dingguo Zhang
- DOI: 10.1016/j.ish.2025.03.002
- URL: https://linkinghub.elsevier.com/retrieve/pii/S3050544525000179
- PDF status: `attached`
- PDF path: /Users/rami/Zotero/storage/QYWC3BU6/Yi et al. - 2025 - A hand exoskeleton with linear motors (HELM) for pathological tremor suppression of fingers.pdf
- Zotero open link: zotero://select/library/items/QYWC3BU6

## Audit Status

- Reading stage: extracted
- Source verification: not fully checked against PDF
- Exact quotes logged: no
- Last audited: 2026-04-06
- Used in:

## Why This Paper Is In The Queue

This is the clearest paper so far for the "keep the finger steady" part of the supervisors' description.

## Citation / Bibliographic Notes

- Title: A hand exoskeleton with linear motors (HELM) for pathological tremor suppression of fingers
- Authors: Andong Yi; Bin Zhang; Nathan Lau; Dingguo Zhang
- Venue: Intelligent Sports and Health
- Year: 2025
- DOI: 10.1016/j.ish.2025.03.002
- URL: https://linkinghub.elsevier.com/retrieve/pii/S3050544525000179
- Tracker question: Do there exist hand or finger exoskeletons that actively or passively steady finger motion rather than only mobilizing it?

## Abstract / Summary

- This paper presents HELM, a wearable hand exoskeleton developed specifically for pathological finger tremor suppression.
- The device uses five lightweight linear motors, one per finger, and works in a passive mode to hold desired finger positions and resist tremulous disturbances.
- Validation targeted posture tremor rather than kinetic tremor and was performed on two healthy subjects with simulated tremor and one Parkinson's patient with actual finger tremor.
- Reported tremor reduction was greater than 80 percent and 90 percent for the two healthy subjects and greater than 70 percent for the Parkinson's patient.
- The paper is important because it directly addresses finger steadiness, which the MCP and index-finger rehabilitation exoskeleton papers do not.

## Model / Mechanism / Validation Details

- System type: five-finger hand exoskeleton for pathological tremor suppression
- Actuation type: one miniature linear motor per finger with passive mode for tremor suppression and active mode for finger motion / grasp assistance
- Model type: rigid-link / connecting-rod hand exoskeleton with linear-actuator drive and position feedback; emphasis is on prototype design and performance testing rather than joint-level biomechanical modeling
- Validation setup: active-mode performance tests for force, grasp, and trajectory tracking; passive-mode tremor suppression tests on two healthy subjects and one Parkinson's patient
- Main metrics: percentage tremor reduction, fingertip force, grip force, grasp capability, and trajectory-tracking behavior

## What Matters For This Thesis

- This is the best current paper in the shortlist for the "steadying" or tremor-suppression angle.
- Unlike the MCP and index-finger papers, it is not mainly about self-alignment or rehabilitation ROM; it is about attenuating involuntary oscillatory finger motion.
- It broadens the review by showing that the literature splits into at least two hardware intentions: assist / mobilize motion versus suppress unwanted motion.
- It also suggests that if your supervisors mean "support the patient in movement" in a steadiness sense, then tremor-management exoskeletons deserve their own category rather than being folded into tapping or pinch papers.

## Limitations

- The device targets posture tremor, not the clinical finger-tapping task.
- It is a five-finger exoskeleton rather than a simplified single-finger system.
- Validation is still very limited: only two healthy subjects and one Parkinson's patient.
- The passive suppression mode holds finger position and suppresses disturbances, which is different from enabling fast voluntary tapping.

## Decision Impact

- Keep this paper in the core review set as the clearest tremor / steadiness precedent.
- Use it to justify a separate presentation category for tremor suppression or movement stabilization devices.
- Do not confuse this paper with tapping-like repetitive-motion assistance; it solves a different problem.

## Quotes / Data To Reuse Later

- The prototype weighs about 213 g for the main body.
- This is presented as the first study to accomplish tremor suppression for five fingers with a hand exoskeleton.
- Average tremor reduction was reported above 80 percent and 90 percent in the two healthy-subject experiments and above 70 percent in the Parkinson's patient.
- The passive mode is suitable for posture and rest tremors, but not kinetic tremor, because voluntary motion is also resisted.

## Next Action

Add to Zotero and decide whether the presentation should separate `movement assistance` from `tremor suppression / stabilization` as two distinct hardware buckets.
