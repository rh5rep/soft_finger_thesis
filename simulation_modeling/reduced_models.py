from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np
from scipy.optimize import root_scalar

PassiveLawName = Literal["linear", "cubic"]
ActuatorMode = Literal["joint_torque", "tendon"]
IndexCouplingMode = Literal["none", "dip_pip_hard"]

INDEX_JOINT_LABELS = ("MCP", "PIP", "DIP")


@dataclass(frozen=True)
class DigitTemplate:
    key: str
    label: str
    link_length_m: float
    theta_0_deg: float
    angle_min_deg: float
    angle_max_deg: float
    interpretation_window_deg: tuple[float, float]
    k1_default: float
    k3_default: float
    joint_torque_default: float
    tendon_force_default: float
    anchor_x_m_default: float
    anchor_y_m_default: float
    attachment_fraction_default: float


@dataclass
class ModelParameters:
    digit_key: str
    passive_law: PassiveLawName
    actuator_mode: ActuatorMode
    link_length_m: float
    theta_0_deg: float
    angle_min_deg: float
    angle_max_deg: float
    k1: float
    k3: float
    joint_torque_nm: float
    tendon_force_n: float
    anchor_x_m: float
    anchor_y_m: float
    attachment_fraction: float


@dataclass(frozen=True)
class EquilibriumPoint:
    theta_rad: float
    net_torque_nm: float


@dataclass
class IndexFingerParameters:
    passive_law: PassiveLawName
    coupling_mode: IndexCouplingMode
    link_lengths_m: tuple[float, float, float]
    joint_angles_deg: tuple[float, float, float]
    neutral_angles_deg: tuple[float, float, float]
    k1: tuple[float, float, float]
    k3: tuple[float, float, float]
    dip_pip_ratio: float
    applied_mcp_torque_nm: float


TEMPLATES: dict[str, DigitTemplate] = {
    "index_mcp": DigitTemplate(
        key="index_mcp",
        label="Index MCP proxy",
        link_length_m=0.055,
        theta_0_deg=0.0,
        angle_min_deg=0.0,
        angle_max_deg=110.0,
        interpretation_window_deg=(0.0, 80.0),
        k1_default=0.08,
        k3_default=0.01,
        joint_torque_default=0.04,
        tendon_force_default=5.0,
        anchor_x_m_default=-0.020,
        anchor_y_m_default=0.020,
        attachment_fraction_default=0.70,
    ),
    "thumb_proxy": DigitTemplate(
        key="thumb_proxy",
        label="Thumb flexion proxy",
        link_length_m=0.040,
        theta_0_deg=5.0,
        angle_min_deg=-10.0,
        angle_max_deg=90.0,
        interpretation_window_deg=(0.0, 60.0),
        k1_default=0.06,
        k3_default=0.008,
        joint_torque_default=0.03,
        tendon_force_default=4.0,
        anchor_x_m_default=-0.015,
        anchor_y_m_default=0.018,
        attachment_fraction_default=0.65,
    ),
}


def default_index_finger_parameters() -> IndexFingerParameters:
    return IndexFingerParameters(
        passive_law="linear",
        coupling_mode="none",
        link_lengths_m=(0.045, 0.025, 0.018),
        joint_angles_deg=(25.0, 35.0, 20.0),
        neutral_angles_deg=(0.0, 0.0, 0.0),
        k1=(0.08, 0.045, 0.025),
        k3=(0.01, 0.006, 0.003),
        dip_pip_ratio=0.67,
        applied_mcp_torque_nm=0.04,
    )


def default_parameters(digit_key: str = "index_mcp") -> ModelParameters:
    template = TEMPLATES[digit_key]
    return ModelParameters(
        digit_key=template.key,
        passive_law="linear",
        actuator_mode="joint_torque",
        link_length_m=template.link_length_m,
        theta_0_deg=template.theta_0_deg,
        angle_min_deg=template.angle_min_deg,
        angle_max_deg=template.angle_max_deg,
        k1=template.k1_default,
        k3=template.k3_default,
        joint_torque_nm=template.joint_torque_default,
        tendon_force_n=template.tendon_force_default,
        anchor_x_m=template.anchor_x_m_default,
        anchor_y_m=template.anchor_y_m_default,
        attachment_fraction=template.attachment_fraction_default,
    )


