# DECISION_LOG

Use this as an append-only decision log. Add new entries to the bottom.

---

## Decision Template

**Decision ID:** DEC-000

**Date:** YYYY-MM-DD

**Question:**  
What question is being answered now?

**Options Considered:**  
List the realistic alternatives that were seriously considered.

**Evidence:**  
Summarize the literature, experimental, or practical evidence used.

**Chosen Option:**  
State the selected path clearly.

**Rationale:**  
Why this option is best now, given thesis constraints.

**Risks Introduced:**  
What this choice may hide, weaken, or postpone.

**Revisit Trigger:**  
What new evidence, failure, or milestone would justify changing this decision?

---

## Decision ID: DEC-001

**Date:** 2026-03-27

**Question:**  
How should the repo represent ongoing thesis work now that both literature operations and simulation modeling are active?

**Options Considered:**  
1. Keep the repo framed primarily as a literature-review system and treat simulation work as ad hoc.  
2. Split the repo into separate literature and modeling repos.  
3. Keep one repo but define explicit workstreams for literature and simulation modeling, while preserving one primary task in `docs/CURRENT_TASK.md`.

**Evidence:**  
The repo already contains a substantial literature pipeline (`refs/SEARCH_TOPICS.csv`, `refs/PAPER_TRACKER.csv`, Zotero sync scripts, topic memos) and now also contains an active simulation notebook at `simulation_modeling/notebooks/01_mcp_1dof_static_hello_world.ipynb`. The previous documentation described the literature flow clearly but underrepresented the simulation track.

**Chosen Option:**  
Keep one repo with two explicit workstreams: `Literature` and `Simulation Modeling`, while using `docs/CURRENT_TASK.md` to track only the single primary task at any given time.

**Rationale:**  
This keeps the thesis workflow coherent in one place, preserves the existing literature automation and tracker setup, and makes the simulation work visible without abandoning the one-task-at-a-time rule needed for focus.

**Risks Introduced:**  
The repo could still drift if secondary work becomes active without a clear primary task, or if workstream boundaries are described inconsistently across files.

**Revisit Trigger:**  
Revisit if the simulation codebase grows into a larger tested package, if literature automation becomes complex enough to need separate operational docs, or if the single-primary-task rule becomes a bottleneck.

---

## Decision ID: DEC-002

**Date:** 2026-04-03

**Question:**  
How should the next literature push respond to supervisor feedback asking for broader Parkinson assistive or control-device context?

**Options Considered:**  
1. Stay narrowly focused on finger tapping, finger devices, and adjacent pinch papers.  
2. Pivot to a broad Parkinson technology survey with no strong filter for thesis relevance.  
3. Build a symptom-centered Parkinson device landscape review, then use it to sharpen thesis positioning and research questions while keeping finger-device papers as the main mechanical precedents.

**Evidence:**  
The current repo literature already shows that direct Parkinson finger-tapping assistive hardware is sparse, while broader Parkinson device literatures are much richer in assessment systems, cueing devices, gait-focused rehabilitation robots, tremor-suppression systems, and adaptive control methods. Representative examples include gravity-supporting upper-extremity exoskeleton training in Parkinson's disease, gait cueing devices such as laser-based wearable or cane systems, and adaptive deep brain stimulation trials. These sources are useful for symptom framing and control logic, but most are weak direct precedents for a simplified finger actuator.

**Chosen Option:**  
Build a broader Parkinson device landscape review that informs thesis framing and research-question development, while keeping finger and hand rehabilitation devices as the primary hardware precedents.

**Rationale:**  
This directly addresses supervisor feedback without letting the thesis drift into an unbounded survey. It preserves the current simulation-first finger-actuator scope, but situates it within the broader Parkinson device ecosystem and clarifies which Parkinson-specific themes actually matter for modeling, control, and validation.

**Risks Introduced:**  
The broader Parkinson literature could pull attention toward gait, wearable monitoring, or invasive neuromodulation more than the thesis can realistically use. It could also blur the difference between disease positioning and direct mechanism precedent.

