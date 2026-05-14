from __future__ import annotations

from simulation_modeling import candidate_sweep_utils as joint_space_sweep
from simulation_modeling import straight_finger_model
from simulation_modeling import straight_finger_sweep
from simulation_modeling import v01_model

import numpy as np


IDX_L_PROX = 41.0
IDX_L_MIDDLE = 26.0
IDX_L_DIST = 20.0

IDX_D_PROX = 0.33 * IDX_L_PROX
IDX_D_MIDDLE = 0.78 * IDX_L_MIDDLE
IDX_D_DIST = 0.68 * IDX_L_DIST


def scale_joint_geometry(
    geom: v01_model.FingerGeometry,
    scale: float,
) -> v01_model.FingerGeometry:
    return v01_model.FingerGeometry(
        geom.l1 * scale,
        geom.l2 * scale,
        geom.l3 * scale,
        geom.d1 * scale,
        geom.d2 * scale,
        geom.d3 * scale,
    )


def scale_straight_geometry(
    geom: straight_finger_model.StraightFingerGeometry,
    scale: float,
) -> straight_finger_model.StraightFingerGeometry:
    return straight_finger_model.StraightFingerGeometry(
        l1=geom.l1 * scale,
        l2=geom.l2 * scale,
        l3=geom.l3 * scale,
    )


BASE_JOINT_FINGER_GEOM = v01_model.FingerGeometry(
    IDX_L_PROX,
    IDX_L_MIDDLE,
    IDX_L_DIST,
    IDX_D_PROX,
    IDX_D_MIDDLE,
    IDX_D_DIST,
)


BASE_STRAIGHT_FINGER_GEOM = straight_finger_model.StraightFingerGeometry(
    l1=IDX_L_PROX,
    l2=IDX_L_MIDDLE,
    l3=IDX_L_DIST,
)


JOINT_FINGER_GEOMS = {
    "small": scale_joint_geometry(BASE_JOINT_FINGER_GEOM, 0.9),
    "nominal": BASE_JOINT_FINGER_GEOM,
    "large": scale_joint_geometry(BASE_JOINT_FINGER_GEOM, 1.1),
}


STRAIGHT_FINGER_GEOMS = {
    "small": scale_straight_geometry(BASE_STRAIGHT_FINGER_GEOM, 0.9),
    "nominal": BASE_STRAIGHT_FINGER_GEOM,
    "large": scale_straight_geometry(BASE_STRAIGHT_FINGER_GEOM, 1.1),
}


JOINT_REST = (0.0, 0.0, 0.0)
STRAIGHT_REST = 0.0


NOMINAL_K_PASSIVE = np.array([0.02, 0.0286, 0.015], dtype=float)
MID_K_PASSIVE = 1.15 * NOMINAL_K_PASSIVE
HIGH_K_PASSIVE = 1.3 * NOMINAL_K_PASSIVE


JOINT_STIFFNESSES = {
    "nominal": tuple(NOMINAL_K_PASSIVE),
    "mid": tuple(MID_K_PASSIVE),
    "high": tuple(HIGH_K_PASSIVE),
}


# Reduced-order straight-finger defaults kept separate from the joint-space
# tuples so they can be tuned independently later without changing notebook
# control flow. These use the MCP passive stiffness directly.
STRAIGHT_STIFFNESSES = {
    "nominal": float(NOMINAL_K_PASSIVE[0]),
    "mid": float(MID_K_PASSIVE[0]),
    "high": float(HIGH_K_PASSIVE[0]),
}


def build_joint_space_model_cases() -> list[joint_space_sweep.ModelParams]:
    cases = []
    for size_name, geom in JOINT_FINGER_GEOMS.items():
        for stiff_name, stiffness in JOINT_STIFFNESSES.items():
            cases.append(
                joint_space_sweep.ModelParams(
                    abstraction_name="joint_space",
                    name=f"{size_name}_{stiff_name}_joint_space",
                    size_name=size_name,
                    stiffness_name=stiff_name,
                    geom=geom,
                    joint_rest=JOINT_REST,
                    stiffness=stiffness,
                )
            )
    return cases


def build_straight_finger_model_cases() -> list[straight_finger_sweep.ModelParams]:
    cases = []
    for size_name, geom in STRAIGHT_FINGER_GEOMS.items():
        for stiff_name, stiffness in STRAIGHT_STIFFNESSES.items():
            cases.append(
                straight_finger_sweep.ModelParams(
                    abstraction_name="straight_finger",
                    name=f"{size_name}_{stiff_name}_straight_finger",
                    size_name=size_name,
                    stiffness_name=stiff_name,
                    geom=geom,
                    joint_rest=STRAIGHT_REST,
                    stiffness=stiffness,
                )
            )
    return cases


def build_all_model_cases() -> list[object]:
    return build_joint_space_model_cases() + build_straight_finger_model_cases()
