# Variable-Stiffness Finger Design Concepts

## Question

Which early variable-stiffness finger-actuator concepts are worth comparing before freezing the first prototype architecture?

## Status

Working design memo for supervisor discussion. This is not yet a mechanism decision.

2026-04-24 update: the current recommendation is to size and compare the routing mechanics before selecting a TSA, CVT/CTA, pneumatic, or series-stiffness actuation architecture. Variable stiffness remains central, but v0 should first establish tendon stroke, posture-dependent leverage, and rough tension requirements.

2026-04-28 clarification: TSA remains a reasonable preferred tendon-drive candidate, but it should be modeled first as a compact source of tendon displacement and tension. Variable stiffness should be claimed only at a stated level: actuator, tendon/transmission, joint, or fingertip/end-effector. A single flexion input that splits into left/right branches is still one independent input unless the branches have separately controlled tensions.

## Field Map

The current concept space separates three questions that are easy to accidentally merge:

- What creates finger motion?
- What creates variable stiffness or compliance?
- What interface transfers motion or force to the finger without invalidating tapping or pinch-like contact?
- What transmission tradeoff is actually needed after routing geometry has been quantified?

Current source anchors:

- Gunawardane et al. 2026: modular strain-limiting layers in zig-zag soft pneumatic actuators can alter actuator trajectory and effective stiffness.
- Mattelaer 2025: variable stiffness can be treated pragmatically as an experimentally calibrated mapping from actuator/tendon input to effective joint or end-effector stiffness, but this is effective stiffness modulation rather than proof of independent equilibrium-plus-stiffness control.
- Shi et al. 2020: soft actuator-finger interaction can be framed around MCP pressure-angle or torque-angle behavior.
- Bagneschi et al. 2023: lateral tendon routing from a dorsal/hand-mounted structure can improve stable wearing and is relevant to the tendon moment-arm problem.

## Candidate Design Branches

| Concept branch | Basic architecture | How it could create flexion | How it could create extension | How stiffness varies | What it can honestly claim now | Main risk |
|---|---|---|---|---|---|---|
| A. Dorsal zig-zag soft actuator + thimble | Soft zig-zag pneumatic actuator mounted on dorsal side, coupled proximally near MCP/hand and distally to thimble | If pressurization makes the dorsal zig-zag expand or unfold, the dorsal side becomes the outside of the bend and can bias the finger toward palmar flexion | If the dorsal structure shortens, stiffens, or elastically returns toward straight, it may assist extension or resist flexion | Modular strain-limiting layers, material stiffness, pressure-dependent stiffness | Dorsal soft variable-stiffness actuator concept that may support flexion if characterized as an expanding or flexion-biased actuator | Direction of assistance is not guaranteed; free deformation and coupled finger motion must be measured |
| B. Dorsal variable-stiffness splint or support | Dorsal zig-zag or segmented support along finger, attached to thimble or nail cap | Not active flexion unless it expands or imposes a flexed preferred shape | More naturally supports extension, return-to-straight, or resistance to flexion | Jamming, strain-limiting layers, adjustable stiffness layers, material choice | Tunable support or constraint for studying how stiffness affects motion amplitude and interaction force | Could become a brace rather than an actuator |
| C. Side-routed flexion input + thimble | Actuator/stiffness module on dorsum or wrist, one flexion input possibly split into left/right side branches to a distal thimble | Side branches pass with palmar/lateral flexion moment arms around MCP/PIP/DIP, so shared tension closes the finger | Passive return through tissue, spring, or elastic dorsal element | Adjustable series spring, interchangeable elastic insert, co-tension later if extension is added | Single-direction flexion-assist module with variable compliance | Routing and branch balance must be physically proven; palmar contact must stay clear |
| D. Dorsal extension tendon + thimble | Dorsal actuator module with tendon routed along dorsal side to nail/thimble attachment | Not primary function | Tension creates dorsal extension moment and opens finger | Adjustable series stiffness or tendon tension | Extension-assist or return-support module | Does not solve flexion unless paired with passive or active flexion |
| E. Antagonistic two-tendon module | Two tendons: one flexion path, one extension path, both connected to thimble or phalanges | Flexion tendon routed through flexion-side moment arm closes finger | Extension tendon routed through dorsal moment arm opens finger | Separate series stiffness for each tendon, or co-contraction/tension sum | True bidirectional variable-stiffness architecture | Mechanically and experimentally more complex; likely Stage 2 |
| F. Zig-zag actuator as remote tendon driver | Zig-zag/SLL actuator mounted on hand/wrist, pulling a tendon to the finger | Tendon routing creates flexion moment; zig-zag supplies displacement/force | Could drive extension tendon if routed dorsally | Zig-zag SLL configuration changes actuator output stiffness/trajectory | Hybrid soft variable-stiffness actuator plus tendon transmission | More complex than simple motor/spring tendon; needs actuator characterization |
| G. SECA-inspired MCP actuator | Soft actuator centered around MCP, coupled to finger/joint support | If actuator bends or expands in flexion-biased direction | Depressurization/passive return, or opposite actuator configuration | Composite layer stiffness, SLLs, pressure-dependent stiffness | MCP-focused soft actuator-finger interaction model | More MCP-specific; may not handle whole tapping path without extra joints |
| H. Pure simulation comparison model | No fixed hardware yet; model compares actuator abstractions | Defined by positive preferred angle or flexion torque | Defined by negative preferred angle or extension torque | Parameter sweep over actuator stiffness, series stiffness, or stiffness maps | Design-screening sandbox for choosing prototype path | Could become abstract unless tied to buildable prototype |

