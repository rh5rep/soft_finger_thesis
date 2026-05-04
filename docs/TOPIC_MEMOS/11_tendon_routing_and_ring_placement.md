# Tendon Routing And Ring Placement For Index-Finger Assistance

## Question

How should tendon routing, soft ring placement, and a distal thimble interface be modeled before choosing the first index-finger prototype architecture?

## Status

Working research and design memo. This is not yet a mechanism decision.

2026-04-24 update: the v0 code now treats the tendon as an ordered `RoutingPath` made from `RoutingElement`s with explicit roles such as `entry`, `guide`, and `anchor`. In this memo, `ring`, `guide`, and `routing support` should be read as physical design candidates; in the code, they are represented first as effective points that capture net path redirection.

2026-04-28 clarification: distinguish independent tension inputs from physical routing branches. The current intended architecture is one flexion input from an actuator or TSA that may split into left/right side branches. Those branches add their moment-arm contributions, but they do not create independent MCP/PIP/DIP control unless they are driven by independently controlled tensions.

## Why This Matters Now

The current design question is no longer just whether a tendon-driven soft glove can work. The useful thesis question is narrower:

- how many independent inputs, routing branches, and routing supports are needed on one index finger
- whether those supports should sit dorsally, laterally, palmar-laterally, or in a combined path
- whether a fingertip thimble alone is enough, or whether intermediate rings are required to create useful joint moment arms
- whether a passive thumb pad or passive thumb opposition structure is enough for pinch-like validation
- how routing geometry changes fingertip force, finger curvature, tendon stroke, slack, and comfort

This fits the simulation-first thesis scope because the routing can be represented with an interpretable reduced-order model before committing to a physical glove.

The current design argument is that routing should become a comparison problem:

```text
candidate routing -> branch lengths, excursion, dL/dq, tension estimate, comfort/complexity proxy
```

That is more defensible than presenting one intuitive tendon path as if it already proves the hardware layout.

## Field Map

Recent and relevant sources cluster into five groups.

| Source cluster | Representative papers | Why it matters |
|---|---|---|
| ExoGlove lineage | Kang et al. 2019, `Exo-Glove Poly II` | Strong direct precedent for polymer glove, thimbles, passive thumb opposition, underactuated tendon routing, and a single-finger kinematic model for wire-length/slack optimization. |
| New tendon-routing soft gloves | Bagneschi et al. 2023 | Directly relevant to soft open rings, side-routed tendons or cords through guide elements, hand-dorsum actuator placement, grasping force, wearing stability, and ring deformation. |
| Bioinspired exotendon routing | Abdelhafiz et al. 2023 | Directly relevant to routing tendons on radial/ulnar sides of a finger to better coordinate MCP/PIP/DIP flexion and extension while avoiding abnormal hyperextension. |
| Tendon path comparison and robotic-finger models | Zhou et al. 2024; Gallup et al. 2025 | Useful for treating tendon path as a design variable and using quasi-static tendon-tension models rather than only qualitative sketches. |
| Adjacent pinch/thumb and mechanism alternatives | Sanders and Reinkensmeyer 2024; Ferguson et al. 2024; CASPHEX 2025 | Relevant for passive thumb opposition, index-thumb pinch validation, and mode switching between hand opening and closing, even when the mechanism is not exactly a soft tendon glove. |

## Source-Backed Observations

### Exo-Glove Poly II, Kang et al. 2019

Exo-Glove Poly II is directly relevant because it combines:

- a polymer glove body
- distal thimbles
- tendon-driven index and middle finger flexion/extension
- a passive thumb structure for opposition
- a single-finger kinematic model used to estimate flexion and extension wire-length changes
- actuator-side pulley/slack optimization for different hand sizes

Key modeling lesson:

`wire path length is a function of finger posture, strap or guide placement, fingertip/thimble anchor location, finger size, and actuator pulley geometry`

For this thesis, the most useful part is not copying the full glove. It is the structure of the kinematic question: define routing points, compute changing tendon path length as joint angles change, then evaluate whether actuator stroke/slack and singularity constraints remain acceptable.

Source links:

- https://doi.org/10.1089/soro.2018.0006
- https://journals.sagepub.com/doi/10.1089/soro.2018.0006

### Bagneschi et al. 2023

Bagneschi et al. are especially relevant because the paper explicitly studies a new tendon layout and soft polymer open rings. The routing folds laterally around both sides of the hand and adds a clenching/stabilizing component when the tendon is loaded. The paper also reports FEM and experiments for ring behavior, glove stability, inter-finger compliance, and grasping force.

Design lesson:

- rings are not just passive holders; their stiffness and placement change both tendon stability and user comfort
- lateral routing can keep tendons closer to the hand and reduce slippage into the grasping workspace
- the number of rings is a tradeoff between routing control, hand-size adaptability, and closure interference

For this thesis, this paper is the strongest current source for the idea of soft open rings as modular tendon guides rather than a full glove sleeve.

Source links:

- https://doi.org/10.1109/TOH.2023.3273908
- https://pubmed.ncbi.nlm.nih.gov/37163404/
- https://www.iris.sssup.it/handle/11382/555071

### Abdelhafiz et al. 2023

Abdelhafiz et al. propose a biomimetic tendon-based mechanism for flexion and extension with one motor. The paper is useful because it argues that a traditional single distal tendon path can create abnormal joint sequencing, while a more bioinspired radial/ulnar routing can coordinate flexion and extension more naturally. The mechanism uses lateral routing and guide elements around the finger to approximate extrinsic tendon functions.

Design lesson:

- the location of intermediate guides strongly affects which joint flexes first and how much DIP motion is produced for a given PIP angle
- routing can be used to avoid hyperextension and unnatural joint coupling
- a one-finger experimental setup is enough to evaluate whether routing produces acceptable trajectories before building a full glove

Source link:

- https://pmc.ncbi.nlm.nih.gov/articles/PMC9960426/

### Zhou et al. 2024

Zhou et al. compare multiple tendon transmission paths for a tendon-driven robotic finger based on grasping-task data. The useful thesis point is not the exact robotic finger design, but the method: treat tendon path as an explicit design variable and compare tension fluctuation, joint angle control, and friction behavior.

Design lesson:

`routing optimization should compare multiple path families under the same task and finger geometry, not only draw one plausible path`

Source links:

- https://doi.org/10.3390/biomimetics9060370
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11201696/

### Gallup et al. 2025

Gallup et al. are relevant on the modeling side. They model a three-link tendon-driven finger with compliant joints using quasi-static virtual work. The paper identifies joint compliance experimentally, represents joints as hinges plus nonlinear torsional springs, and validates tendon-tension-to-flexion predictions.

Design lesson:

- the first simulation can be low-order and still defensible
- tendon tension, joint stiffness, and geometry can be separated cleanly
- experimental validation can use image-tracked marker positions and tendon loads
- object contact and fingertip force can be added later after free-motion routing behavior is understood

Source link:

- https://doi.org/10.1016/j.rineng.2025.106979

## Common Modeling Approaches

### 1. Pure Kinematic Routing Model

Purpose:

- predict tendon stroke as a function of joint angles and routing points
- compare guide/ring count and location
- identify slack or singularity problems early

Minimal variables:

```text
q = [theta_MCP, theta_PIP, theta_DIP]
L = [metacarpal/proximal/middle/distal segment lengths]
g_i = tendon guide or ring points attached to each segment
a = distal thimble anchor point
x_tendon(q, g_i, a) = total tendon path length
Delta x = x_tendon(q) - x_tendon(q_neutral)
```

Current code abstraction:

```text
RoutingPath = ordered sequence of RoutingElement
RoutingElement.kind = entry | guide | anchor
RoutingElement.body = world | proximal | middle | distal
```

This distinction matters because a world entry, a pass-through guide, and a terminal thimble anchor have different mechanical meanings even if all are represented as 2D points in v0.

Useful outputs:

- tendon stroke
- path curvature or bend count
- guide contact changes
- whether a path loses a useful moment arm

### 2. Quasi-Static Tendon Force Model

Purpose:

- estimate joint torques and fingertip force for a given tendon force
- compare dorsal, palmar-lateral, and side-routed paths
- see whether one routing overdrives DIP/PIP or underdrives MCP

Minimal relationship:

```text
tau(q) = r(q)^T F_tendon
tau_passive(q) = K_passive(q - q0)       # first pass
tau_act(q) - tau_passive(q) = 0          # free motion
J_tip(q)^T F_tip = tau_act(q)            # fingertip output estimate
```

For a multi-joint finger, `r(q)` is not necessarily constant. It can be computed from tendon path length:

```text
tau_i = -F_tendon * partial x_tendon / partial theta_i
```

This is the cleanest bridge between ExoGlove-style kinematic routing and Gallup-style quasi-static equilibrium.

If one independent input splits into multiple branches, compute the relationship branch by branch:

```text
R_j(q) = -partial L_j(q) / partial q
R_total(q) = sum_j R_j(q)
tau_tendon(q, T) = T * R_total(q)
```

The branch index `j` can be implemented explicitly as `left` and `right` in code. The more important model output is branch imbalance, such as `abs(L_left - L_right)` or `abs(s_left - s_right)`, because imbalance hints at slack, yoke motion, or uneven loading.

Current sanity checks:

- zero angles mean a straight finger along `+x`
- positive rotation is counterclockwise
- negative joint angles represent physiological flexion for the current palmar routing choice
- the current palmar/flexion path shortens during flexion
- the current dorsal/extension path lengthens during flexion
- gradients are smooth and posture-dependent over the coordinated sweep
- MCP influence is currently strongest, which is plausible because proximal rotation moves all downstream routing elements

### 3. Series-Stiffness Transmission Model

Purpose:

- introduce variable stiffness without immediately building a complex soft actuator
- compare soft/medium/stiff transmission behavior
- evaluate controllability and interaction force

Minimal relationship:

```text
F_tendon = K_series(c) * (x_actuator(u) - x_tendon(q))
tau_i = -F_tendon * partial x_tendon / partial theta_i
```

where `c` is the stiffness setting or interchangeable elastic element.

### 4. Passive Thumb / Thumb Pad Model

Purpose:

- support pinch-like validation without active thumb actuation
- keep thesis scope on the index-finger actuator

Minimal version:

- represent the thumb as a fixed or adjustable contact surface
- evaluate index fingertip position, normal force direction, and contact stability against that surface
- only add thumb kinematics if pinch validation requires it

This is consistent with the passive thumb strategy in Exo-Glove Poly II and the passive thumb support in IGripX.

## Candidate Routing Families To Simulate

| Routing family | Physical idea | Expected effect | Main risk |
|---|---|---|---|
| Distal thimble only | tendon anchored at fingertip/thimble, minimal intermediate supports | simplest hardware and simulation baseline | likely poor joint distribution, path bowstringing, weaker control of curvature |
| Two-ring palmar-lateral route | one guide near proximal phalanx, one near middle/distal phalanx, plus thimble | better flexion moment arms; simple enough to prototype | may interfere with palmar contact or thumb-index pinch |
| Three- or four-ring side route | side-routed cords through guides distributed along phalanges, inspired by ExoGlove/Bagneschi/Abdelhafiz | tunable joint sequencing and curvature | more friction, donning complexity, possible closure interference |
| Dorsal extension route | dorsal tendon path to thimble or distal guide | useful for opening/return support | does not solve active flexion alone |
| Antagonistic flexion + extension route | palmar-lateral flexion path plus dorsal extension path | true bidirectional control and variable apparent stiffness through co-tension | higher mechanism and control complexity; likely stage 2 |
| Lateral folded hand route | Bagneschi-style lateral fold around the hand/palm | improves wearing stability and keeps tendons away from grasp workspace | full-hand path may be overkill for an index-only mock-up |

## What Seems Realistic For This Thesis

The most defensible next simulation should be an index-finger design sandbox, not a full glove model.

Recommended first model:

1. three-link planar index finger with MCP/PIP/DIP
2. passive joint stiffness at each joint, initially linear or simple nonlinear
3. configurable tendon guide points attached to each phalanx
4. distal thimble anchor point
5. optional passive thumb pad as fixed contact geometry
6. tendon path length, moment arms, and equilibrium solved in Python