def resolved_index_joint_angles_rad(params: IndexFingerParameters) -> np.ndarray:
    angles_deg = np.asarray(params.joint_angles_deg, dtype=float)
    if params.coupling_mode == "dip_pip_hard":
        angles_deg = angles_deg.copy()
        angles_deg[2] = params.dip_pip_ratio * angles_deg[1]
    return np.deg2rad(angles_deg)


def index_finger_joint_points(
    params: IndexFingerParameters,
    joint_angles_rad: np.ndarray | None = None,
) -> np.ndarray:
    angles = resolved_index_joint_angles_rad(params) if joint_angles_rad is None else np.asarray(joint_angles_rad, dtype=float)
    cumulative_angles = np.cumsum(angles)
    points = [np.array([0.0, 0.0], dtype=float)]
    current = points[0].copy()

    for length, angle in zip(params.link_lengths_m, cumulative_angles, strict=True):
        current = current + np.array([length * np.cos(angle), length * np.sin(angle)])
        points.append(current.copy())

    return np.vstack(points)


def index_finger_tip_point(params: IndexFingerParameters) -> np.ndarray:
    return index_finger_joint_points(params)[-1]


def index_finger_passive_required_torques(params: IndexFingerParameters) -> np.ndarray:
    angles = resolved_index_joint_angles_rad(params)
    neutral = np.deg2rad(np.asarray(params.neutral_angles_deg, dtype=float))
    delta = angles - neutral
    k1 = np.asarray(params.k1, dtype=float)

    if params.passive_law == "linear":
        return k1 * delta

    k3 = np.asarray(params.k3, dtype=float)
    return k1 * delta + k3 * delta**3


def index_finger_applied_torques(params: IndexFingerParameters) -> np.ndarray:
    return np.array([params.applied_mcp_torque_nm, 0.0, 0.0], dtype=float)


def index_finger_net_torques(params: IndexFingerParameters) -> np.ndarray:
    return index_finger_applied_torques(params) - index_finger_passive_required_torques(params)


def index_finger_local_passive_stiffness(params: IndexFingerParameters) -> np.ndarray:
    angles = resolved_index_joint_angles_rad(params)
    neutral = np.deg2rad(np.asarray(params.neutral_angles_deg, dtype=float))
    delta = angles - neutral
    k1 = np.asarray(params.k1, dtype=float)

    if params.passive_law == "linear":
        return k1

    k3 = np.asarray(params.k3, dtype=float)
    return k1 + 3.0 * k3 * delta**2


def passive_required_torque(theta_rad: np.ndarray | float, params: ModelParameters) -> np.ndarray | float:
    delta = np.asarray(theta_rad) - np.deg2rad(params.theta_0_deg)
    if params.passive_law == "linear":
        required = params.k1 * delta
    else:
        required = params.k1 * delta + params.k3 * delta**3
    if np.isscalar(theta_rad):
        return float(required)
    return required


def passive_torque(theta_rad: np.ndarray | float, params: ModelParameters) -> np.ndarray | float:
    return -passive_required_torque(theta_rad, params)


def actuator_torque(theta_rad: np.ndarray | float, params: ModelParameters) -> np.ndarray | float:
    theta_array = np.atleast_1d(np.asarray(theta_rad, dtype=float))

    if params.actuator_mode == "joint_torque":
        torque = np.full_like(theta_array, fill_value=params.joint_torque_nm, dtype=float)
    else:
        attachment = attachment_point(theta_array, params)
        anchor = np.array([params.anchor_x_m, params.anchor_y_m], dtype=float)
        direction = anchor[None, :] - attachment
        distance = np.linalg.norm(direction, axis=1)
        safe_distance = np.where(distance > 1e-12, distance, 1e-12)
        unit = direction / safe_distance[:, None]
        force_vec = params.tendon_force_n * unit
        torque = attachment[:, 0] * force_vec[:, 1] - attachment[:, 1] * force_vec[:, 0]

    if np.isscalar(theta_rad):
        return float(torque[0])
    return torque


def net_torque(theta_rad: np.ndarray | float, params: ModelParameters) -> np.ndarray | float:
    return actuator_torque(theta_rad, params) + passive_torque(theta_rad, params)


