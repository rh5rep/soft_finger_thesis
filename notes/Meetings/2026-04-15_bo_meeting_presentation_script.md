# Bo Meeting Presentation Script 2026-04-15

## Purpose

Use this as a short speaking guide for the clinical-input meeting.

The goal is to keep the discussion focused on:

- clinically meaningful finger-tapping features
- outputs worth preserving in a simplified engineering model
- practical experience with Parkinson assessment or rehabilitation tools

The goal is not to ask for mechanism design advice, clinical validation, or treatment claims.

## Core Slide Questions

1. Which finger-tapping features are most informative in practice?
2. Have you seen external cues help with Parkinson movement tasks?
3. If you could improve one Parkinson assessment or rehabilitation tool, what would you want it to capture or change?
4. Have you seen hand or finger rehabilitation devices used clinically?

## Opening

`Thanks for meeting with me. I am not trying to ask you to design the device or validate the engineering. I mainly want clinical perspective on which movement features are worth preserving and measuring in a simplified finger-actuator model.`

## Slide 1: Project Context

Say:

`My thesis is an engineering project: a simplified soft variable-stiffness finger actuator, first modeled in simulation and later checked with a benchtop prototype. Parkinson finger tapping is useful here as a clinical task lens, because it gives concrete movement features like slowness, amplitude reduction, irregularity, halts, and sequence effect.`

Keep in mind:

- do not imply this is a patient-ready device
- do not claim clinical efficacy
- emphasize that the goal is choosing meaningful outputs, not proving treatment benefit

## Slide 2: Clinical Features


The first thing I want to understand is what matters when you actually watch or score finger tapping. Some features are easy for me to measure technically, but I do not want to optimize for variables that are not clinically meaningful.`

Possible follow-up:

If you had to pick only two or three features to preserve in a simplified system, which would they be?`

## Slide 3: Outputs And Rehabilitation Context


The second part is broader. If this kind of finger-focused setup were useful later, I want to understand whether its value would be closer to assessment, training, assistance, or something else. I am also interested in whether you have seen hand or finger rehab devices in practice, and what tends to be useful or limiting.`

Possible follow-up:

For a benchtop prototype, I could measure things like angle, timing, amplitude, force, torque, and stiffness. I am trying to decide which of those are worth prioritizing.`

## Closing

