# Image Generation Prompts For Silvia Update

Use these prompts to generate clean slide visuals. Recommended style for all: white background, technical editorial look, restrained DTU-like red accent plus charcoal/blue-gray, no decorative gradients, no cartoon hand, no clinical patient imagery, no fake logos, no dense text.

## Master Style Prompt

Create a professional technical slide illustration for an MSc robotics thesis supervisor update. Use a clean white background, thin charcoal linework, restrained red accents, subtle blue-gray secondary lines, flat vector-like engineering style, high readability, no decorative gradients, no shadows except very subtle depth, no people, no fake logos, no medical claims. The image should look suitable for a university robotics lab PowerPoint. Leave generous negative space for a title and captions.

## Prompt 1 - V0.1 Thesis Workflow

Create a clean left-to-right workflow diagram for a robotics thesis model: "Literature + thesis objective" flows into "Reduced-order finger model", then "Tendon/ring routing parameterization", then "Simulation sweeps", then "Mechanical feasibility metrics", then "3-5 prototype sleeve/routing candidates". Use compact icons: papers, simple finger model, routing guides, parameter grid, metric gauges, prototype sketches. Keep text minimal and legible. White background, thin charcoal lines, red accent arrows, technical editorial style.

## Prompt 2 - Physical Sleeve Concept

Create an engineering concept illustration of an index finger wearing a minimal experimental sleeve: distal fingertip thimble/cap, two removable soft ring guides on the proximal and middle phalanges, a side/palmar-lateral tendon path, and an upstream tendon entry toward the hand/wrist. Keep the palm contact area mostly unobstructed. Show the tendon as a red line, rings as soft translucent gray bands, and guide points as small red dots. Use a simplified anatomically neutral finger, not a photorealistic hand. White background, clean technical line art.

## Prompt 3 - 2D Effective Model Abstraction

Create a 2D planar index-finger mechanics diagram. Show three rigid links labeled proximal, middle, distal; revolute joints labeled MCP, PIP, DIP; joint angles q_MCP, q_PIP, q_DIP; effective routing elements labeled entry, guide, guide, anchor; and a piecewise-linear tendon path through those points. Show the fingertip trajectory as a faint arc. Use no more than five labels, with mathematical notation kept crisp. White background, thin black link lines, red tendon, blue-gray joint axes.

## Prompt 4 - Geometry-To-Torque Equation Chain

Create a visual equation pipeline for a reduced-order tendon-routing model. Use six connected blocks: q -> FK(q) -> L(q) -> dL/dq -> R(q) = -dL/dq -> tau_tendon = T R(q). Add a second lower branch: tau_req = K(q - q0) -> least-squares T_req -> residual tau_error. Use clean math typesetting, boxes, and arrows. This should look like a polished methods slide, not a handwritten note. White background, charcoal text, red highlights on R(q), T_req, and tau_error.

## Prompt 5 - What V0.1 Does And Does Not Claim

Create a two-column technical boundary graphic. Left column title: "V0.1 supports". Right column title: "V0.1 does not yet prove". Left column icons: routing geometry, tendon stroke, moment arm, tension estimate, prototype candidate. Right column icons: tapping frequency, sequence effect, patient adaptation, clinical improvement, final actuator choice. Use minimal text, checkmarks on the left, caution markers on the right. Professional supervisor-update style, white background, restrained red and gray.

## Prompt 6 - Candidate Sweep Scorecard

Create a clean scorecard-style slide visual for comparing routing candidates. Show three small schematic routing thumbnails in a row, each with metric chips below: peak tension, pull excursion, torque mismatch, branch imbalance, feasibility. Highlight the middle candidate as "refined candidate" with a subtle red outline, but do not imply it is final. Use placeholder values based on: 1.82 N, 19.8 mm, 0.34 RMS relative mismatch. White background, crisp tables, thin lines, no 3D render.

## Prompt 7 - Passive Stiffness Caveat

