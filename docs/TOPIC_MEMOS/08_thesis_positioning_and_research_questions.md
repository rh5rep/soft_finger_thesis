# Thesis Positioning and Candidate Research Questions

## Question

What is the most coherent current umbrella for the thesis, given the project brief, the reviewed literature, the broader Parkinson device landscape, and the strongest direct papers captured so far?

## Current Umbrella

The thesis is best understood as a `simulation-first, simplified finger-actuator study` that uses `Parkinson-relevant repetitive finger motion` as its strongest current task-framing layer without turning the project into a full clinical Parkinson device program.

In practical terms, the current umbrella is:

- `core engineering problem`
  - model and validate how a soft variable-stiffness actuator interacts with a simplified finger system
- `current task framing`
  - repetitive voluntary finger motion, especially Parkinson finger tapping and its related deficit structure
- `closest mechanical precedents`
  - near-adjacent index-finger and MCP exoskeletons rather than direct Parkinson tapping-assist devices
- `strongest direct literature`
  - Parkinson finger-tapping assessment, symptom decomposition, and task-level measurement systems
- `validation style`
  - benchtop and simulation validation, not clinical efficacy claims

This makes the thesis narrower and more defensible than:

- a full hand glove project
- a generic Parkinson technology survey
- a sensing-led project
- a clinical intervention study

## Current Thesis Understanding

The repo evidence currently supports the following thesis interpretation:

- The project is not primarily about building a wearable clinical device.
- The project is about identifying a tractable finger-actuator abstraction that is rich enough to study controllability and biomechanical interaction, but simple enough to model and validate within thesis scope.
- Parkinson's disease remains useful because it gives a strong symptom and task context for repetitive finger motion, especially through bradykinesia, reduced amplitude, sequence effect, and tapping-task irregularity.
- The direct Parkinson literature does not yet provide strong tapping-assist hardware precedents. Instead, it provides a strong `task-definition and measurement layer`.
- The best hardware precedents so far come from `near-adjacent finger and MCP exoskeletons`, not from direct Parkinson finger-tapping exoskeleton papers.

## What The Literature Now Says Most Clearly

### 1. Parkinson finger tapping is useful as a task definition

The strongest direct papers indicate that finger tapping is not just `tap faster or slower`.

- `Bologna 2020` and `Paparella 2026` show that bradykinesia should not be treated as one scalar slowness variable.
- `Zarrat 2026` shows that the task can be decomposed into clinically meaningful motor-characteristic families and measured through a task-level signal.
- `Amo-Salas 2024` and `Ravichandran 2023` show that the direct task literature is rich in assessment technology, including home or wearable measurement settings.

### 2. The direct assistive-hardware literature is sparse

The literature review so far has not produced a strong bucket of `Parkinson finger-tapping assistive exoskeleton` papers.

That absence is itself a result:

- direct Parkinson tapping assistance appears weakly represented
- direct Parkinson tapping assessment appears strongly represented
- the closest hardware bridge therefore comes from non-Parkinson or near-adjacent repetitive finger-motion devices

### 3. MCP and index-finger exoskeletons are the strongest hardware bridge

The current closest mechanical precedents are:

- `Sun 2021` for richer index-finger kinematics
- `Peperoni 2023` for MCP-dominant self-aligning architecture and joint-level estimation
- `Peperoni 2024` for a clinical pilot built on the same MCP-centered device line

These papers do not solve the Parkinson task directly, but they provide the clearest bridge to a simplified actuator-finger mechanism.

### 4. Task-level observables may be enough for a first thesis model

The Parkinson tapping papers do not insist on a full anatomical or joint-level representation.

Instead, the strongest current assessment anchor, `Zarrat 2026`, shows that clinically meaningful structure can be extracted from:

- thumb-index distance
- cycle timing
- speed-related observables
- variability
- interruptions
- decrement over repeated cycles

This supports a thesis strategy in which:

- the first model is reduced-order and interpretable
- validation uses task-level outputs that matter clinically
- higher-fidelity anatomy remains secondary unless later evidence makes it necessary

## Most Useful Papers Right Now

### A. Core Parkinson task-framing papers

