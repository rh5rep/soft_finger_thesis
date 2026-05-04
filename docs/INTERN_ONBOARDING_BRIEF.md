# Intern Onboarding Brief

## Purpose

This brief is the fastest safe way to bring a new intern into the thesis without making them read the entire repo in random order.

The goal is not to turn interns into domain experts on day one. The goal is to give them:

- the current thesis scope
- the active literature framing
- the strongest paper buckets already identified
- the repo workflow they should follow when adding value
- the boundaries that stop them from widening the project accidentally

## Thesis In One Paragraph

This thesis is currently best understood as a simulation-first study of how a soft variable-stiffness actuator interacts with a simplified finger system for neurorehabilitation. The strongest current task-framing lens is Parkinson-relevant repetitive finger motion, especially finger tapping, but the closest mechanical precedents are not Parkinson-specific tapping exoskeletons. They are near-adjacent index-finger and MCP-centered rehabilitation devices. The project is not a full glove project, not a sensing-led thesis, and not a clinical efficacy study.

## Read These First

These are the mandatory repo entry points before an intern starts reading papers or touching model code.

1. [THESIS_BRIEF.md](THESIS_BRIEF.md)
2. [CURRENT_TASK.md](CURRENT_TASK.md)
3. [DECISION_LOG.md](DECISION_LOG.md)
4. [STUDY_GUIDE.md](STUDY_GUIDE.md)
5. [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md)

What each file is for:

- `THESIS_BRIEF.md`: thesis scope, research questions, success criteria
- `CURRENT_TASK.md`: current primary question and deliverable boundaries
- `DECISION_LOG.md`: decisions that prevent repeated scope drift
- `STUDY_GUIDE.md`: writing-safe synthesis only
- `LITERATURE_AUDIT.md`: operational truth about what is captured versus actually usable

## Topic Audit

### Tier 1: Core Topics Interns Should Understand Immediately

These are the topics that most directly explain what this thesis is doing now.

| Topic | Why it is core | Best current repo resources |
| --- | --- | --- |
| Thesis scope and architecture | Prevents interns from widening the project into a glove, clinical study, or full FEM problem | [THESIS_BRIEF.md](THESIS_BRIEF.md), [DECISION_LOG.md](DECISION_LOG.md), [08_thesis_positioning_and_research_questions.md](TOPIC_MEMOS/08_thesis_positioning_and_research_questions.md) |
| Parkinson finger tapping as task framing | Explains why finger tapping matters even though the thesis is not becoming a pure assessment project | [07_parkinsons_assistive_control_devices.md](TOPIC_MEMOS/07_parkinsons_assistive_control_devices.md), [06_pinch_finger_tapping_technologies.md](TOPIC_MEMOS/06_pinch_finger_tapping_technologies.md) |
| Direct task-definition and symptom papers | Clarifies that bradykinesia is not just slowness and that tapping should be treated through multiple observables | [p2020_bologna_bradykinesia_concepts.md](../notes/papers/p2020_bologna_bradykinesia_concepts.md), [p2026_paparella_bradykinesia_complex.md](../notes/papers/p2026_paparella_bradykinesia_complex.md), [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md) |
| Assessment technologies for finger tapping | Shows where the direct task literature is strongest today | [p2024_amo_salas_pd_ft_survey.md](../notes/papers/p2024_amo_salas_pd_ft_survey.md), [p2023_ravichandran_itex_gloves.md](../notes/papers/p2023_ravichandran_itex_gloves.md) |
| Near-adjacent hardware bridge | These are the clearest mechanical precedents for a simplified finger system | [p2021_sun_self_aligning_index_finger.md](../notes/papers/p2021_sun_self_aligning_index_finger.md), [p2023_peperoni_self_aligning_mcp.md](../notes/papers/p2023_peperoni_self_aligning_mcp.md), [p2024_peperoni_iphlex_mcp.md](../notes/papers/p2024_peperoni_iphlex_mcp.md) |
| Reduced-order finger modeling baseline | Explains what level of model is currently defensible | [03_finger_biomechanics_models.md](TOPIC_MEMOS/03_finger_biomechanics_models.md), [01_mcp_1dof_static_hello_world.ipynb](../simulation_modeling/notebooks/01_mcp_1dof_static_hello_world.ipynb), [02_mcp_1dof_static_nonlinear_passive.ipynb](../simulation_modeling/notebooks/02_mcp_1dof_static_nonlinear_passive.ipynb), [reduced_models.py](../simulation_modeling/reduced_models.py) |

