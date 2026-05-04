# Meeting Prep 10-04-26

## Focus

- Broad Parkinson's disease rehabilitation literature, not only finger or hand papers
- Use `Raciti et al. 2022` as an example of Parkinson-specific upper-limb robotic rehabilitation
- Extract what this paper contributes to thesis positioning and what it does not

## Paper

- `Raciti et al. 2022`
- `Improving Upper Extremity Bradykinesia in Parkinson’s Disease: A Randomized Clinical Trial on the Use of Gravity-Supporting Exoskeletons`
- DOI: `10.3390/jcm11092543`
- Type: Parkinson-specific rehabilitation trial
- Bucket: `robot-assisted rehabilitation / upper-limb exoskeleton context`

## What The Paper Is Actually About

This is not a finger-device paper. It is a Parkinson-specific upper-limb rehabilitation paper using the `Armeo Spring`, a gravity-supporting exoskeleton-like rehab system for the arm with a hand grasping interface.

The key question is whether robot-assisted repetitive upper-limb training improves Parkinson-related upper-limb function better than matched conventional therapy.

## Device And Intervention

- Device: `Armeo Spring`
- Role: gravity-supported upper-extremity training
- Setup: clinic-based, therapist-calibrated, semi-autonomous, with visual feedback / virtual tasks
- Dose: `45 min/day`, `6 days/week`, `8 weeks`
- Comparison: same total therapy time with conventional physical therapy

## Study Design

- `30` PD participants enrolled
- Hoehn-Yahr `2-3`
- randomized `1:1`
- assessor-blinded
- primary outcome: `9HPT`
- secondary outcomes: `UPDRS-III`, `FMA-UE`, `MI-UE`, `FIM`, `P-NRS`

## Results To Remember

### Strongest Positive Findings

- `9HPT`
  - ERT: `42.2 -> 34.1`
  - CPT: `35.1 -> 31.4`
  - between-group `p = 0.004`
- `MI-UE`
  - ERT: `72 -> 89`
  - CPT: `77 -> 82`
  - between-group `p = 0.0001`
- `FMA-UE`
  - ERT: `48 -> 53`
  - CPT: `53 -> 56`
  - between-group `p = 0.009`

### Weaker Or Less Convincing Findings

- `UPDRS-III`
  - ERT improves numerically
  - between-group `p = 0.5`
  - not a strong between-group result from the table
- `FIM`
  - not a convincing between-group result
- `P-NRS`
  - both groups improved
  - no robotic advantage

### Important Nuance From Table 3

When the authors focus on the `most affected side`, the paper becomes less clean:

- `9HPT`: both groups improved, between-group `p = 0.7`
- `MI-UE`: still favors ERT
- `FMA-UE`: still favors ERT

So the strongest headline result, `9HPT superiority`, is not equally strong in every slice of the analysis.

## Figures

### Figure 1

Participant flow diagram.

Why it matters:

- shows the study was disrupted by `COVID-19`
- shows `6` control-group dropouts
- final analyzed groups were `15 ERT` and `9 CPT`

This is one of the paper's main weaknesses.

### Figure 2

Photo of a PD patient using the `Armeo Spring`.

Why it matters:

- visually confirms this is a `large clinic-based upper-limb rehab system`
- not a small wearable assistive device
- not a finger-specific mechanism precedent

## What The Paper Contributes To A PD Rehab Review

- It shows Parkinson-specific robotic rehabilitation is not only about gait.
- It supports the idea that `repetitive`, `task-oriented`, `assistive` upper-limb training is an active PD rehab theme.
- It treats `hand dexterity` as a meaningful Parkinson rehabilitation outcome.
- It helps justify a broader PD rehab section in the literature review.

## What The Paper Does Not Contribute Well

- It is not a direct finger-actuator or finger-biomechanics precedent.
- It gives limited mechanical or control detail.
- It is a clinical outcome paper, not a modeling paper.
- It does not directly tell us how to design a variable-stiffness finger system.

## Why MI-UE Is A Limitation

`MI-UE` means `Motricity Index for Upper Extremity`.

Why I called it `more stroke-style than PD-specific`:

- The measure is more commonly used in `stroke rehabilitation`.
- It evaluates gross upper-limb motor capacity with tasks such as holding or lifting against gravity.
- Parkinson-related upper-limb impairment is real, but the scale was not built specifically around classic Parkinson motor features such as bradykinesia, sequence effect, hesitations, or tremor.
- The authors themselves say this is a limitation and note that the scale is not usual for PD evaluation.

So:

