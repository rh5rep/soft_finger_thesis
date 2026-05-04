# Onshape FeatureScript CAD Baseline For Single-Tendon Ring-Thimble Hardware

## Purpose

Capture the first scriptable CAD baseline for the bench-top hardware side of the thesis without turning it into a premature mechanism decision.

## Context

The repo already argues for an index-finger design sandbox built around:

- one distal thimble
- a small number of intermediate tendon guides or rings
- a single flexion tendon as the first hardware baseline

That matches the current simulation-first thesis scope better than a full glove or antagonistic multi-tendon design.

## Working Decision For This Baseline

Use Onshape `FeatureScript` as the first scriptable CAD route for the hardware concept, with the Onshape REST API reserved for later export, batch-variation, or workflow automation.

## Why This Is Reasonable

- it keeps the geometry parametric inside the CAD system rather than relying on manual redraws
- it is close to the thesis need, which is fast iteration on routing geometry and interface placement
- it supports the current simplified hardware decomposition: ring guides plus distal thimble
- it avoids committing yet to a full wearable architecture

## Current Geometry Assumptions

- finger axis is modeled as a straight local `X` axis
- guide rings and thimble are cylindrical first-pass parts
- the tendon path is approximated as a straight longitudinal channel offset laterally and slightly dorsally
- the distal thimble uses a closed tip cap and a transverse anchor hole
- ring and thimble openings are represented with simple split cuts rather than realistic compliant closures

## Deliverable In Repo

- [single_tendon_ring_thimble.fs](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/cad/onshape/single_tendon_ring_thimble.fs)
- [README.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/cad/onshape/README.md)

## Limitations

- the feature has not yet been executed inside a live Onshape document from this repo workflow
- parameter defaults are documented in the README rather than encoded as polished feature-dialog presets
- the parts are geometric placeholders for routing iteration, not comfort-validated wearable interfaces
- the script does not yet emit dimensions back into Python for route-length or moment-arm comparison

## Open Questions

- whether two guides are enough before curvature control becomes poor
- whether the tendon channel should remain lateral or move to a palmar-lateral track
- whether the distal anchor should be a direct hole, a molded post, or a separate hard insert
- whether the first physical build should stay index-only or include a passive thumb contact block

## Next Useful Step

Open the feature in Onshape, confirm it regenerates cleanly, and then tie one or two CAD parameter sweeps back to the reduced routing comparisons already outlined in the tendon-routing memo.
