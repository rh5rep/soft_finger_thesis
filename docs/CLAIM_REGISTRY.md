# Claim Registry

This file is the cross-paper bridge between individual notes and thesis-facing synthesis.

Rules:

- Only log claims here when they are backed by at least one paper note with page-level support.
- Separate `source claim` from `project interpretation`.
- Add contradictions or scope caveats when papers disagree.
- Treat this file as a synthesis ledger, not as a place for unattributed brainstorming.

## Registry Entries

### C001 - Bradykinesia Is Not One Scalar Variable

- Claim: Bradykinesia should not be treated as a single pure slowness variable because it includes separable abnormalities such as reduced amplitude and sequence effect.
- Sources:
  - [p2020_bologna_bradykinesia_concepts.md](../notes/papers/p2020_bologna_bradykinesia_concepts.md)
  - [p2026_paparella_bradykinesia_complex.md](../notes/papers/p2026_paparella_bradykinesia_complex.md)
- Support notes:
  - Bologna 2020 frames bradykinesia through slowness, reduced amplitude, and sequence effect.
  - Paparella 2026 argues for using `bradykinesia and associated features` more carefully than narrow single-term usage.
- Thesis use:
  - Parkinson finger-tapping framing
  - justification for multidimensional outcome definitions

### C002 - Sequence Effect Is A Distinct Repetitive-Movement Phenomenon

- Claim: Sequence effect is the progressive decrement of movement amplitude and/or speed during repeated movement, and it should be handled as a distinct feature rather than folded into generic slowness.
- Sources:
  - [p2020_bologna_bradykinesia_concepts.md](../notes/papers/p2020_bologna_bradykinesia_concepts.md)
  - [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)
- Support notes:
  - Bologna 2020 gives the clinical framing.
  - Zarrat 2026 operationalizes sequence-effect features in a direct finger-tapping analysis pipeline.
- Thesis use:
  - tapping task decomposition
  - simulation output candidates
  - validation metrics

### C003 - Task-Level Tapping Signals Can Be More Practical Than Joint-Level Kinematics

- Claim: Direct Parkinson finger-tapping assessment literature can extract clinically meaningful information from task-level thumb-index signals rather than full joint-level biomechanical state estimation.
- Sources:
  - [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)
  - [p2024_amo_salas_pd_ft_survey.md](../notes/papers/p2024_amo_salas_pd_ft_survey.md)
- Support notes:
  - Zarrat 2026 uses normalized thumb-index distance as the central signal.
  - Amo-Salas 2024 maps the vision-assessment literature around task-focused finger-tapping measurement.
- Thesis use:
  - simplified modeling scope
  - task-level validation framing

### C004 - Direct Parkinson Finger-Tapping Literature Is Stronger In Assessment Than Assistance

- Claim: The strongest direct Parkinson finger-tapping literature in this repo is currently on assessment, measurement, and symptom decomposition rather than tapping-specific assistive hardware.
- Sources:
  - [p2024_amo_salas_pd_ft_survey.md](../notes/papers/p2024_amo_salas_pd_ft_survey.md)
  - [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)
  - [docs/STUDY_GUIDE.md](./STUDY_GUIDE.md)
- Support notes:
  - assessment papers are deeper and more numerous than tapping-specific assistance precedents
  - existing hardware precedents are mostly near-adjacent rather than direct Parkinson tapping assistance devices
- Thesis use:
  - review positioning
  - scope defense

### C005 - Distance-Based Tapping Signals Are A Strong Baseline Measurement Choice

- Claim: Distance-based thumb-index signals are a robust and empirically strong measurement choice for video-based finger-tapping assessment.
- Sources:
  - [p2026_zarrat_ehsan_npj_pd_finger_tapping.md](../notes/papers/p2026_zarrat_ehsan_npj_pd_finger_tapping.md)
- Support notes:
  - Zarrat 2026 reports better performance for distance-based than angle-based signals across tested classifiers.
- Thesis use:
  - simulation-to-measurement bridge
  - future experimental measurement design