Create an uncertainty-chain diagram showing why passive stiffness matters. Use a central chain: K_passive -> tau_req -> T_req -> torque mismatch -> candidate ranking. Add three small scenarios labeled low, nominal, high stiffness as stacked bands feeding into the chain. Make the takeaway visually clear: routing rankings depend on stiffness assumptions. Use a serious engineering style, white background, red accent on "candidate ranking", blue-gray uncertainty bands.

## Prompt 8 - Underactuated Single Input

Create a clean mechanics diagram explaining underactuation. Show one actuator/tendon input splitting to influence three joints MCP/PIP/DIP, with one scalar tension T and a three-component torque vector. Include a subtle visual mismatch between desired torque vector and fitted torque vector, labeled "residual mismatch". Keep it conceptual and mathematical, not hardware-heavy. White background, red tendon line, gray finger links, blue desired vector, red fitted vector.

## Prompt 9 - One Input, Two Physical Branches

Create an engineering diagram of one upstream actuator input splitting into two left/right physical tendon branches around an index finger, both sharing the same tension input. Show both branches contributing moment arms around MCP/PIP/DIP, then summing into R_total(q). Include a clear note visually: "branches do not equal independent control". Use minimal words, clean schematic linework, white background, red branches, gray finger.

## Prompt 10 - V0.1 Result Figure Redesign

Create a polished four-panel scientific figure layout inspired by a Plotly analysis output. Panels: required tension over sweep, relative torque mismatch over sweep, moment-arm components over sweep, fingertip trajectory. Use clean axes, sparse ticks, consistent typography, and a small callout: "Refined candidate: 1.82 N peak tension, 19.8 mm pull, 0.34 RMS relative mismatch". Do not show noisy legends; use direct labels. White background, publication-style.

## Prompt 11 - Prototype Resource Path With Skylab

Create a concise resource-path diagram for moving from model to prototype with Skylab support. Steps: V0.1 candidate screening -> 2D candidate sketches -> design review -> fabrication route -> bench-top validation. Add a side rail labeled Skylab support: fabrication advice, expert design review, innovation coaching, grant navigation. Keep startup/company path as a small optional note, not the main story. White background, professional operations diagram.

## Prompt 12 - Minimal BOM Visual

Create a clean bill-of-materials visual for a benchtop index-finger tendon-routing prototype. Show grouped components as simple technical icons: distal thimble, removable soft rings/guides, tendon cord or Bowden line, spool/pulley or TSA placeholder, motor/driver, load cell/tension sensor, markers/camera, microcontroller, springs/elastic inserts, straps/fasteners. Use compact labels and a neat grid. White background, thin line icons, red accent on actuation/sensing items.

## Prompt 13 - Six-Slide Appendix Cover Graphic

Create a title slide background for a supervisor appendix called "V0.1 routing-screening update". Show a simplified index finger line drawing, a red tendon path, and faint overlay of a parameter grid and trajectory curve. Leave the left third empty for title text. Technical, restrained, white background, no decorative gradients, no photorealistic hand.

## Prompt 14 - Decision Matrix Visual

Create a compact decision matrix comparing next actions: "expand routing families", "add two-branch routing", "calibrate passive stiffness", "choose actuator", "fabricate prototype". Columns: evidence needed, thesis value, risk reduced, timing. Use a clean table with subtle icons and a red highlight around the recommended next two actions: expand routing families and clarify passive stiffness. White background, professional slide design.

## Prompt 15 - Actuation Kept Separate From Routing

Create a technical concept graphic showing routing requirements feeding into actuator selection. Left side: routing model outputs stroke, tension, speed/bandwidth, stiffness range. Right side: candidate actuator options labeled motor-spool, TSA, variable transmission, adjustable series stiffness. Use arrows from outputs to options, with a caption-like visual idea: "route first, actuator second". White background, clean engineering diagram, red accents.

## Prompt 16 - Bench Validation Loop

Create a closed-loop validation workflow diagram: simulate candidate -> fabricate adjustable mock-up -> measure tendon tension and marker-tracked joint motion -> compare model vs measurement -> update assumptions. Use technical icons for simulation plot, prototype, load cell, camera markers, residual plot, and iteration arrow. Keep it concise and professional for a thesis methods slide.
