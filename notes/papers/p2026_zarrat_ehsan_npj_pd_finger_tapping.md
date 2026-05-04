# Interpretable and granular video-based quantification of motor characteristics from the finger-tapping test in Parkinson’s disease

## Metadata

- Paper ID: `DOI:10.1038/s41531-026-01307-w`
- Zotero key: `JK7DT9RK`
- Topic: `T010`
- Status: `shortlist`
- Priority: `high`
- Source: `manual`
- Year: `2026`
- Venue: npj Parkinson's Disease
- Authors: Tahereh Zarrat Ehsan; Michael Tangermann; Yağmur Güçlütürk; SooYoon Shin; King Chung Ho; Bastiaan R. Bloem; Luc J. W. Evers
- DOI: 10.1038/s41531-026-01307-w
- URL: https://www.nature.com/articles/s41531-026-01307-w
- PDF status: `attached`
- PDF path: /Users/rami/Zotero/storage/Y88QVSBU/Zarrat Ehsan et al. - 2026 - Interpretable and granular video-based quantification of motor characteristics from the finger-tappi.pdf
- Zotero open link: zotero://select/library/items/Y88QVSBU

## Audit Status

- Reading stage: quote-verified
- Source verification: checked against PDF on 2026-04-06
- Exact quotes logged: yes
- Last audited: 2026-04-06
- Used in:

## Why This Paper Is In The Queue

This is currently the strongest direct task-definition and measurement paper for the Parkinson finger-tapping assessment track in the repo.

## Citation / Bibliographic Notes

- Title: Interpretable and granular video-based quantification of motor characteristics from the finger-tapping test in Parkinson’s disease
- Authors: Tahereh Zarrat Ehsan; Michael Tangermann; Yağmur Güçlütürk; SooYoon Shin; King Chung Ho; Bastiaan R. Bloem; Luc J. W. Evers
- Venue: npj Parkinson's Disease
- Year: 2026
- DOI: 10.1038/s41531-026-01307-w
- URL: https://www.nature.com/articles/s41531-026-01307-w
- Tracker question: What exactly is the Parkinson finger-tapping task, and which motor characteristics does the direct literature measure?

## Abstract / Summary

- This paper introduces an interpretable computer-vision framework for quantifying Parkinson finger-tapping performance from standard videos rather than from wearables or depth cameras.
- The main contribution is not just score prediction. The paper explicitly operationalizes four clinically relevant motor domains: hypokinesia, bradykinesia, sequence effect, and hesitation-halts.
- The paper is unusually important because it connects the Bologna-style clinical decomposition of bradykinesia to a concrete measurement pipeline rather than leaving that decomposition at the review or neuroscience level.
- It is based on a large-scale dataset: 4,073 video recordings from 446 people with Parkinson's disease from the Personalized Parkinson Project, with external evaluation on the TULIP dataset.
- The paper also gives a concrete task abstraction: reduce the movement to a normalized thumb-index distance signal, then derive interpretable tapping features from that signal.
- For this thesis, this is a high-value anchor because it shows how the field currently defines, measures, and decomposes the finger-tapping task without requiring a joint-level biomechanical model.

## One-Sentence Thesis Relevance

- This paper is the strongest current direct anchor in the repo for how Parkinson finger tapping is actually measured, because it turns the clinical task into a source-verified, multi-domain, task-level signal framework.

## Core Definitions (Only From Source)

- Finger-tapping task:
  - in the introduction, patients tap thumb and index finger as widely and rapidly as possible for 10 seconds; in Table 1, they tap the index finger on the thumb 10 times as fast and as large as possible
  - support: p.2 introduction and p.4 Table 1
- Hypokinesia / bradykinesia / sequence effect / hesitation-halts:
  - four clinically relevant motor-characteristic groups used by the paper's feature framework
  - support: p.2 abstract and p.4 results overview
- Signal definition:
  - normalized thumb-index distance based on thumb tip and index finger tip divided by palm length
  - support: p.10 Fig. 7

## Main Claims (Only From Source)

- Claim:
  - an interpretable video-based feature set can quantify granular Parkinson finger-tapping motor characteristics rather than only reproduce a global score
  - Support: abstract p.2 and discussion pp.8-9