- [p2020_bologna_bradykinesia_concepts.md](../notes/papers/p2020_bologna_bradykinesia_concepts.md)
- [p2026_paparella_bradykinesia_complex.md](../notes/papers/p2026_paparella_bradykinesia_complex.md)

Why these matter:

- they define the conceptual problem correctly
- they justify separating slowness, reduced amplitude, sequence effect, and related irregularities
- they stop the thesis from collapsing Parkinson finger motion into one vague deficit label

### B. Core direct finger-tapping papers

- [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)
- [p2024_amo_salas_pd_ft_survey.md](../notes/papers/p2024_amo_salas_pd_ft_survey.md)
- [p2023_ravichandran_itex_gloves.md](../notes/papers/p2023_ravichandran_itex_gloves.md)

Why these matter:

- they define what the direct finger-tapping task literature actually measures
- they show that the task is strongest on assessment and measurement, not direct actuation
- they provide realistic signal, sensing, and home-use framing

### C. Core hardware bridge papers

- [p2021_sun_self_aligning_index_finger.md](../notes/papers/p2021_sun_self_aligning_index_finger.md)
- [p2023_peperoni_self_aligning_mcp.md](../notes/papers/p2023_peperoni_self_aligning_mcp.md)
- [p2024_peperoni_iphlex_mcp.md](../notes/papers/p2024_peperoni_iphlex_mcp.md)

Why these matter:

- they are the strongest current mechanical analogs for repetitive finger motion
- they help justify simplified MCP-dominant or index-finger abstractions
- they provide real design, estimation, and validation patterns for benchtop-oriented work

### D. Broader Parkinson positioning papers

- [07_parkinsons_assistive_control_devices.md](07_parkinsons_assistive_control_devices.md)
- [p2025_andong_helm_tremor.md](../notes/papers/p2025_andong_helm_tremor.md)
- [p2022_raciti_bradykinesia_exoskeleton_trial.md](../notes/papers/p2022_raciti_bradykinesia_exoskeleton_trial.md)

Why these matter:

- they sharpen the distinction between assistance, stabilization, and assessment
- they help position the thesis in the wider Parkinson device landscape without forcing the project to imitate gait or DBS literatures

## What You Have Learned

### About the thesis itself

- The thesis is currently strongest when framed as `simplified actuator-finger interaction` rather than `full rehabilitation product development`.
- A reduced-order model is not a compromise anymore; it is becoming the right first step.
- Variable stiffness remains central, but it must be tied to a concrete question about controllability or interaction, not treated as an abstract feature.

### About Parkinson framing

- Parkinson remains a useful framing choice, but mainly because it gives:
  - a strong repetitive-motion task
  - a meaningful symptom vocabulary
  - clinically interpretable outputs
- Parkinson does not currently give you a rich direct hardware precedent library for finger tapping.

### About the literature surface

- Finger tapping is treated much more often as an `assessment task` than as an `assistive movement target`.
- There is a real literature split between:
  - `assist movement`
  - `suppress unwanted motion`
  - `measure or quantify task performance`
- These should not be collapsed into a single device goal.

### About modeling and validation

- The first useful outputs are likely task-level observables, not full anatomical state reconstruction.
- Good validation metrics may include:
  - achieved amplitude
  - cycle timing
  - speed-related outputs
  - repeatability
  - variability
  - decay across repeated cycles
- The thesis likely needs to justify not just `can it move the finger`, but `what kind of repetitive movement behavior does it produce or preserve`.

## Current Open Positioning Choice

One major choice is still open:

Should the simplified finger system be positioned primarily as:

- `motion assistance`
  - help execute repetitive voluntary finger motion
- `stabilization`
  - resist unwanted oscillatory or unstable motion
- `assessment-enabling platform`
  - reproduce and measure a meaningful repetitive finger task under controlled conditions

My current view is:

- the thesis should probably stay closest to `motion assistance`
- but it should borrow heavily from `assessment` to define outputs
- and it should keep `stabilization` as a comparison bucket rather than the main target unless supervisor feedback pushes more strongly toward `steady finger` or tremor logic

## Candidate Research Questions

