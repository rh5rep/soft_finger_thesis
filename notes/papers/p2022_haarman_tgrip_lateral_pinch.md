# Design and feasibility of the T-GRIP thumb exoskeleton to support the lateral pinch grasp of spinal cord injury patients

## Metadata

- Paper ID: `DOI:10.1109/ICORR55369.2022.9896595`
- Zotero key: `PL9BWHHV`
- Topic: `T007`
- Status: `shortlist`
- Priority: `high`
- Source: `manual`
- Year: `2022`
- Venue: IEEE International Conference on Rehabilitation Robotics
- Authors: Claudia J. W. Haarman; Edsko E. G. Hekman; Ellen M. Maas; Johan S. Rietman; Herman van der Kooij
- DOI: 10.1109/ICORR55369.2022.9896595
- URL: https://pubmed.ncbi.nlm.nih.gov/36176123/
- PDF status: `missing in repo`
- PDF path: _not attached_
- Zotero open link: _missing_

## Why This Paper Is In The Queue

Strong comparison paper because it is a very lightweight, clearly specified `thumb-only` exoskeleton aimed at restoring `lateral pinch grasp`.

## Citation / Bibliographic Notes

- Title: Design and feasibility of the T-GRIP thumb exoskeleton to support the lateral pinch grasp of spinal cord injury patients
- Authors: Claudia J. W. Haarman; Edsko E. G. Hekman; Ellen M. Maas; Johan S. Rietman; Herman van der Kooij
- Venue: IEEE International Conference on Rehabilitation Robotics
- Year: 2022
- DOI: 10.1109/ICORR55369.2022.9896595
- URL: https://pubmed.ncbi.nlm.nih.gov/36176123/
- Tracker question: Which current technologies support thumb-index opposition or lateral pinch and how do they work?

## Abstract / Summary

- This paper presents `T-GRIP`, a robotic `thumb exoskeleton` to support the `lateral pinch grasp`.
- The target population is `cervical spinal cord injury` patients with impaired hand function.
- The design philosophy is minimalist:
  - restore a highly useful grasp
  - actuate only `one degree of freedom`
  - keep hardware light and wearable
- This makes it a good counterexample to more complex multi-finger exoskeletons.

## Model / Mechanism / Validation Details

- System type: `thumb exoskeleton` for assistive lateral pinch
- Motion focus:
  - lateral pinch
  - thumb flexion toward the side of the index finger
- Actuation:
  - `electric micro linear actuator`
  - manufacturer listed as `Actuonix Motion Devices`
  - actuator weight about `15 g`
  - `20 mm` stroke
  - maximum force about `40 N`
- Mechanical architecture:
  - actuator mounted on a `thermoplastic hand bracket`
  - actuator positioned on the `dorsal side of the hand`
  - actuator pushes on a `lever arm`
  - lever arm rotates about a pivot and moves a `thumb ring`
  - thumb ring design prevents distal thumb hyperextension
- Size / mass:
  - hand-mounted part about `50 g`
  - maximum height above the hand about `40 mm`
- Additional hardware:
  - optional bracket can stabilize the index finger in a flexed position if needed
- Kinematic / force logic:
  - mechanism modeled to estimate `thumb range of motion` and `pinch force`
  - key design variable is lever-arm ratio `(l1 / l2)`
  - decreasing lever-arm ratio increases ROM and allows grasp of smaller objects, but reduces peak pinch force
- Control:
  - thumb movement controlled via `contralateral wrist rotation`
  - programmable smartwatch on the opposite wrist measures pronation/supination
  - smartwatch communicates over `Bluetooth Low Energy`
  - discrete state machine on `ESP32`
  - `wrist pronation` triggers thumb flexion
  - `wrist supination` triggers thumb extension
  - neutral wrist stops the motor

## Validation Setup

- Feasibility study with `3 tetraplegic SCI patients`
- Main outcomes:
  - pinch force
  - `Grasp and Release Test`
  - `D-QUEST` satisfaction questionnaire

## Main Metrics / Results

- Achieved grip force about `7 N`
- Overall performance during the `Grasp and Release Test` was better `with T-GRIP than without device`
- The paper positions the device as a promising assistive option achieved with only `one actuated DOF`

## What Matters For This Thesis

- This is one of the clearest examples of a `thumb-index task-specific` assistive device with very little hardware.
- Useful for:
  - minimalist actuation strategy
  - thumb-side mechanism design
  - thinking about how much function can be recovered with a `single actuated DOF`
- It helps show that `pinch/opposition` devices are already quite mature as a category compared with tapping-specific devices.

## Limitations

- SCI-specific, not Parkinson-specific.
- Lateral pinch task, not tapping task.
- Focused on functional assistive grasp, not repetitive movement training.
- Not a soft variable-stiffness device.
- Primarily a conference feasibility paper, not a large mature clinical study.

## Decision Impact

- Keep as a `comparison-only` paper in the pinch/opposition bucket.
- Use it to show that the hardware literature is richer when the task is a grasp task.
- Do not treat it as a tapping precedent.

## Quotes / Data To Reuse Later

- Lightweight `50 g` robotic thumb exoskeleton for lateral pinch.
- Micro linear actuator mounted on dorsal side of the hand.
- One actuated DOF only.
- Controlled through contralateral wrist rotation.
- Approximate grip force `7 N`.

## Clean Takeaway

- `T-GRIP 2022` is a strong example of minimalist task-specific thumb-assist hardware, but it belongs firmly in the `pinch/opposition comparison` category, not the tapping category.

## Next Action

- Keep as the main `thumb-only` comparison device in the notes.
- If needed later, add the full PDF to Zotero / repo notes for figure extraction.