**Revisit Trigger:**  
Revisit if the broadened Parkinson review still fails to clarify the thesis target symptom, if supervisors request a disease-agnostic framing instead, or if a stronger direct Parkinson finger-assistance literature cluster emerges.

---

## Decision ID: DEC-003

**Date:** 2026-04-06

**Question:**  
How should the thesis maintain a living literature study guide without losing citation safety or relying on scattered chat history?

**Options Considered:**  
1. Keep the main study guide inside ChatGPT or Canvas and treat the repo as secondary storage.  
2. Use Zotero notes alone as the main knowledge base.  
3. Keep the repo as the canonical study-guide and audit system, use Zotero for bibliographic storage and PDFs, and treat ChatGPT or Canvas as an optional mirror or drafting surface.

**Evidence:**  
The current repo already contains a literature tracker, topic memos, paper-note paths, and thesis decision files. The user's stated requirement is to preserve exact citations and exact quotes without hallucination so the material can be reused safely in thesis writing. Chat conversation history is not a stable or auditable evidence store for quote-level work. Zotero is strong for bibliography and PDF storage, but weaker as the sole home for thesis-facing synthesis across topics and decisions.

**Chosen Option:**  
Keep the repo as the canonical literature study-guide and audit system, use Zotero as the source of truth for PDFs and bibliographic metadata, and use ChatGPT or Canvas only as an optional mirrored workspace for drafting or review.

**Rationale:**  
This keeps the evidence trail local, inspectable, and versionable. It also separates roles cleanly: Zotero stores sources, per-paper notes store quote-level evidence, and the study guide stores thesis-facing synthesis. That structure is the safest fit for a literature review that must support later writing without relying on memory.

**Risks Introduced:**  
The workflow adds maintenance overhead, and duplicate copies could drift if ChatGPT or Canvas is updated without syncing back to the repo. It also requires discipline to avoid writing synthesis before quote or page verification is complete.

**Revisit Trigger:**  
Revisit if the repo workflow becomes too heavy to maintain, if a better citation-safe single system replaces this split, or if thesis drafting reveals that the study guide needs a different level of granularity.

---

## Decision ID: DEC-004

**Date:** 2026-04-06

**Question:**  
How should the repo name and track per-paper notes so they remain readable without losing Zotero traceability?

**Options Considered:**  
1. Keep Zotero-key filenames such as `IF5PMF4P.md`.  
2. Allow a mix of key-based names and manually named readable notes.  
3. Standardize on human-readable note filenames and keep Zotero keys in note metadata and the tracker.

**Evidence:**  
The repo had drifted into a mixed state: some papers used key-only filenames, some used readable names, and several papers had both a key-based scaffold and a richer readable duplicate note. This made folder browsing harder, weakened link clarity, and created ambiguity about which note was canonical.

**Chosen Option:**  
Standardize on human-readable note filenames in `notes/papers/`, while keeping Zotero keys in the note metadata and `refs/PAPER_TRACKER.csv`.

**Rationale:**  
Human-readable filenames are easier to browse, link, and audit during thesis writing. Keeping the Zotero key in metadata preserves precise traceability back to the bibliographic source without forcing the filesystem naming scheme to carry that burden.

**Risks Introduced:**  
Path migrations can break links if the tracker and internal references are not updated together. Filename heuristics may also produce imperfect short titles for future papers unless reviewed.

**Revisit Trigger:**  
Revisit if future sync behavior keeps producing confusing filenames, if collisions become common, or if a stronger need emerges for machine-oriented rather than human-oriented note naming.

---

## Decision ID: DEC-005

**Date:** 2026-04-06

**Question:**  
How should per-paper literature notes distinguish source-backed evidence from thesis interpretation as the review becomes more detailed?