The main thing I hope to leave with is a smaller set of clinically grounded outputs that I can use to keep the model and validation focused.`


## Supplementary Prompts


- How standardized is bedside finger-tapping assessment, and where does variability enter?
- Is it useful to separate tapping into components, or is that too granular for clinical use?
- Which prototype outputs would be most meaningful: range of motion, tapping amplitude, timing, irregularity, decrement, force, torque, or stiffness?
- Would a finger-focused setup be most useful for assessment, assistance, training, or stabilization?

## Post-Meeting Debrief 2026-04-17

Source: reconstructed from handwritten meeting notes and later verbal read-back. Several handwritten fragments were unclear, so this section captures the coherent meeting substance rather than a literal OCR transcript.

### Cleaned Notes

- Bo's input supports keeping the thesis framed around clinically observable movement features and objective assessment, not around mechanism design or clinical efficacy.
- Finger tapping and hand gripping are useful because they are fast repeated movements that expose Parkinson-related motor features.
- Parkinson finger tapping should not be treated as a single speed variable. Relevant observable features include rigidity, slowness, tremor, bradykinesia, amplitude, timing/rhythm, decrement across repetitions, fatigue, irregularity, and halts.
- Parkinson's disease can include or develop other movement disorders. Dystonia was mentioned as one example, so the thesis should avoid assuming that every abnormal finger movement has the same cause.
- Bradykinesia is usually assessed repeatedly in clinic and ranked on a scale. A key open problem is how to assess bradykinesia more objectively and properly.
- A general population baseline is not enough. Assessment should use a baseline per patient and then compare that patient over time.
- Variability and confounding factors matter. Possible contributors include arthritis, lack of strength, reduced perception or sensation, diabetes, natural severity grade, cerebral problems or changes, and other slow-movement causes.
- The relevant clinical question is: which comorbidities or coexisting impairments will affect the outcome?
- Light sensory input or "placebo-like" assistance can sometimes allow fuller movement. The example discussed was lightly pressing on someone's arm during a downward movement and seeing the movement complete more fully. This should be interpreted cautiously as sensory cueing or facilitation, not as proof that assistance alone solves the motor problem.
- Sensory input during the activity can be helpful. External cues can help with movement tasks, even though cueing is not used heavily in all clinical contexts.
- Freezing of gait was discussed as a cueing example: laser lines or beams projected on the floor or out a doorway can help some patients initiate walking.
- Another cueing example was cycling: some patients can bike normally even when they cannot walk normally.
- Music and dancing can also change movement performance. Patients may feel or move much better when dancing with music than during uncued movement.
- Participants in rehabilitation do not necessarily get better in the sense of reversing Parkinson's disease, but activity and rehabilitation may help them deteriorate more slowly in motor symptoms.
- Neurorehabilitation in Parkinson's disease is different from neurorehabilitation after stroke. Stroke is often a one-time injury, whereas Parkinson's is neurodegenerative, so "rehabilitation" should not be framed as the same kind of recovery mechanism.
- Patient movement is critical, and objective assessment is crucial.
- Patient-centered input matters. Bo emphasized that clinicians and engineers can ask many technical questions, but what is actually helpful depends on what patients experience and want. Workshops with patients or patient/caregiver groups can be useful for this.
- Rapid alternating movements are relevant to better assessment and should remain in the clinical task vocabulary.
- REM behavior disorder was mentioned as an important early or prodromal marker in Parkinson's disease.
- Lewy bodies, alpha-synuclein, gut/brain involvement, constipation, and reduced sense of smell were mentioned as disease-background concepts. These are useful clinical context but not direct drivers of the current finger-actuator model.

### Thesis Implications

- Keep `Parkinson finger tapping` as the task-definition and output-selection lens.
- Use clinical features to justify what the simulation and bench-top setup should measure, especially amplitude, timing, decrement, irregularity, and halts.
- If the thesis includes an assessment angle, frame it around patient-specific baseline tracking rather than one universal normal baseline.
- Treat force, torque, stiffness, or sensory input as engineering interaction variables, not as direct clinical improvement claims.
- Avoid claiming that the system treats Parkinson's disease, reverses symptoms, or proves neurorehabilitation benefit.
- In the model and validation plan, prioritize interpretable repeated-motion outputs before adding more complex actuator, cueing, or sensing claims.
- Keep cueing, sensory facilitation, music/dance, cycling, and freezing-of-gait examples as clinical analogies or future-work context unless the thesis explicitly adds a cueing experiment.

### Open Questions

- Which patient subgroup or symptom profile is the most defensible clinical reference point for this project: early-stage bradykinesia, prominent sequence effect, tremor, dystonia, or general impaired finger control?
- Which comorbidities or coexisting impairments should be explicitly excluded or controlled for in a future study design?
- Should `steady finger` be interpreted as a tremor/stabilization issue, a rigidity issue, or should the thesis stay focused on repetitive tapping and bradykinesia-related motion features?
- If sensory input, biofeedback, or external cueing stays in the background, should it be mentioned only as future work or as a comparison category in the literature review?
- Should patient-centered interviews or workshops be mentioned as future translational work, separate from the bench-top validation?

### Limitations Of This Debrief

- The original notes were handwritten and partly illegible. The later verbal read-back clarified several items, but exact wording and some examples should still be confirmed before being used in formal writing.
- The note about patient or caregiver workshops should be confirmed, because the handwritten/read-back wording was ambiguous.
- This debrief should be used as supervisor-meeting context, not as citable clinical evidence.



One thing is moving the finger another is moving all the joints

the 9 ball game


we need to undetstand what we are targeting once we have a design

if we are able to keep it as simple as possible:

a table where we have accessibility, feasibility, then you end up iwht a design adn propose different use cases 


once we have a design, we can show them, and see what htey think
- this will help this group of patients 
- other design will help for patients 


if considering opensim 
- samuela is working on that 
- and phillip is doing the design of the actuator and cad 



compile a list of things for the erasmus students to get briefed on 
- may -  july
- context for me with the colleagues 
