# Meeting Prep 2026-04-11

## Purpose

Align with Silvia on how to frame the meeting with `Bo Biering-Sørensen` so it supports the thesis directly.

The goal is `not` to turn the thesis into a broad Parkinson rehabilitation or neuroplasticity project. The goal is to use Bo's clinical perspective to sharpen:

- which finger-tapping features matter clinically
- which outputs are worth preserving in a simplified engineering model
- what would make the work clinically credible without overclaiming

## Thesis Frame To Keep Fixed

- The thesis is a `simulation-first, simplified finger-actuator study`.
- `Parkinson finger tapping` is mainly the `task-definition and output-definition lens`.
- The core engineering focus remains:
  - reduced-order modeling
  - controllability
  - biomechanical interaction
  - benchtop validation
- The thesis is `not` a clinical efficacy study.
- The thesis does `not` aim to prove neuroplasticity.

## Why Meeting Bo Is Useful

Bo appears relevant mainly as a `movement-disorders clinical anchor`, not as a mechanical design source.

The meeting should help answer:

- what clinicians actually look for during finger tapping
- where bedside assessment is strong or weak
- whether granular decomposition of tapping features is clinically useful
- which measured outputs would matter if a simplified finger system is later extended

## Main Alignment Question For Silvia

Does she agree that the Bo meeting should be framed primarily as:

`clinical grounding for task definition, output selection, and translational relevance`

rather than as:

- mechanism design advice
- proof of rehabilitation efficacy
- a broad discussion of Parkinson neuroplasticity

## Recommended 5 Questions For Bo

1. In your clinical practice, when you assess finger tapping in Parkinson's disease, which features are most informative to you: slowness, reduced amplitude, rhythm irregularity or halts, sequence effect, asymmetry, or something else?
2. How standardized is finger-tapping assessment in real practice, and where do you see the biggest limitations or sources of variability in bedside scoring?
3. Do you find it clinically useful to separate finger tapping into distinct components like slowness, amplitude reduction, irregularity, and sequence effect, or is that too granular for everyday use?
4. For a simplified engineering thesis like mine, which outputs would actually be clinically meaningful: range of motion, tapping amplitude, cycle timing, rhythm irregularity, decrement over repeated taps, force or torque, or only a smaller subset?
5. If a finger-focused system were to become clinically meaningful later, what would make it valuable in the broader Parkinson rehabilitation context rather than just as an isolated hand device?

## Slide-Deck Core Questions

Dedicated speaking script:
[2026-04-15_bo_meeting_presentation_script.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/notes/Meetings/2026-04-15_bo_meeting_presentation_script.md)

Use these as the visible slide questions so the meeting stays focused:

1. Which finger-tapping features are most informative in practice?
2. Have you seen external cues help with Parkinson movement tasks?
3. If you could improve one Parkinson assessment or rehabilitation tool, what would you want it to capture or change?
4. Have you seen hand or finger rehabilitation devices used clinically?

## Supplementary Prompts

Keep these for follow-up conversation if the discussion naturally opens:

- How standardized is bedside finger-tapping assessment, and where does variability enter?
- Is it useful to separate tapping into components, or is that too granular for clinical use?
- Which prototype outputs would be most meaningful: range of motion, tapping amplitude, timing, irregularity, decrement, force, torque, or stiffness?
- Would a finger-focused setup be most useful for assessment, assistance, training, or stabilization?

## One Backup Question

If Silvia wants one broader rehabilitation question, use this:

How do you think about `functional improvement` versus `compensation` in Parkinson rehabilitation, and where could a finger-focused system realistically contribute?

This is better than leading with `neuroplasticity`, which is easy to overstate relative to thesis scope.

## Questions To Avoid Leading With

- "Can this thesis improve neuroplasticity?"
- "Should I build a full rehabilitation device?"
- "What is the best actuator architecture?"
- "Can finger tapping become a clinical intervention in this thesis?"

These either exceed scope or invite answers that the current thesis cannot support directly.

## Desired Outcome From The Supervisor Meeting

- Confirm the `purpose` of the Bo meeting
- Confirm the `5-question shortlist`
- Decide whether to keep the discussion tightly on `finger tapping and clinically meaningful outputs` or allow one broader Parkinson rehabilitation question
- Make sure the meeting supports the proposal's current scope rather than widening it

## Suggested Background Slide For Bo

Draft slide artifact:
[bo_background_context_slide.html](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/presentation_assets/bo_background_context_slide.html)

### Slide Title

`Thesis Context`

### On-Slide Text

- `MSc thesis on a simplified soft variable-stiffness finger actuation system`
- current focus: `simulation-first reduced-order finger-actuator model`
- target questions:
  - how stiffness affects `controllability`
  - how the actuator interacts with a simplified finger model
  - what should later be validated on a `bench-top prototype`
- `Parkinson finger tapping` is being used mainly as a `task-definition and output-definition lens`
- the thesis is `not`:
  - a clinical efficacy study
  - a full wearable glove project
  - a broad neuroplasticity project

### What To Say

`The project is an engineering thesis, not a clinical trial. I am trying to build a simplified finger-actuator model and later a bench-top prototype, and I am using Parkinson finger tapping mainly to understand which movement features and outputs are clinically meaningful enough to preserve in that simplified model.`

### Why This Slide Helps

- it gives Bo the minimum context needed to answer at the right level
- it reduces the risk of the discussion widening too early
- it makes clear that the main input sought is about `clinically meaningful outputs`, not detailed mechanism design