**Options Considered:**  
1. Keep paper notes as lightweight mixed summaries with no strong boundary between paper claims and project interpretation.  
2. Move deep paper reviews into a separate parallel note system outside `notes/papers/`.  
3. Keep one note per paper in `notes/papers/`, but expand the schema so notes explicitly separate source-backed claims, exact quotes, mechanistic insights, project interpretation, and open questions, while also promoting recurring cross-paper claims into a shared registry.

**Evidence:**  
The current paper-note system is useful for auditability, but deeper thesis writing now needs a clearer separation between what a paper directly says and what the thesis infers from it. Recent high-priority notes such as Bologna 2020 and Zarrat 2026 also show that the most useful papers need more than a short summary and quote bank; they need structured sections for definitions, claims, interpretation, and thesis relevance. Creating a second parallel note system would recreate the fragmentation problem the repo is trying to eliminate.

**Chosen Option:**  
Keep one canonical note per paper in `notes/papers/`, expand the note schema to separate source-backed evidence from project interpretation, and add a shared `docs/CLAIM_REGISTRY.md` for recurring cross-paper claims.

**Rationale:**  
This preserves one source of truth per paper while making deep reading notes safer to reuse in writing. It also creates a clean path from paper-level extraction to cross-paper synthesis without depending on chat memory or mixing unsupported interpretation into source claims.

**Risks Introduced:**  
The richer schema increases note-maintenance overhead, and lower-priority papers could become overworked if the same depth is applied everywhere. The workflow therefore still needs tiering by paper priority and PDF availability.

**Revisit Trigger:**  
Revisit if the richer note schema becomes too heavy for everyday screening, if the claim registry grows unwieldy, or if thesis drafting reveals that a different split between paper notes and synthesis files would be more maintainable.

---

## Decision ID: DEC-006

**Date:** 2026-04-22

**Question:**  
What should the first multi-joint biomechanical model be for the tendon-routing simulation branch?

**Options Considered:**  
1. Jump directly to a higher-fidelity anatomical or 3D model with more detailed tissue, friction, or dynamic effects.  
2. Keep working only with a 1-DOF proxy and postpone multi-joint routing geometry.  
3. Use a reduced-order planar 2D index-finger model with three rigid phalanges, three revolute joints, one routed tendon, fixed guide points on the phalanges, a distal thimble anchor, and quasi-static interpretation.

**Evidence:**  
The thesis scope explicitly favors a simplified finger system, simulation first, and interpretable reduced-order models over full FEM or anatomically exhaustive models. Recent work in `simulation_modeling/v0_model.py` shows that the planar routing model is already sufficient to compute forward kinematics, fingertip trajectory, tendon path length, tendon excursion, segment-wise path changes, and the local numerical gradient `dL/dq`. The current routing also behaves physically under the chosen sign convention: physiological flexion shortens the palmar path smoothly and monotonically.

**Chosen Option:**  
Use the reduced-order planar 2D three-link tendon-routing model as the baseline multi-joint simulation abstraction, and treat tendon geometry and sensitivity as the completed first stage before adding passive mechanics and equilibrium solving.

**Rationale:**  
This model is simple enough to understand, parameterize, and compare across routing variants, but rich enough to answer early thesis questions about tendon stroke, posture dependence, routing sensitivity, and how tendon tension will map into generalized joint torque. It is the smallest defensible model that creates a clean bridge from geometry to mechanics.

**Risks Introduced:**  
The model ignores out-of-plane motion, tendon wrap/friction, soft tissue deformation, tendon stretch, and dynamic effects. It may overstate geometric cleanliness relative to a real soft prototype, and the present routing sensitivity reflects the chosen guide locations rather than an experimentally validated transmission.

**Revisit Trigger:**  
Revisit if passive-torque or bench-top results show that planar geometry is insufficient, if routing friction or slack dominates behavior, if a supervisor requires a stronger anatomical justification, or if extending to antagonistic flexor-extensor routing exposes limitations that the current abstraction cannot handle cleanly.

---

## Decision ID: DEC-007

**Date:** 2026-04-24

**Question:**  
How should the current tendon-routing model influence hardware and actuator choices before the first lab presentation and prototype decision?