## Current Ranking

| Rank | Design idea | Why |
|---|---|---|
| 1 | Dorsal zig-zag soft actuator + thimble | Closest to the soft variable-stiffness identity and may support flexion through dorsal expansion. Needs characterization. |
| 2 | Side-routed flexion tendon + variable series stiffness | Cleanest mechanics and easiest to simulate/validate. Less clearly a soft actuator unless paired with elastic or soft module. |
| 3 | Zig-zag actuator as remote tendon driver | Strong hybrid: soft variable-stiffness actuator plus clean tendon moment arms. More complex but promising. |
| 4 | Antagonistic two-tendon module | Best for true bidirectional control, but likely too much for the first prototype. Good Stage 2 simulation branch. |
| 5 | SECA-inspired MCP actuator | Strong modeling and validation precedent, but less obviously connected to variable-stiffness tapping unless adapted. |

## Key Comparison: Dorsal Zig-Zag vs Side-Routed Tendon

| Question | Dorsal zig-zag actuator | Side-routed tendon actuator |
|---|---|---|
| What creates motion? | Expansion/bending of soft actuator | Tendon tension through moment arm |
| What creates stiffness change? | SLL configuration, material, pressure | Series spring, tensioning, stiffness module |
| How does it help flexion? | Dorsal expansion makes the outside of flexion bend longer | Tendon routed with flexion moment arm pulls finger closed |
| Is direction obvious from image? | No, must characterize actuator free shape | Yes, if moment arms are drawn |
| Easy to simulate first? | Medium | High |
| Easy to prototype first? | Medium to low | High |
| Strong soft-robotics novelty? | High | Medium |
| Strong mechanical defensibility? | Medium until measured | High if routed correctly |

## Common Approaches

### Actuator Screening Sequence

The current staged logic is:

1. Compare routing geometry with a reduced-order tendon path model.
2. Estimate excursion and `dL/dq` over a tapping-like or flexion sweep.
3. Convert target assistive joint torques into rough tendon tension using `tau_tendon = -T * dL/dq`.
4. Use stroke, tension, and compactness requirements to decide whether a simple tendon drive, TSA, CVT/CTA-style transmission, soft pneumatic actuator, or adjustable series stiffness is justified.

This keeps the hardware discussion from treating TSA or variable transmission as an assumption before the model has shown the actual speed, stroke, and torque demands.

### Reduced-Order Actuator Representation

For a dorsal zig-zag or SECA-style actuator:

```text
tau_act = K_act(c, u) * (theta_free(c, u) - theta)
```

where `u` is actuator input, `c` is the stiffness or SLL configuration, `theta_free` is the actuator's preferred angle, and `K_act` is the effective actuator-finger stiffness.

For a tendon or remote actuator:

```text
F_tendon = K_series(c) * (x_actuator(u) - x_finger(q))
tau_joint = r_joint(q) * F_tendon
```

where `K_series` is the adjustable transmission stiffness and `r_joint` is the tendon moment arm around MCP, PIP, or DIP.

In the current multi-joint routing model, the posture-dependent moment-arm equivalent should be computed from path length:

```text
tau_tendon = -T * partial L(q) / partial q
```

This is preferable to assigning constant moment arms before the routing geometry is known.

For a branched single input, use:

```text
tau_tendon = T * sum_j R_j(q)
R_j(q) = -partial L_j(q) / partial q
```