- Claim:
  - the dataset is unusually large for this literature, with 4,073 videos from 446 people with Parkinson's disease
  - Support: p.2 abstract, p.4, p.9 discussion, p.10 methods
- Claim:
  - hypokinesia, bradykinesia, and hesitation-halts features align more strongly with clinical severity than the sequence-effect features used here
  - Support: p.4 results and p.8 discussion
- Claim:
  - four clinical domains are useful, but the empirical structure expands to a six-component representation because sequence effect and hesitation-halts each split into finer substructures
  - Support: pp.4-5 PCA discussion and Fig. 4
- Claim:
  - distance-based signals outperform angle-based alternatives in this pipeline
  - Support: p.5 Table 3 discussion

## Key Quotes (Only When Wording Matters)

- Quote:
  - "hypokinesia, bradykinesia, sequence effect, and hesitation-halts"
  - Page: 2
  - Why wording matters: anchors the four-domain decomposition used throughout the paper
- Quote:
  - "period of 10 seconds"
  - Page: 2
  - Why wording matters: captures one side of the task-protocol ambiguity
- Quote:
  - "tap the index finger on the thumb 10 times"
  - Page: 4
  - Why wording matters: captures the other side of the task-protocol ambiguity
- Quote:
  - "We quantified 12 features measuring four groups"
  - Page: 4
  - Why wording matters: concise statement of the feature-engineering scope
- Quote:
  - "six-dimensional representation may capture additional structure"
  - Page: 4
  - Why wording matters: preserves the paper's more nuanced conclusion instead of flattening everything back to four domains

## Mechanistic Insights (From Paper)

- Mechanism:
  - the paper operationalizes tapping through a task-level observable rather than a joint-level biomechanical model
  - support: p.10 Fig. 7 and method pipeline
- Mechanism:
  - clinically meaningful structure can be extracted from a one-dimensional normalized distance signal when paired with feature engineering
  - support: pp.3-5
- Mechanism:
  - sequence effect and hesitation-halts may each contain more than one substructure
  - support: pp.4-5 and p.8 discussion

## Observations / Results (From Paper)

- Finding:
  - 12 domain features plus 2 combined hypo/brady features were quantified
  - description: the feature set covers amplitude, cycle duration, speed, slopes, variability, and interruptions
  - support: p.4
- Finding:
  - the best PPP model achieved 56.44% accuracy and 56.33% balanced accuracy
  - description: this provides the main within-dataset benchmark for the interpretable pipeline
  - support: p.5 Table 2
- Finding:
  - the external TULIP evaluation reached 61.82% balanced accuracy for the best model
  - description: the transfer result supports some cross-dataset robustness
  - support: p.5 Table 2
- Finding:
  - most classification errors occur between adjacent severity classes
  - description: the model is not random; it tends to confuse neighboring ratings rather than collapsing completely
  - support: p.5 Fig. 5
- Finding:
  - most prior studies in this area analyzed fewer than 500 videos
  - description: this helps justify why this paper deserves anchor-paper status
  - support: p.9 discussion

## What This Paper Suggests (Project Interpretation)

- Interpretation:
  - task-level signals may be sufficient for a first thesis-scale tapping analysis even if a richer biomechanical model exists elsewhere
  - Why it matters: it supports a simpler initial measurement and validation strategy
- Interpretation:
  - thesis outputs should likely include separate amplitude, timing, variability, and decrement-like measures rather than one single tapping score
  - Why it matters: it aligns your study guide and future model outputs with current direct assessment practice
- Interpretation:
  - sequence effect should not be assumed to behave cleanly as one scalar feature; even this strong paper finds a more complex internal structure
  - Why it matters: it cautions against oversimplified model assumptions

## Model / Mechanism / Validation Details

- System type: video-based assessment framework for Parkinson finger tapping
- Actuation type: none; vision-only task measurement
- Model type: automated video preprocessing, hand keypoint extraction with Mediapipe, one-dimensional normalized thumb-index distance signal, interpretable feature engineering, PCA with varimax rotation, and machine-learning severity classification
- Signal definition: Euclidean distance between thumb tip and index finger tip, normalized by palm length
- Dataset and labels:
  - Personalized Parkinson Project dataset
  - 4,073 retained videos from 446 participants
  - 2,094 off-medication videos and 1,979 on-medication videos
  - 3,699 videos had a single rating; remaining videos had 2 to 7 ratings
  - videos with 2-point or greater rating disagreement were excluded