These are the strongest current candidate research questions for the project plan and longer proposal.

### Core modeling question

1. What reduced-order biomechanical model is sufficient to study the interaction between a soft variable-stiffness actuator and repetitive finger motion without overbuilding the system?

### Core actuation / controllability question

2. How does variable stiffness affect controllability, repeatability, and actuator-finger interaction in a simplified repetitive finger-motion task?

### Core positioning question

3. Should a thesis-scale simplified finger system be positioned primarily as a motion-assistance device, a stabilization device, or an assessment-enabling experimental platform?

### Core validation question

4. Which task-level outputs best support benchtop validation of a simplified finger-actuator system: amplitude, cycle timing, speed-related observables, variability, interruptions, and sequence-effect-like decay?

### Core abstraction question

5. How much mechanical simplification is acceptable if the task framing comes from Parkinson finger tapping, but the closest hardware precedents come from near-adjacent MCP and index-finger exoskeletons?

### Optional adaptation question

6. What level of adaptive behavior is worth including in a thesis-scale variable-stiffness finger system, given that the broader Parkinson control literature increasingly favors personalized or closed-loop adjustment?

## Recommended Working Thesis Question

If the thesis needs one umbrella question right now, the most defensible version is:

How should a simplified soft variable-stiffness finger actuator be modeled and validated so that it captures the key controllability and interaction features of repetitive finger motion, using Parkinson finger tapping as the task-framing lens without depending on a full clinical or full-hand system?

## Cleaner Project-Plan Version

For the project plan, a shorter and more readable umbrella question is probably better:

How can a simplified variable-stiffness finger actuator be modeled and validated to study controllable repetitive finger motion?

Why this shorter version is better for the plan:

- it keeps the engineering problem clear
- it removes wording that sounds too broad or too clinical
- it leaves Parkinson finger tapping in the `task-framing and output-selection` layer rather than forcing it into the main sentence
- it is easier to scan quickly in a formal project-plan document

If one short explanatory sentence is needed under the question, use:

Parkinson finger tapping is used as the task-framing lens for choosing meaningful motion features and validation outputs.

## Project-Plan Implications

If this framing is accepted, the project plan should probably proceed as:

1. finalize the target task framing
   - repetitive voluntary finger motion with Parkinson finger tapping as the strongest current lens
2. finalize the first abstraction level
   - reduced-order finger plus simplified actuator representation
3. choose the main output variables
   - task-level observables first
4. narrow the hardware bridge
   - MCP/index-finger exoskeleton precedents as the primary mechanical comparison class
5. define benchtop validation around controllability and repeated-movement behavior
   - not around clinical efficacy

## Gantt Guidance

Supervisor feedback suggests the Gantt chart should look less linear and less optimistic.

The current work is better represented as an `iterative modeling-to-prototype workflow` rather than a one-pass sequence.

Recommended planning logic:

1. literature and task framing
   - narrow the engineering question and validation outputs
2. first reduced-order model
   - build the simplest defensible finger-actuator model
3. parameter and model revision
   - revise assumptions after literature and early simulations
4. prototype concept and feasibility
   - choose the mechanism family and clarify what can actually be built
5. prototype iteration and benchtop setup
   - expect redesign and setup friction here
6. bench testing and model comparison
   - compare trends and mismatches, not only best-case fits
7. writing and consolidation
   - keep explicit buffer for analysis cleanup and thesis writing

What the Gantt should show explicitly:

- at least one `iteration loop` between modeling and prototype definition
- a `buffer` between initial prototype concept and actual testing
- overlap between reading, modeling, and design decisions rather than pretending those phases are fully separate
- a final writing block that is not squeezed into the very end

What the Gantt should avoid:

- a perfect straight-line progression from simulation to build to validation
- assuming the first model structure or first prototype concept will hold unchanged
- treating benchtop testing as a short final checkbox

## Next Decision To Make

The next high-value decision is:

Should the thesis explicitly adopt `repetitive voluntary finger motion with Parkinson finger tapping as task framing` as the main positioning layer, while keeping direct mechanical precedent anchored in near-adjacent finger and MCP rehabilitation devices?