Recommended first routing comparison:

| Variant | Include | Why |
|---|---|---|
| V0 | thimble-only distal tendon | lower-bound baseline |
| V1 | two side/palmar-lateral rings plus thimble | likely simplest buildable flexion route |
| V2 | three/four rings plus thimble | tests whether added guides improve curvature enough to justify complexity |
| V3 | V1 plus dorsal elastic/extension return | tests tapping-like repeated flexion/extension without a second motor |
| V4 | antagonistic flexion/extension tendons | simulation-only stage 2 unless V1/V3 fail |

## What To Optimize

Primary design variables:

- number of rings
- ring longitudinal positions along the finger
- ring side offset relative to finger centerline
- thimble anchor position
- tendon entry location
- routing-element role: entry, guide, anchor, and later wrap/contact if needed
- tendon pretension/slack
- series stiffness setting
- passive thumb pad position, if pinch is included

Primary outputs:

- fingertip trajectory
- fingertip force against a fixed pad or object
- MCP/PIP/DIP angle distribution
- tendon stroke required
- peak tendon tension required
- estimated passive/restoring torque
- curvature smoothness or joint-angle ratio
- palmar clearance for object or thumb contact

Secondary outputs:

- sensitivity to hand length and finger segment lengths
- sensitivity to ring placement error
- estimated friction or number of high-curvature guide contacts
- contact interference from rings during full flexion

Presentation-safe current interpretation:

- The current model passes an internal reduced-order sanity check, not an anatomical validation check.
- The output is already useful because it produces actuator-relevant quantities: path length, excursion, `dL/dq`, and torque per unit tendon tension.
- It should now be used to rank alternatives under explicit criteria before deciding ring count, placement, cord strength, TSA feasibility, or variable-transmission needs.

## Tradeoffs

- More rings can improve path control and reduce bowstringing, but increase friction, donning burden, and possible interference.
- A palmar route gives clearer flexion moment arms, but may block pinch/tapping contact if it occupies the finger pad side.
- A lateral route preserves palmar contact better, but the resulting moment arms may depend strongly on finger thickness and ring offset.
- A dorsal route is cleaner for extension or return support, but does not directly flex the finger unless paired with another mechanism.
- A passive thumb pad is a good first validation target, but it should not be allowed to turn the project into a thumb exoskeleton.
- A one-motor antagonistic path is elegant but brings slack/singularity problems; Exo-Glove Poly II is useful precisely because it shows this needs explicit kinematic analysis.

## Design Implications

1. Drawings and simulations should define joint axes, guide points, tendon line of action, and torque direction. A visual concept without moment arms is not enough.
2. The first Python model should compute tendon path length and `partial x_tendon / partial theta_i`; this gives both actuator stroke and joint torque distribution from the same geometry.
3. The physical mock-up should probably start with an index thimble plus two or three removable soft rings, not a sewn full glove. That preserves the ability to move rings and test the model.
4. A passive thumb pad is reasonable for pinch-like tests, but the initial optimization should still be index-finger centered.
5. Do not equate every modeled routing element with a separate physical ring. The next prototype can use fewer physical parts than the effective-point model if the same net path and retention behavior are preserved.
6. TSA, CVT, and CTA options should be screened after the model estimates stroke and tendon load, not before.

## Open Gaps

- What ring geometry gives enough tendon guidance without uncomfortable pressure?
- Is side routing sufficient for palmar flexion torque, or does it need a partially palmar-lateral path?
- How much ring friction can be ignored in the first model?
- Should the initial passive stiffness represent human finger tissues, the soft rings/sleeve, or the combined human-device system?
- Which target motion should tune the first routing: pinch closure, tapping-like flexion/extension, or a generic curl?
- How should hand-size variability enter the model: absolute segment lengths, normalized ring positions, or both?

## Candidate Next Decision

Should the first simulation branch model a side/palmar-lateral flexion tendon with two to three removable soft rings and a distal thimble as the primary candidate, while keeping dorsal extension and antagonistic routing as secondary comparison branches?