where `j` indexes physical branches, not independent actuators.

### TSA, CVT  Caution

For the current thesis stage:

- TSA may be useful as a compact tendon driver, but TSA alone is not the same thing as variable stiffness.
- If TSA is selected for v0, first size it from required tendon stroke and tension. Add stiffness only through a declared series/compliance element, antagonistic co-tension, or measured effective interaction stiffness.
- CVT-style ideas are mainly relevant if the required assistance has posture-dependent tradeoffs between speed, stroke, and torque.
- The first prototype should not lock into a variable-transmission architecture until the routing model has produced rough stroke and tension requirements.
- If TSA is pursued, the model should first answer whether the required cord stroke and tendon load are plausible for a bench-top device.

### Bidirectional Extension

A bidirectional architecture should not be described as one cable doing both unless a switching mechanism exists. The clean form is antagonistic:

```text
flexion tendon   -> flexion-side moment arm
extension tendon -> dorsal extension-side moment arm
```

Then:

```text
F_flex - F_ext -> motion direction
F_flex + F_ext -> apparent stiffness or co-contraction
```

## Tradeoffs

- The dorsal zig-zag branch is closer to the soft variable-stiffness identity, but its assistance direction depends on measured deformation mode.
- The tendon branch is mechanically clearer, but it may look less like a soft actuator unless the stiffness or actuation module is explicitly soft/compliant.
- The antagonistic branch is the most complete bidirectional solution, but it adds routing, sensing, and control complexity.
- A dorsal-only splint/support branch may preserve palmar contact well, but risks becoming a tunable brace rather than an actuator.
- The SECA branch is strong for MCP-centered modeling and validation, but may need adaptation to address multi-joint tapping-like motion.

## What Seems Realistic For This Thesis

The safest near-term modeling path is:

1. Keep the current 1-DOF MCP model as the baseline.
2. Use the current 3-link tendon-routing model to compare candidate routing paths by excursion and `dL/dq`.
3. Add passive MCP/PIP/DIP stiffness and quasi-static equilibrium only after the routing geometry behaves coherently.
4. Add a generic actuator interface that can represent both a dorsal zig-zag actuator and a tendon-series-stiffness actuator.
5. Compare soft/medium/stiff configurations using fingertip travel, tapping-like amplitude, joint angle range, interaction torque, and tendon tension.

The safest near-term prototype path is either:

- a dorsal zig-zag soft actuator plus thimble, if free-deformation tests confirm flexion-biased behavior; or
- a side-routed flexion tendon plus adjustable series stiffness, if the priority is clean force/moment-arm validation.

## Open Gaps

- Does a dorsal zig-zag actuator actually expand into a flexion-biased shape when coupled to a finger or thimble?
- How much palmar clearance is required for the intended tapping or thumb-index contact task?
- Which joint should be the first validation target: MCP only, MCP/PIP coupled, or all three joints?
- Can the stiffness setting be varied independently enough from motion input to support a clean variable-stiffness thesis claim?
- If stiffness is calibrated empirically, which level should be reported as the thesis definition: actuator stiffness, series/transmission stiffness, joint stiffness, or fingertip/end-effector stiffness?
- Which first prototype is more realistic by the D3 target: dorsal zig-zag/thimble or side-routed tendon/thimble?

## Design Implications

1. Do not rely on photorealistic renders to validate mechanism logic. The next drawings must show joint axes, tendon or actuator lines of action, moment arms, and torque direction.
2. Treat the dorsal zig-zag concept and side-routed tendon concept as separate branches until each can be reduced to a clear equation and a clear benchtop test.
3. For the first simulation, build a design-sandbox interface rather than a single locked actuator model.

## Meeting-Safe Framing

I currently see two leading concept branches. The first is a dorsal zig-zag soft actuator coupled to a thimble, where dorsal expansion could support palmar flexion while strain-limiting layers tune stiffness and trajectory. The second is a side-routed tendon-thimble module, where flexion is created more explicitly by tendon moment arms and variable stiffness is introduced through series compliance. The zig-zag branch is more aligned with soft variable-stiffness actuation, while the tendon branch is mechanically cleaner and easier to simulate. I want to use the reduced-order model to compare these branches before freezing the prototype concept.

## Candidate Next Decision

Which mechanism family should be used for the first prototype architecture: dorsal zig-zag soft actuator with thimble, side-routed tendon with adjustable series stiffness, or a staged path where both are simulated but only one is built?