- Task protocol as described in the paper:
  - introduction wording: tap thumb and index finger as widely and rapidly as possible for 10 seconds
  - Table 1 wording: tap the index finger on the thumb 10 times, as fast and as large as possible
- Feature families:
  - hypokinesia: average amplitude
  - bradykinesia: average cycle duration
  - combined hypo/bradykinesia: average cycle maximum speed and cycle average speed
  - sequence effect: amplitude slope, cycle duration slope, speed slope
  - hesitation-halts: variability in amplitude, cycle duration, cycle maximum speed, cycle average speed, plus number of interruptions
  - total extracted feature count used in the main analysis: 12 domain features plus 2 combined hypo/brady features
- Validation setup:
  - leave-one-subject-out cross-validation on PPP
  - comparison against prior video-based methods under matched evaluation settings
  - external transfer test on front-view TULIP videos
- Main quantitative results:
  - PPP best model: multi-class LightGBM with 56.44% accuracy and 56.33% balanced accuracy
  - TULIP transfer: best balanced accuracy 61.82%, macro precision 61.11%, macro F1 56.64%
  - distance-based features outperformed angle-based features across all tested classifiers
- Main interpretation result:
  - PCA partially supports the four-domain clinical structure, but a six-component representation was needed because sequence effect and hesitation-halts each split into finer substructures

## Figure / Result Takeaways

- Figure 1 is the cleanest one-slide summary of the paper's logic: video -> hand keypoints -> normalized thumb-index distance signal -> interpretable feature extraction -> severity estimation.
- Table 1 is useful for thesis writing because it reproduces the MDS-UPDRS task criteria in concrete terms, including how interruptions, slowing, and amplitude decrement patterns map to severity scores.
- Figure 2 gives a concrete visual contrast between low-impairment and higher-impairment tapping:
  - score 0 example: average cycle duration 0.34 s
  - score 3 example: average cycle duration 0.42 s
  - the higher-impairment example shows reduced amplitude and speed that decays over time
- Figure 3 is important because it shows which feature families actually separate clinical severity:
  - hypokinesia, bradykinesia, and hesitation-halts features separate severity levels strongly
  - sequence-effect features are weaker and less monotonic than the other families
  - interruptions become especially informative at scores 3 and 4
- Figure 4 is one of the most thesis-relevant results in the paper:
  - six components explain approximately 90.8% of total variance
  - sequence effect splits into amplitude/speed slope versus cycle-duration slope
  - hesitation-halts splits into amplitude/speed variability versus cycle-duration variability/interruption structure
- Table 2 matters mainly as benchmarking support: the interpretable pipeline is not only clinically cleaner than black-box scoring approaches, it also remained competitive or better on score prediction.
- Table 3 is especially useful for method reuse: distance-based features outperform angle-based features across logistic regression, LightGBM, and random forest.
- Figure 7 is the key methodological figure to remember if you later compare task-level sensing with biomechanical modeling: the paper's central signal is normalized thumb-index distance, not a joint-angle state estimate.

## What Matters For This Thesis

- This paper gives the clearest current answer in the repo to what the Parkinson finger-tapping task is and how the task is decomposed analytically.
- It supports a key framing point for the thesis: the clinical task itself is simple, but the measurable deficits are not. The field is already moving away from a single coarse tapping score toward multiple motor-characteristic outputs.
- Importantly, the paper does not require a joint-level anatomical model to extract useful clinical information. It works from a task-level observable, which is relevant because your thesis may not need a full anatomical hand model to justify a simplified tapping-oriented system.
- Methodologically, this paper is a strong reminder that assessment literature often prefers robust task-level observables over richer but less reliable biomechanical representations. Their own comparison shows distance-based signals outperform angle-based signals.
- For design positioning, the paper strengthens the argument that the direct Parkinson literature is richest in assessment logic and signal design, not in tapping-specific assistance hardware.
- For modeling, the paper suggests at least one useful comparison axis: joint-level biomechanical states versus task-level observables such as tap amplitude, cycle duration, speed, interruptions, and intra-trial decay.
- For validation, it points toward outputs that would be meaningful even for a benchtop or simulated system:
  - amplitude achieved
  - cycle timing
  - speed-related observables
  - variability and interruptions across repeated cycles
  - whether deficits should be reported as one score or as a structured set of outcomes
