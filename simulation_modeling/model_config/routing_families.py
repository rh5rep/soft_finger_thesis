from simulation_modeling.candidate_sweep_utils import (
    SharedRoutingGeometry,
    generate_two_guide_family,
)


# Shared upstream routing preset for first-pass palmar flexion screening.
PALMAR_ENTRY_SHARED = SharedRoutingGeometry(
    entry_body="world",
    entry_local=(-8.0, -4.0),
    splitter_body=None,
    splitter_local=None,
)


# Same shared entry but with an explicit splitter placeholder for later
# branch-balance experiments.
PALMAR_ENTRY_WITH_SPLITTER = SharedRoutingGeometry(
    entry_body="world",
    entry_local=(-8.0, -4.0),
    splitter_body="proximal",
    splitter_local=(8.0, -4.0),
)


# Baseline single-branch proximal-to-middle two-guide family.
TWO_GUIDE_PROX_MID_BASELINE = generate_two_guide_family(
    family="two_guide_prox_mid_baseline",
    shared=PALMAR_ENTRY_SHARED,
    guide_bodies=("proximal", "middle"),
    guide_long_sets=(
        (0.25, 0.25),
        (0.25, 0.45),
        (0.45, 0.45),
        (0.45, 0.65),
    ),
    guide_offset_sets=(
        (-3.0, -3.0),
        (-5.0, -5.0),
    ),
    distal_anchor_longs=(0.80, 0.90),
    distal_anchor_offsets=(-4.0,),
)


# Slightly more aggressive palmar offsets for larger routing leverage.
TWO_GUIDE_PROX_MID_HIGH_OFFSET = generate_two_guide_family(
    family="two_guide_prox_mid_high_offset",
    shared=PALMAR_ENTRY_SHARED,
    guide_bodies=("proximal", "middle"),
    guide_long_sets=(
        (0.25, 0.45),
        (0.45, 0.65),
    ),
    guide_offset_sets=(
        (-6.0, -6.0),
        (-8.0, -8.0),
    ),
    distal_anchor_longs=(0.80, 0.90),
    distal_anchor_offsets=(-4.0, -6.0),
)


# Downstream-shifted family to test whether a more distal routing emphasis
# changes excursion and moment-arm behavior enough to matter.
TWO_GUIDE_MID_DIST_BASELINE = generate_two_guide_family(
    family="two_guide_mid_dist_baseline",
    shared=PALMAR_ENTRY_SHARED,
    guide_bodies=("middle", "distal"),
    guide_long_sets=(
        (0.20, 0.20),
        (0.20, 0.40),
        (0.40, 0.40),
    ),
    guide_offset_sets=(
        (-3.0, -3.0),
        (-5.0, -5.0),
    ),
    distal_anchor_longs=(0.80, 0.95),
    distal_anchor_offsets=(-4.0,),
)


ALL_TWO_GUIDE_FAMILIES = (
    TWO_GUIDE_PROX_MID_BASELINE
    + TWO_GUIDE_PROX_MID_HIGH_OFFSET
    + TWO_GUIDE_MID_DIST_BASELINE
)