def attachment_point(theta_rad: np.ndarray | float, params: ModelParameters) -> np.ndarray:
    theta_array = np.atleast_1d(np.asarray(theta_rad, dtype=float))
    radius = params.attachment_fraction * params.link_length_m
    x = radius * np.cos(theta_array)
    y = radius * np.sin(theta_array)
    return np.column_stack((x, y))


def tip_point(theta_rad: float, params: ModelParameters) -> np.ndarray:
    return np.array(
        [
            params.link_length_m * np.cos(theta_rad),
            params.link_length_m * np.sin(theta_rad),
        ]
    )


def angle_grid_rad(params: ModelParameters, count: int = 361) -> np.ndarray:
    return np.deg2rad(np.linspace(params.angle_min_deg, params.angle_max_deg, count))


def find_equilibria(params: ModelParameters, samples: int = 361) -> list[EquilibriumPoint]:
    grid = angle_grid_rad(params, count=samples)
    residual = net_torque(grid, params)
    roots: list[EquilibriumPoint] = []

    for index, value in enumerate(residual[:-1]):
        next_value = residual[index + 1]
        left = grid[index]
        right = grid[index + 1]

        if abs(value) < 1e-8:
            roots.append(EquilibriumPoint(theta_rad=float(left), net_torque_nm=float(value)))
            continue

        if value * next_value > 0.0:
            continue

        solution = root_scalar(lambda theta: net_torque(theta, params), bracket=(left, right), method="brentq")
        roots.append(
            EquilibriumPoint(
                theta_rad=float(solution.root),
                net_torque_nm=float(net_torque(solution.root, params)),
            )
        )

    deduped: list[EquilibriumPoint] = []
    for root in roots:
        if deduped and abs(root.theta_rad - deduped[-1].theta_rad) < np.deg2rad(0.2):
            continue
        deduped.append(root)
    return deduped


def select_continuation_root(candidates: list[EquilibriumPoint], previous_theta_rad: float | None, theta_0_rad: float) -> float | None:
    if not candidates:
        return None

    if previous_theta_rad is None:
        return min(candidates, key=lambda point: abs(point.theta_rad - theta_0_rad)).theta_rad

    return min(candidates, key=lambda point: abs(point.theta_rad - previous_theta_rad)).theta_rad


def equilibrium_branch(
    params: ModelParameters,
    input_values: np.ndarray,
) -> np.ndarray:
    branch = np.full_like(input_values, np.nan, dtype=float)
    previous_theta: float | None = None
    theta_0_rad = np.deg2rad(params.theta_0_deg)

    for index, value in enumerate(input_values):
        trial = ModelParameters(**vars(params))
        if trial.actuator_mode == "joint_torque":
            trial.joint_torque_nm = float(value)
        else:
            trial.tendon_force_n = float(value)

        candidates = find_equilibria(trial)
        selected = select_continuation_root(candidates, previous_theta, theta_0_rad)
        if selected is None:
            previous_theta = None
            continue

        branch[index] = np.rad2deg(selected)
        previous_theta = selected

    return branch


def current_input_label(params: ModelParameters) -> str:
    if params.actuator_mode == "joint_torque":
        return "Applied joint torque [N·m]"
    return "Actuator force [N]"


def current_input_value(params: ModelParameters) -> float:
    if params.actuator_mode == "joint_torque":
        return params.joint_torque_nm
    return params.tendon_force_n


def sweep_input_values(params: ModelParameters, count: int = 80) -> np.ndarray:
    if params.actuator_mode == "joint_torque":
        upper = max(0.12, params.joint_torque_nm * 1.5, 1e-4)
    else:
        upper = max(12.0, params.tendon_force_n * 1.5, 1e-3)
    return np.linspace(0.0, upper, count)


def summary_text(params: ModelParameters, equilibrium_roots: list[EquilibriumPoint]) -> str:
    lines = [
        f"Digit: {TEMPLATES[params.digit_key].label}",
        f"Passive law: {params.passive_law}",
        f"Actuator mode: {params.actuator_mode}",
    ]
    if not equilibrium_roots:
        lines.append("Equilibrium: none in current angle window")
        return "\n".join(lines)

    for index, root in enumerate(equilibrium_roots, start=1):
        theta_deg = np.rad2deg(root.theta_rad)
        lines.append(f"Eq {index}: {theta_deg:.1f} deg")
    return "\n".join(lines)