- Most importantly, the paper suggests that a tapping-oriented rehabilitation device or simulator may be evaluated more convincingly if it reproduces or perturbs deficit-specific task signatures rather than only maximizing generic tapping frequency.

## Relevance To Finger Tapping / Thesis

- Direct relevance:
  - strongest direct assessment and task-decomposition paper for Parkinson finger tapping currently in the repo
- Indirect relevance:
  - useful as a measurement benchmark and as a counterpoint to hardware papers that do not specify clinically meaningful task outputs

## Control-System Interpretation (Project Interpretation)

- Controller:
  - abstracted away; the paper measures output behavior rather than modeling neural control directly
- Plant:
  - thumb-index tapping behavior as observed through video
- Feedback:
  - not explicitly modeled, but irregularity and interruption features indirectly reflect breakdown in repeated movement stability
- Reference:
  - repeated fast, large thumb-index tapping task
- Notes:
  - the paper is a good reminder that a useful system model can live at the task-signal level even when internal biomechanics remain simplified

## Limitations

- It is not a device-assistance or exoskeleton paper.
- It does not tell you how to design a finger actuator or simplify the finger mechanically.
- The method extracts task-relevant features from observed motion rather than defining a biomechanical control model.
- The dataset is large, but still clinic-collected rather than truly uncontrolled home data.
- All videos were acquired in the same clinic, even though they include variability in room lighting, background, camera angle, and participant distance.
- The paper explicitly notes failure modes from occlusion and poor keypoint visibility, especially in more severely impaired participants.
- The ground truth ratings remain subjective clinical scores; inter-rater agreement was only moderate (`Krippendorff's alpha = 0.52`), which is one reason the authors argue against treating score prediction as the final objective.
- The article-in-press text contains a wording ambiguity around `10 times` versus `10 seconds`, so the final published version should be checked before quoting the protocol verbatim.
- The external validation set is useful but still small, so cross-dataset generalization should not be overstated.

## Decision Impact

- Promote this paper above Guo 2022 as the primary direct assessment-anchor paper.
- Use it to define the task protocol caveats, signal definition, and main motor-feature vocabulary for the review and presentation.
- Use it to argue that direct Parkinson finger-tapping literature is strongest in assessment systems, symptom decomposition, and task-level signal design, not in assistive hardware.
- Use it as the main justification for discussing Parkinson finger tapping through multiple deficit dimensions instead of one scalar severity score.

## Exact Quotes / Evidence Bank

- Quote: "4,073 videos from 446 individuals with PD"
- Page: 4
- Section or figure: method overview / dataset description
- Why it matters: confirms the unusually large dataset behind this task-definition paper.
- Reusable in: assessment-track justification

- Quote: "hypokinesia, bradykinesia, sequence effect, and hesitation-halts"
- Page: 2
- Section or figure: conceptual framing
- Why it matters: anchors the four-domain decomposition used throughout the paper.
- Reusable in: Parkinson task-framing synthesis

- Quote: "tap the index finger on the thumb 10 times"
- Page: 4
- Section or figure: MDS-UPDRS criteria figure/discussion
- Why it matters: one explicit statement of the task protocol wording used in the paper.
- Reusable in: task-definition note with ambiguity caveat

- Quote: "period of 10 seconds"
- Page: 2
- Section or figure: introduction
- Why it matters: shows the internal wording ambiguity that should be preserved as a caution.
- Reusable in: protocol caveat

- Quote: "thumb tip and index finger tip divided by palm length"
- Page: 10
- Section or figure: signal-generation figure
- Why it matters: captures the task-level signal abstraction used by the method.
- Reusable in: modeling-vs-task-level comparison

- Quote: "We quantified 12 features measuring four groups"
- Page: 4
- Section or figure: results / feature overview
- Why it matters: confirms the feature-engineering scope and the link between the four-domain framing and the actual analysis.
- Reusable in: assessment-method breakdown