- the result is still useful
- but it is a `less disease-specific signal` than something like dexterity or task-focused movement measures

## Q And A On The Paper

### Does the paper provide guidance on neuroplasticity?

Yes, but only `conceptually`, not directly.

What it says:

- intensive, repetitive, task-oriented robotic training may help trigger neuroplasticity
- assist-as-needed practice may support motor relearning
- visual feedback and virtual tasks may improve engagement and learning
- the authors mention possible roles for:
  - motor learning
  - mirror neuron system activation
  - cortical and subcortical reorganization
  - cerebellar compensation

What it does **not** do:

- it does not measure neuroplasticity directly
- no imaging
- no electrophysiology
- no mechanistic biomarker showing that plasticity changed

So the paper gives a `rehabilitation rationale`, not direct evidence of neuroplasticity mechanisms.

### What is the most defensible takeaway from the paper?

That Parkinson-specific upper-limb robotic rehabilitation can improve some dexterity- and movement-related outcomes, but the evidence here is `promising rather than definitive`.

### Why is the paper still worth keeping if it is not finger-specific?

Because this literature pass is now about `PD rehabilitation in general`.

This paper helps answer:

- do Parkinson-specific upper-limb robotic rehab papers exist?
- what kinds of outcomes do they care about?
- what kind of intervention logic is used?
- is dexterity considered a meaningful endpoint?

### Does the paper say robot therapy is clearly superior overall?

Not cleanly.

The paper supports superiority on some measures, especially:

- `9HPT`
- `MI-UE`
- `FMA-UE`

But not across all outcomes, and the attrition makes the result less robust than the abstract tone suggests.

### What are the biggest weaknesses?

- underpowered relative to the planned sample
- COVID disruption
- severe dropout imbalance in the control group
- no intention-to-treat analysis
- some discussion claims are stronger than the table evidence
- no long-term follow-up

### Does it help with thesis research questions?

Yes, mainly on the `positioning` side.

It supports questions like:

- Which Parkinson-relevant outcomes should matter for a rehabilitation device?
- Should the thesis be framed around dexterity, repetitive movement quality, or broader motor impairment?
- How much should the thesis borrow from PD-specific rehab logic versus finger-device mechanics?

### Which outcomes are actually strong, and which are overstated?

Strongest outcomes:

- `9HPT` in the main analysis
- `MI-UE`
- `FMA-UE`

Less convincing than the discussion tone suggests:

- `UPDRS-III`
  - between-group `p = 0.5`
- `FIM`
  - between-group `p = 0.6`
- `P-NRS`
  - both groups improved, no robotic advantage

Best meeting phrasing:

- the paper is strongest on `dexterity` and `selected upper-limb function measures`
- it is not equally strong across all clinical outcomes

### Why does 9HPT look stronger in Table 2 than in Table 3?

Most likely because:

- the overall analysis is cleaner than the affected-side-only analysis
- once the analysis narrows to the most affected side, the already small sample becomes noisier
- the dropout imbalance reduces stability

So:

- `9HPT` is still an important positive result
- but it is better described as `promising` than `fully robust`

### What does the dropout imbalance do to how much we trust the result?

It matters a lot.

- planned sample: `60`
- enrolled: `30`
- final analyzed groups: `15 ERT` and `9 CPT`
- no intention-to-treat analysis

This weakens confidence in the effect size and makes the study better used as `supportive evidence` than as decisive proof.

### Does this paper support a dexterity-focused framing more than a tremor- or control-focused one?

Yes.

This paper is much closer to:

- `repetitive movement assistance`
- `dexterity-oriented rehabilitation`
- `bradykinesia-related upper-limb dysfunction`

It is much less relevant to:

- tremor suppression
- disturbance rejection
- adaptive closed-loop symptom control

So if this paper is used in the thesis framing, it supports a `dexterity / repetitive movement` angle more than a `tremor stabilization` angle.

## Raciti 2025

- `Exploring the Impact of Robotic Hand Rehabilitation on Functional Recovery in Parkinson’s Disease: A Randomized Controlled Trial`
- Brain Sciences `2025`
- DOI: `10.3390/brainsci15060644`

This looks like a more `hand-specific follow-on` paper from the same broader research direction.

Key differences versus `Raciti 2022`:

- uses the `AMADEO` robotic hand system rather than the `Armeo Spring`
- more explicitly hand- and finger-focused
- includes both `motor` and `cognitive` outcomes
- treats hand/finger rehabilitation as a more direct target

From the abstract:

- RAT improved `MoCA` and `FAB`
- motor improvement was strongest in `wrist` and `hand control`
- `9HPT` improvements were less consistent and did not reach robust significance
- quality of life effects were limited except for the `stigma` subdomain of `PDQ-39`

Why it matters:

- it is probably a better bridge paper than `Raciti 2022` if the literature review wants to move from `general PD upper-limb rehab` toward `hand-focused PD rehab`
- it still is not a soft finger-actuator paper, but it is closer to the thesis motion scale

## Use This Note

Working copy for the meeting lives here in `notes/Meetings/`.

---

## Raciti 2025

### Paper

- `Raciti et al. 2025`
- `Exploring the Impact of Robotic Hand Rehabilitation on Functional Recovery in Parkinson’s Disease: A Randomized Controlled Trial`
- DOI: `10.3390/brainsci15060644`
- Venue: `Brain Sciences`
- Device: `AMADEO`
- Bucket: `Parkinson-specific robotic hand rehabilitation`

### Definitions First

- `RAT`
  - `Robotic-Assisted Therapy`
  - this is the experimental group in the 2025 paper
- `CPT`
  - `Conventional Physical Therapy`
  - this is the control group
- `T0`
  - baseline, before treatment
- `T1`
  - post-treatment
- `MoCA`
  - `Montreal Cognitive Assessment`
  - broad cognitive screening
- `FAB`
  - `Frontal Assessment Battery`
  - executive-function screening
- `UPDRS-III`
  - motor section of the Parkinson rating scale
- `9HPT`
  - `9-Hole Peg Test`
  - hand dexterity test
- `FMA-UE`
  - `Fugl-Meyer Assessment for Upper Extremity`
  - upper-limb motor control score
- `PDQ-39`
  - `Parkinson’s Disease Questionnaire-39`
  - Parkinson-specific quality-of-life questionnaire
- `HAM-D`
  - `Hamilton Depression Rating Scale`

### What This Paper Is Actually About

Unlike `Raciti 2022`, this paper is much more `hand-focused`.

It uses the `AMADEO` robotic hand system, where each finger is attached individually to robotic actuators and trained with passive/active modes plus visual/virtual feedback.

The paper is also more ambitious than the 2022 paper because it tries to show:

- motor improvement
- cognitive improvement
- some quality-of-life effects
- predictive relationships using regression models

### Study Design

- `40` total patients
- `20` experimental and `20` control
- single-blind randomized controlled trial
- Hoehn-Yahr `1-3`
- `45 min per arm`, `6 days/week`, `8 weeks`

This is cleaner than the 2022 study in terms of sample size and balance of group numbers.

### Table 1: Baseline Characteristics

This table matters more than it first appears.

What it shows:

- experimental group was `older`
  - `64.8` vs `56.8`, `p = 0.01`
- experimental group had `less education`
  - `8.8` vs `12.2`, `p = 0.007`
- sex distribution was not significantly different

Why this matters:

- the groups were not fully comparable at baseline
- this makes later cognitive comparisons harder to interpret cleanly
- the authors try to handle this statistically with `ANCOVA`

### Table 2: Inter-Group Comparison At T0 And T1

This is the most important table to keep straight.

At `T0`:

- no baseline difference in `MoCA`, `UPDRS-III`, or `9HPT`
- but there **were** baseline differences in:
  - `HAM-D`
  - `FMA-UE hand`
  - `FMA-UE wrist`

At `T1`:

- `FAB` differs between groups
  - `p = 0.04`
- `HAM-D` still differs
  - `p = 0.002`
- `FMA-UE wrist` still differs
  - `p = 0.0081`
- `MoCA`, `UPDRS-III`, and `9HPT` do **not** differ significantly between groups at T1

Main caution:

- the abstract sounds stronger than this table alone
- the cleanest raw between-group evidence is not for every outcome

### Table 3: Experimental Group Only, T0 Vs T1

This table is within-group only for the robotic group.

Significant improvement within the experimental group:

- `UPDRS-III`
- `FMA-UE hand`
- `FMA-UE wrist`
- `FMA-UE coordination`
- `9HPT`
- `MoCA`
- `FAB`
- `PDQ-39 stigma`

Not significant:

- total `PDQ-39`
- `HAM-D`
- most memory and broader neuropsych measures

Why this matters:

- the robotic group clearly improved on several measures
- but this table alone does **not** prove superiority over control
- it is useful, but it is not the same as a between-group result

### Table 4: Regression Models

This table summarizes regression models for:

- `MoCA`
- `FAB`
- `HAM-D`