### Tier 2: Important Comparison Topics

These should be understood after Tier 1, not before it.

| Topic | Why it matters | How to use it |
| --- | --- | --- |
| Tremor suppression and stabilization devices | Useful if the thesis needs to separate `assist motion` from `suppress unwanted motion` | Comparison bucket, not current main hardware baseline |
| Broader Parkinson assistive/control devices | Helps position the thesis within the disease landscape | Use for symptom framing, control framing, and validation framing |
| Pinch and thumb-index opposition devices | Useful because they are movement-specific and thumb-index oriented | Treat as far-adjacent comparison, not direct tapping precedent |
| Soft hand exoskeleton reviews | Useful for architecture survey and manufacturing context | Good background, but too broad to lead the current thesis story |

Primary resources:

- [p2025_andong_helm_tremor.md](../notes/papers/p2025_andong_helm_tremor.md)
- [p2022_raciti_bradykinesia_exoskeleton_trial.md](../notes/papers/p2022_raciti_bradykinesia_exoskeleton_trial.md)
- [p2022_haarman_tgrip_lateral_pinch.md](../notes/papers/p2022_haarman_tgrip_lateral_pinch.md)
- [p2024_andres_esperanza_pulp_pinch.md](../notes/papers/p2024_andres_esperanza_pulp_pinch.md)
- [p2024_saldarriaga_soft_hand_exoskeleton_review.md](../notes/papers/p2024_saldarriaga_soft_hand_exoskeleton_review.md)

### Tier 3: Open But Not Yet Mature In This Repo

These topics matter to the thesis, but the repo does not yet have a mature synthesis for them. Interns should not assume they are settled.

| Topic | Current state | Intern instruction |
| --- | --- | --- |
| Soft finger actuation | topic memo mostly empty | Screen papers and extract mechanism families carefully |
| Variable-stiffness mechanisms | topic memo mostly empty | Do not claim a chosen mechanism family yet |
| Validation methods | topic memo mostly empty | Collect metric patterns, but do not overstate consensus |
| Controllability framing | promising but still emerging | Tie any suggestion back to simplified modeling and benchtop validation |

Primary resources:

- [01_soft_finger_actuation.md](TOPIC_MEMOS/01_soft_finger_actuation.md)
- [02_variable_stiffness_mechanisms.md](TOPIC_MEMOS/02_variable_stiffness_mechanisms.md)
- [05_validation_methods.md](TOPIC_MEMOS/05_validation_methods.md)
- [p2025_besharati_aansoftfinger.md](../notes/papers/p2025_besharati_aansoftfinger.md)
- [p2024_mccall_softpneumaticextension.md](../notes/papers/p2024_mccall_softpneumaticextension.md)

## Recommended Paper Stack

If interns only have time to read a small stack first, use this order.

### Stack A: Understand The Task

1. [p2020_bologna_bradykinesia_concepts.md](../notes/papers/p2020_bologna_bradykinesia_concepts.md)
2. [p2026_paparella_bradykinesia_complex.md](../notes/papers/p2026_paparella_bradykinesia_complex.md)
3. [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)
4. [p2024_amo_salas_pd_ft_survey.md](../notes/papers/p2024_amo_salas_pd_ft_survey.md)
5. [p2023_ravichandran_itex_gloves.md](../notes/papers/p2023_ravichandran_itex_gloves.md)

What this stack teaches:

- what Parkinson finger tapping measures
- why a one-number slowness interpretation is too weak
- which task-level observables are clinically meaningful
- why assessment literature is stronger than direct assistive hardware here

### Stack B: Understand The Hardware Bridge