- Quote: "six-dimensional representation may capture additional structure"
- Page: 4
- Section or figure: PCA-varimax interpretation
- Why it matters: shows that the paper does not fully collapse back to the original four-domain framing.
- Reusable in: discussion of task complexity

- Quote: "accuracy of 56.44 % and balanced accuracy of 56.33 %"
- Page: 5
- Section or figure: classifier comparison
- Why it matters: gives the core PPP benchmark numbers for the best model.
- Reusable in: performance summary

- Quote: "balanced accuracy of 61.82 %"
- Page: 5
- Section or figure: external TULIP evaluation
- Why it matters: supports the claim that the method transfers reasonably to an external dataset.
- Reusable in: generalization discussion

- Quote: "fewer than 500 videos"
- Page: 9
- Section or figure: discussion / dataset scale comparison
- Why it matters: helps justify why this paper is a stronger anchor than many older assessment studies.
- Reusable in: why-this-paper-is-central

- Quote: "entirely non-contact and does not require physical attachment"
- Page: 9
- Section or figure: discussion / comparison with wearable sensors
- Why it matters: clarifies the sensing tradeoff versus glove- or sensor-based systems.
- Reusable in: sensing-modality comparison

- Quote: "Krippendorff's α, which yielded α = 0.52"
- Page: 10
- Section or figure: methods / rating reliability
- Why it matters: quantifies the subjectivity still present in the label source.
- Reusable in: caveat on ground truth

- Quote: "2,094 were recorded in the off state and 1,979 in the on state"
- Page: 10
- Section or figure: dataset flow / retained sample description
- Why it matters: preserves the medication-state split, which could matter later for validation framing.
- Reusable in: dataset description

## Claims Safe To Reuse Later

- Claim: Zarrat Ehsan 2026 is currently one of the strongest direct Parkinson finger-tapping assessment anchors because it combines a large dataset with an interpretable multi-domain feature framework.
- Support: pp.2, 4, and 9
- Confidence: high

- Claim: The paper treats finger tapping as a task-level thumb-index signal rather than as a joint-level biomechanical model.
- Support: p.10 signal-generation description
- Confidence: high

- Claim: The protocol wording in the paper should be quoted cautiously because the text contains both "10 times" and "10 seconds" formulations.
- Support: p.2 and p.4
- Confidence: high

- Claim: The paper's own results suggest that four clinical domains are useful but not fully sufficient, because sequence effect and hesitation-halts split into finer substructures.
- Support: pp.4-5 PCA discussion and Fig. 4
- Confidence: high

- Claim: Distance-based tapping signals are a stronger methodological choice than angle-based signals for this vision-based task because they are more robust to viewpoint variation and performed better across classifiers.
- Support: p.5 comparison text and Table 3
- Confidence: high

- Claim: The dataset scale makes this paper a stronger assessment anchor than many prior finger-tapping vision papers in the repo.
- Support: p.2 abstract, p.4 dataset description, p.9 scale comparison against prior work
- Confidence: high

## What This Paper Does Not Answer

- Gap:
  - it does not provide a mechanical assistance or exoskeleton design for Parkinson finger tapping
- Gap:
  - it does not specify how a simplified finger actuator should be designed or controlled
- Gap:
  - it does not resolve whether the best thesis model should be task-level only or should also include a low-order biomechanical layer

## Open Questions

- Question:
  - which subset of Zarrat's task-level features is most worth carrying into a thesis-scale simulation or benchtop validation?
- Question:
  - if sequence effect and hesitation-halts each split internally, how much of that structure is necessary for a first reduced-order model?

## Tags

- Parkinson's disease
- finger tapping
- assessment
- computer vision
- sequence effect
- task-level signal
- validation metrics

## Clean Takeaway

- The paper defines finger tapping clinically as repeated fast, large thumb-index tapping and operationalizes it as a normalized thumb-index distance signal over time.
- From that signal, it separates clinically meaningful deficit families instead of collapsing the task into one overall score, and the results suggest that some of those families split further into six components.
- This is useful for thesis framing because it suggests that task-level signals and deficit-specific outputs may matter more than a full anatomical finger model when the goal is tapping assessment or tapping-oriented validation.

## Next Action

Use it as the main assessment anchor, preserve the task-protocol wording ambiguity when citing it, and mirror the strongest quotes and table-level figures into the Zotero note for writing-time reuse.