Reported `R^2` values are very high:

- `MoCA`: `0.911`
- `FAB`: `0.927`
- `HAM-D`: `0.929`

Important interpretation:

- these are mainly saying baseline variables strongly predict T1 values
- for example baseline `FAB` predicts later `FAB`
- this is not the same as saying the intervention itself explains almost everything

So the regression section is interesting, but it should not be mistaken for direct causal proof of robotic benefit.

### Figure 1

`CONSORT flow diagram`

Why it matters:

- confirms randomized-trial structure
- unlike the 2022 paper, this does not visually signal the same kind of dramatic control-group attrition problem

### Figure 2

`Photo of the AMADEO system`

Why it matters:

- confirms this is a `distal hand/finger` robotic system
- much closer to finger-focused rehabilitation than the `Armeo Spring`
- still a clinic device, not a soft wearable daily-life assist device

### Figure 3

`Demographic distributions`

What it adds:

- mainly visual confirmation of the age and education imbalance

This figure is not conceptually deep, but it is useful because it visually reinforces the baseline mismatch.

### Figure 4

`Grouped bar plots of outcomes with significant differences`

This is one of the most useful figures in the paper because it shows:

- `FAB` is stronger for the experimental group at T1
- `FMA hand` started worse in the experimental group, then got closer
- `FMA wrist` started worse in the experimental group and still remained lower at T1

This figure actually makes one weakness of the paper clearer:

- some motor outcomes look improved within the robotic group
- but the group differences are partly entangled with baseline imbalance

### Figure 5

`ANCOVA-adjusted comparison for MoCA and FAB`

This is the figure the authors use to support the `cognition` story.

It matters because:

- the raw Table 2 comparison for `MoCA` is not significant
- but the adjusted analysis is presented as significant

So this figure is central to their claim that the robotic intervention helps cognition beyond simple baseline differences.

### Figures 6 To 8

`Observed vs predicted and residual plots for MoCA, FAB, HAM-D`

These are mostly regression-diagnostic figures.

What they are for:

- showing model fit
- showing residual behavior

What they are **not**:

- direct evidence of motor benefit
- direct evidence of hand-specific rehabilitation value

So these figures are technically legitimate, but for thesis reading they are lower priority than Figures `3`, `4`, and `5`.

### Figure 9

`Standardized regression coefficients`

This is a compact summary of which baseline variables predict which T1 outcomes.

Usefulness:

- good for seeing how age, education, and baseline severity might shape outcomes

Limitation:

- still a secondary statistical layer, not the core rehabilitation evidence

### What The Paper Seems Strongest On

Most convincing:

- `executive and global cognitive improvement`
  - especially `FAB`
  - `MoCA` mostly through adjusted analysis
- `within-group motor improvements` in the robotic arm
- the idea that hand-focused robotic rehab in PD is feasible and worth studying

### What The Paper Is Weakest On

Less convincing:

- clean raw between-group superiority on `9HPT`
- clean raw between-group superiority on all motor measures
- quality-of-life improvement outside the `stigma` subscale
- broad emotional improvement

### Neuroplasticity: What Does This Paper Actually Say?

This paper leans much harder on neuroplasticity than the 2022 paper.

What it argues:

- repetitive, goal-directed, attentionally demanding robotic training may engage:
  - frontal-executive networks
  - frontal-striatal circuits
  - sensorimotor hand representation areas
  - broader cross-domain motor-cognitive plasticity

What it does **not** show directly:

- no direct neural measurement
- no imaging
- no electrophysiology
- no biomarker proving plastic change

So again:

- `neuroplasticity is the explanatory framework`
- not a directly measured result

### Most Defensible Takeaway

`Raciti 2025 provides promising Parkinson-specific evidence that robotic hand rehabilitation may improve executive function and some hand/wrist motor outcomes, but the motor story is complicated by baseline group differences and the strongest claims rely more on adjusted cognitive analyses than on uniformly strong raw between-group effects.`

### Good Questions To Bring Up About This Paper

#### 1. Why is `MoCA` non-significant in Table 2 but highly significant in the ANCOVA figure?

This is one of the sharpest reading questions in the paper.

Why it matters:

- the raw table does not show a clear post-treatment between-group difference for `MoCA`
- the adjusted analysis does
- this means the cognition claim depends heavily on the adjustment model, not just the raw data

#### 2. Exactly which covariates were included in the ANCOVA models?

The methods clearly mention baseline score as a covariate, but the surrounding text makes it sound like age and education may also matter.

Why it matters:

- the interpretation of the adjusted results depends on what was actually adjusted
- the paper is not as transparent here as it could be

#### 3. Why is there no full control-group pre/post table parallel to Table 3?

Table 3 only shows within-group change in the experimental group.

Why it matters:

- this makes the robotic group improvement easy to see
- but makes direct comparison to control less transparent

#### 4. How much should we trust motor conclusions when `FMA-hand` and `FMA-wrist` were already significantly different at baseline?

Why it matters:

- these baseline imbalances complicate the motor interpretation
- the paper may be showing robotic-group improvement, but not always clean superiority over control

#### 5. Does the paper show robotic superiority, or mostly that the robotic group improved from a worse starting point?

This is probably the best single critique question.

#### 6. Were corrections made for multiple comparisons?

The paper measures many outcomes.

Why it matters:

- with many tests, some significant p-values can appear by chance
- this matters especially when the paper highlights selected positive findings

#### 7. Are the cognitive changes clinically meaningful, or only statistically significant?

Why it matters:

- `MoCA` and `FAB` changes may be statistically interesting
- but that is not automatically the same as a meaningful change in daily functioning

#### 8. Do the regression models add causal insight, or mostly show that baseline scores predict post-treatment scores?

Why it matters:

- high `R^2` can look impressive
- but if baseline score is doing most of the work, that is not the same as strong intervention evidence

#### 9. Is the paper’s strongest contribution really motor rehabilitation, or is it a `cognitive-motor rehabilitation` argument?

My current answer:

- more the second than the first

#### 10. If `9HPT` is the main dexterity measure, why is its between-group evidence relatively weak?

Why it matters:

- this question cuts directly into the gap between the hand-rehabilitation framing and the actual raw evidence

## Thesis Checkpoint

### Have The Research Questions Evolved?

Yes, at least in framing.

Earlier, the work was being pulled toward:

- finger tapping
- pinch/opposition
- near-adjacent finger exoskeletons

Now the broader Parkinson pass suggests the thesis may need to separate three possible framings more explicitly:

- `repetitive voluntary finger-movement assistance`
- `stabilization / suppression of unwanted motion`
- `assessment-oriented task reproduction`

This does not mean the thesis question has to become broader. It means the framing question has become clearer.

### Current Best Thesis-Level Questions

These now look like the strongest candidates:

1. Which Parkinson-relevant motor problem should a simplified variable-stiffness finger system target: repetitive voluntary movement impairment, unwanted oscillatory motion, or a hybrid of both?
2. What reduced-order biomechanical model is sufficient to capture the dominant actuator-finger interaction for that target problem?
3. Which controllability and validation metrics best distinguish useful assistance from excessive resistance in a simplified finger-actuator system?
4. How should broader Parkinson rehabilitation literature inform the thesis framing without pretending that broad PD rehab devices are direct finger-mechanism precedents?

### What The Broad PD Literature Is Doing For The Thesis

It is helping with:

- symptom framing
- outcome framing
- rehabilitation logic
- control/assistance framing

It is not yet giving:

- a direct finger mechanism answer
- a direct variable-stiffness design answer
- a direct simplified finger model answer

### Current Thesis Risk

The main risk now is not lack of reading. It is `framing drift`.

In other words:

- broad PD rehab papers are useful
- but the thesis still needs to stay anchored to a simplified finger-actuator study

### Current Best Working Position

Use broad Parkinson literature for:

- why the problem matters
- which symptom/task class is defensible
- what outcomes matter

Use finger and hand device papers for:

- mechanism precedent
- interaction variables
- simplification choices

## Useful One-Line Summary

`Raciti et al. 2022 is a Parkinson-specific upper-limb robotic rehabilitation trial showing promising improvements in dexterity-related outcomes, but it is better used as PD rehab positioning evidence than as a direct mechanical precedent for a finger-actuator thesis.`

## Good Supervisor Questions To Be Ready For

- Why is this paper relevant if the device is not finger-specific?
- Which outcomes in this paper are actually convincing?
- What does this paper add beyond "robot rehab might help"?
- Does the paper justify any control or modeling choice, or only a clinical framing choice?
- Does this support a Parkinson-specific thesis framing, or only a general neurorehabilitation framing?
- What does the paper imply about which motor deficit should be targeted next?

## My Current Answer

This paper is useful because it shows that Parkinson-specific upper-limb robotic rehabilitation exists and values dexterity-oriented outcomes. But it does not replace the need for more targeted hand or finger papers if the thesis eventually narrows back toward a simplified finger-actuator system.