**Options Considered:**  
1. Present the current routing as one plausible hardware concept and proceed directly toward a TSA or variable-transmission prototype.  
2. Keep the model as a visualization-only explanation of the finger and tendon path.  
3. Use the model as a design-screening framework that compares candidate routings using explicit metrics before selecting ring count, placement, cord strength, and actuator architecture.

**Evidence:**  
The current v0 model already computes forward kinematics, effective routing-element world positions, tendon path length, excursion relative to neutral, central-difference `dL/dq`, tendon torque per unit tension, coordinated flexion sweeps, and summary plots. The latest sanity checks show the palmar/flexion path shortening during physiological flexion, the dorsal/extension path lengthening, and smooth posture-dependent gradients. The thesis scope also favors reduced-order modeling before physical mock-up validation, and the tendon-routing memo shows that ring placement, thimble anchoring, and tendon entry location should be treated as design variables rather than fixed intuition.

**Chosen Option:**  
Use the current reduced-order routing model as a design-screening framework. Candidate routing designs should be compared by excursion, posture-dependent leverage, rough tendon tension demand, smoothness/monotonicity, palmar clearance, and hardware complexity before committing to TSA, CVT/CTA, soft pneumatic actuation, or a simpler tendon-series-stiffness branch.

**Rationale:**  
This makes the model defensible as an engineering tool instead of a visual aid. It directly links simulation outputs to prototype decisions: ring count, routing-element placement, thimble/anchor location, tendon stroke, cord load, and actuator plausibility. It also prevents the thesis from treating TSA or variable transmission as a premise before the routing mechanics show whether those added mechanisms are needed.

**Risks Introduced:**  
The comparison metrics may create false precision if the model is not later calibrated against passive stiffness, tendon friction, slack, or bench-top measurements. The effective-point abstraction may also hide local ring deformation, contact pressure, and comfort issues.

**Revisit Trigger:**  
Revisit if routing rankings change after passive torque and equilibrium are added, if bench-top measurements show friction/slack dominates the behavior, if fabrication constraints make the best simulated routing impractical, or if supervisor feedback prioritizes a specific actuator identity over routing optimization.

---

## Decision ID: DEC-008

**Date:** 2026-04-28

**Question:**  
How should the model distinguish one actuator input from multiple physical tendon branches around the finger?

**Options Considered:**  
1. Treat every visible cord or side route as a separate tendon input.  
2. Treat the entire flexion route as one unbranched tendon path.  
3. Model one independent flexion tension input that may split into multiple physical routing branches, with the branch moment-arm vectors summed into one total actuation map.

**Evidence:**  
The intended hardware concept is one actuator-side flexion input, likely from a motor/spool or TSA, that may split into left/right side routes around the index finger before reaching the distal thimble or guide layout. This is mechanically different from two independently controlled tendons: branch geometry can add torque contributions and affect slack or balance, but it does not add independent joint control unless the branches have separately controlled tensions.

**Chosen Option:**  
Model the v0 flexion architecture as one independent tension input with one or more physical branches. For branch `j`, compute `L_j(q)` and `R_j(q) = -partial L_j(q) / partial q`; then use `R_total(q) = sum_j R_j(q)` and `tau_tendon(q, T) = T * R_total(q)`.

**Rationale:**  
This keeps the simulation aligned with the intended hardware while preserving the underactuation argument. It also creates a clean way to compare one-side, two-side, and later extension routes without confusing actuator count, input count, and branch count.

**Risks Introduced:**  
The equal-tension branch assumption may be too optimistic if the real splitter or yoke does not equalize tension, if one branch goes slack, or if friction and guide deformation dominate. Branch imbalance must therefore become a reported design metric and later an experimental check.

**Revisit Trigger:**  
Revisit if a physical splitter is chosen, if left/right branch lengths diverge substantially, if bench tests show one side loads before the other, or if antagonistic extension is added with independently controlled flexion and extension inputs.