1. [p2023_peperoni_self_aligning_mcp.md](../notes/papers/p2023_peperoni_self_aligning_mcp.md)
2. [p2024_peperoni_iphlex_mcp.md](../notes/papers/p2024_peperoni_iphlex_mcp.md)
3. [p2021_sun_self_aligning_index_finger.md](../notes/papers/p2021_sun_self_aligning_index_finger.md)

What this stack teaches:

- why MCP-dominant simplifications are defensible
- how self-alignment changes comfort and reaction forces
- what a credible benchtop validation pattern looks like
- why the repo currently treats these papers as the best mechanical bridge

### Stack C: Understand The Positioning Layer

1. [07_parkinsons_assistive_control_devices.md](TOPIC_MEMOS/07_parkinsons_assistive_control_devices.md)
2. [p2022_raciti_bradykinesia_exoskeleton_trial.md](../notes/papers/p2022_raciti_bradykinesia_exoskeleton_trial.md)
3. [p2025_andong_helm_tremor.md](../notes/papers/p2025_andong_helm_tremor.md)

What this stack teaches:

- where the thesis sits in the broader Parkinson device landscape
- why assistance and stabilization are different design problems
- why broader Parkinson papers are mainly positioning sources rather than direct mechanism precedents

## Suggested Briefing Agenda

For a live 45 to 60 minute intern briefing:

1. Thesis scope and non-goals
2. Why finger tapping is the current task-framing lens
3. Why the direct tapping-assist hardware literature is sparse
4. Why MCP/index-finger rehab devices are the current mechanical bridge
5. What the current reduced-order modeling baseline is
6. Which literature buckets are core, comparison, and still immature
7. What interns should update when they read new papers

## Repo Workflow Interns Should Follow

When interns read a paper, they should not write directly into synthesis docs from memory.

Correct workflow:

1. Find the paper in [PAPER_TRACKER.csv](../refs/PAPER_TRACKER.csv)
2. Open or create the corresponding note in `notes/papers/`
3. Add source-backed summary, exact quotes, page numbers, and thesis relevance
4. Update tracker status if the read state changed
5. Promote only verified claims into [STUDY_GUIDE.md](STUDY_GUIDE.md) or a topic memo

Files that matter operationally:

- [PAPER_TRACKER.csv](../refs/PAPER_TRACKER.csv)
- [paper_note_template.md](templates/paper_note_template.md)
- [CLAIM_REGISTRY.md](CLAIM_REGISTRY.md)
- [ZOTERO_SYNC.md](ZOTERO_SYNC.md)

## What Interns Should Not Assume

- There is not yet a strong direct paper bucket of `Parkinson finger-tapping assist exoskeletons`.
- The thesis is not choosing pinch devices as the main precedent class.
- The thesis is not currently claiming that variable stiffness has already been narrowed to one mechanism family.
- The thesis is not trying to solve all of Parkinson rehabilitation hardware.
- The simulation track is still intentionally reduced-order and interpretable.

## Good Starter Tasks For Interns

- classify one unassigned paper into the correct topic bucket
- strengthen note quality for a high-priority paper already in the tracker
- extract validation metrics from a near-adjacent hardware paper
- compare assistance versus stabilization logic across two papers
- summarize what a paper changes for modeling assumptions, if anything

## Bad Starter Tasks For Interns

- proposing a full glove architecture
- drafting a broad unsourced Parkinson survey
- jumping to FEM because the reduced model feels simple
- writing thesis prose from memory without checked notes
- treating assessment systems as if they were hardware assistance precedents

## Current Open Questions

- Is the best thesis-facing task label `finger tapping`, `tapping-like repetitive finger motion`, or a broader repetitive voluntary finger-motion phrasing?
- How much of the final thesis framing should stay Parkinson-specific versus broader neurorehabilitation?
- Which variable-stiffness mechanism family is realistic enough for thesis-scale prototyping?
- Which benchtop outputs should be treated as primary validation targets?

## Bottom Line

If an intern remembers only five things, they should remember these:

1. The thesis is about simplified actuator-finger interaction, not a full product.
2. Parkinson finger tapping is mainly the task-framing lens.
3. The strongest direct literature is on assessment, not tapping assistance hardware.
4. The strongest hardware bridge is MCP and index-finger rehabilitation devices.
5. The repo requires note-first, evidence-first literature work.
