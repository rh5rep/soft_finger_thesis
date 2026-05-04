"""
Version 0 reduced-order tendon-routing model for the thesis.

Current stage:
- 2D planar index-finger geometry with rigid proximal, middle, and distal phalanges
- MCP, PIP, and DIP forward kinematics
- tendon routing through fixed local element points and a distal thimble anchor
- tendon path length, tendon segment lengths, fingertip trajectory, and plotting helpers
- local numerical gradient dL/dq for posture-dependent routing sensitivity

What has been verified in this file:
- under the current sign convention, negative joint angles represent physiological flexion
- the chosen palmar routing shortens smoothly during coordinated flexion
- same-body tendon segments stay constant while cross-body segments vary with posture
- the tendon-length gradient is posture-dependent and can be used for generalized tendon
  torque through tau_tendon = -T * dL/dq

What is intentionally not implemented yet:
- explicit tendon-torque helper functions
- passive joint torque laws
- multi-joint static equilibrium solving
- antagonistic extensor routing or routing optimization
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Coordinate / sign convention:
# - MCP joint J1 is at (0, 0)
# - zero angles = finger straight along +x
# - positive rotation = counterclockwise
# - theta1, theta2, theta3 are relative joint angles
# - local u = along phalanx from proximal joint
# - local v = perpendicular offset from phalanx centerline
# - negative v values represent palmar-side routing in this setup
# In this coordinate setup:
# - negative joint angles correspond to physiological flexion
#   for the current palmar tendon routing choice

Vec2 = np.ndarray

ORIGIN = np.array([0.0, 0.0], dtype=float)


@dataclass
class FingerGeometry:
    """
    Reduced-order 2D finger model.

    Assumptions:
    - planar 2D
    - 3 rigid phalanges
    - 3 revolute joints (MCP, PIP, DIP)
    - tendon routed through fixed element points attached to phalanges
    - total tendon length = sum of straight-line distances between consecutive routing points
    """

    l1: float
    l2: float
    l3: float

@dataclass
class FingerKinematics:
    joint_angles: Tuple[float, float, float]
    J1: Vec2
    J2: Vec2
    J3: Vec2
    Fingertip: Vec2
    phi1: float
    phi2: float
    phi3: float


@dataclass
class RoutingElement:
    name: str
    body: str
    kind: str
    local: Vec2

@dataclass 
class RoutingPath:
    name: str
    elements: tuple[RoutingElement, ...]


def rot2d(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)


def dist(p1: Vec2, p2: Vec2) -> float:
    return float(np.linalg.norm(p2 - p1))


def transform_local_point(base_world: Vec2, phi: float, point_local: Vec2) -> Vec2:
    return base_world + rot2d(phi) @ point_local


def forward_kinematics(
    geom: FingerGeometry,
    joint_angles: Tuple[float, float, float]
) -> FingerKinematics:
    """
    joint_angles = (theta1, theta2, theta3)
    where:
        theta1 = MCP angle
        theta2 = PIP relative angle
        theta3 = DIP relative angle
    """
    theta1, theta2, theta3 = joint_angles

    phi1 = theta1
    phi2 = theta1 + theta2
    phi3 = theta1 + theta2 + theta3

    # MCP joint at origin
    J1 = np.array(ORIGIN, dtype=float)

    J2 = J1 + np.array([geom.l1 * np.cos(phi1), geom.l1 * np.sin(phi1)], dtype=float)
    J3 = J2 + np.array([geom.l2 * np.cos(phi2), geom.l2 * np.sin(phi2)], dtype=float)
    Fingertip  = J3 + np.array([geom.l3 * np.cos(phi3), geom.l3 * np.sin(phi3)], dtype=float)

    return FingerKinematics(
        joint_angles=joint_angles,
        J1=J1, J2=J2, J3=J3, Fingertip=Fingertip,
        phi1=phi1, phi2=phi2, phi3=phi3
    )


def element_world_position(
    element: RoutingElement,
    fk: FingerKinematics | None = None
) -> Vec2:
    

    if element.body == 'world':
        return element.local
    
    if fk is None:
        raise ValueError(f"{element.body} requires finger kinematics on {element.name}.")
    
    frame_map = {
        "proximal": (fk.J1, fk.phi1),
        "middle": (fk.J2, fk.phi2),
        "distal": (fk.J3, fk.phi3),

    }

    if element.body not in frame_map:
        raise ValueError(f"Unsupported element body {element.body}")

    base_world, phi = frame_map[element.body]
    return transform_local_point(base_world, phi, element.local)
    

def tendon_path_points_world(fk: FingerKinematics,
                             path: RoutingPath) -> np.ndarray:
    
    points = []
    for element in path.elements:
        points.append(element_world_position(element, fk))

    return np.asarray(points)


def tendon_path_length(fk: FingerKinematics,
                       path: RoutingPath) -> tuple[float, list[float], np.ndarray]:

    points = tendon_path_points_world(fk, path)
    segment_lengths = [dist(points[i], points[i+1]) for i in range(len(points)-1)]

    total = float(sum(segment_lengths))

    return total, segment_lengths, points


def compute_tendon_lengths(joint_angles_list: np.ndarray, geom: FingerGeometry, path: RoutingPath) -> np.ndarray:
    lengths = []
    for joint_angles in joint_angles_list:
        fk = forward_kinematics(geom, joint_angles)
        total_len = tendon_path_length(fk, path)[0]
        lengths.append(total_len)

    return np.array(lengths)


def tendon_excursion(
    geom: FingerGeometry,
    path: RoutingPath,
    joint_angles: tuple[float, float, float],
    reference_angles: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> float:
    fk = forward_kinematics(geom, joint_angles)
    fk_ref = forward_kinematics(geom, reference_angles)

    L = tendon_path_length(fk, path)[0]
    L_ref = tendon_path_length(fk_ref, path)[0]

    return L - L_ref


def tendon_gradient(
    geom: FingerGeometry,
    path: RoutingPath,
    joint_angles: tuple[float, float, float],
    eps: float = 1e-6,
) -> np.ndarray:
    q = np.array(joint_angles, dtype=float)
    grad = np.zeros(3, dtype=float)

    for i in range(3):
        q_plus = q.copy()
        q_minus = q.copy()

        q_plus[i] += eps
        q_minus[i] -= eps

        fk_plus = forward_kinematics(geom, tuple(q_plus))
        fk_minus = forward_kinematics(geom, tuple(q_minus))

        l_plus = tendon_path_length(fk_plus, path)[0]
        l_minus = tendon_path_length(fk_minus, path)[0]

        grad[i] = (l_plus - l_minus) / (2.0 * eps)

    return grad


def tendon_torque(
    path: RoutingPath,
    geom: FingerGeometry,
    joint_angles: tuple[float, float, float],
    T: float,
) -> np.ndarray:
    return -T * tendon_gradient(geom, path, joint_angles)


def coordinated_flexion_sweep(
    n: int = 50,
    mcp_range_deg: tuple[float, float] = (0.0, -40.0),
    pip_scale: float = 1.5,
    dip_scale: float = 0.8,
) -> np.ndarray:
    mcp_vals = np.deg2rad(np.linspace(mcp_range_deg[0], mcp_range_deg[1], n))
    q_list = []

    for mcp in mcp_vals:
        pip = pip_scale * mcp
        dip = dip_scale * pip
        q_list.append((mcp, pip, dip))

    return np.asarray(q_list, dtype=float)

def evaluate_path_over_sweep(
    geom: FingerGeometry,
    path: RoutingPath,
    joint_angles_list: np.ndarray,
    reference_angles: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> dict[str, np.ndarray]:
    lengths = []
    excursions = []
    gradients = []
    torques_T1 = []

    for q in joint_angles_list:
        q_tuple = tuple(q)

        lengths.append(tendon_path_length(forward_kinematics(geom, q_tuple), path)[0])
        excursions.append(tendon_excursion(geom, path, q_tuple, reference_angles))
        grad = tendon_gradient(geom, path, q_tuple)
        gradients.append(grad)
        torques_T1.append(-1.0 * grad)

    return {
        "q": np.asarray(joint_angles_list),
        "L": np.asarray(lengths),
        "dL": np.asarray(excursions),
        "grad": np.asarray(gradients),
        "tau_T1": np.asarray(torques_T1),
    }
def make_length_vs_mcp_figure(flex_data: dict[str, np.ndarray], ext_data: dict[str, np.ndarray]) -> go.Figure:
    mcp_deg_flex = np.rad2deg(flex_data["q"][:, 0])
    mcp_deg_ext = np.rad2deg(ext_data["q"][:, 0])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=mcp_deg_flex,
        y=flex_data["L"],
        mode="lines",
        name="flex path length",
    ))

    fig.add_trace(go.Scatter(
        x=mcp_deg_ext,
        y=ext_data["L"],
        mode="lines",
        name="ext path length",
    ))

    fig.update_layout(
        title="Tendon path length vs MCP angle",
        xaxis_title="MCP angle (deg)",
        yaxis_title="Path length",
        template="plotly_white",
    )

    return fig

def make_excursion_vs_mcp_figure(flex_data: dict[str, np.ndarray], ext_data: dict[str, np.ndarray]) -> go.Figure:
    mcp_deg_flex = np.rad2deg(flex_data["q"][:, 0])
    mcp_deg_ext = np.rad2deg(ext_data["q"][:, 0])


    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=mcp_deg_flex,
        y=flex_data["dL"],
        mode="lines",
        name="flex excursion",
    ))

    fig.add_trace(go.Scatter(
        x=mcp_deg_ext,
        y=ext_data["dL"],
        mode="lines",
        name="ext excursion",
    ))

    fig.update_layout(
        title="Tendon excursion vs MCP angle",
        xaxis_title="MCP angle (deg)",
        yaxis_title="Excursion relative to neutral",
        template="plotly_white",
    )

    return fig

def make_gradient_figure(flex_data: dict[str, np.ndarray], ext_data: dict[str, np.ndarray] ) -> go.Figure:

    mcp_deg_flex = np.rad2deg(flex_data["q"][:, 0])
    mcp_deg_ext = np.rad2deg(ext_data["q"][:, 0])
        
    flex_grad_data = flex_data["grad"]
    ext_grad_data = ext_data["grad"]

    joint_names = ["dL/dthetaMCP", "dL/dthetaPIP", "dL/dthetaDIP"]

    fig = go.Figure()

    for col in range(flex_grad_data.shape[1]):

        fig.add_trace(go.Scatter(
            x=mcp_deg_flex,
            y=flex_grad_data[:, col],
            mode="lines",
            name=f"Flex {joint_names[col]}"
        ))

    for col in range(ext_grad_data.shape[1]):
            fig.add_trace(go.Scatter(
            x=mcp_deg_ext,
            y=ext_grad_data[:, col],
            mode="lines",
            name=f"Ext {joint_names[col]}"
        ))
            
    fig.update_layout(
        title="Path-length gradients vs MCP angle",
        xaxis_title="MCP angle (deg)",
        yaxis_title="Gradient",
        template="plotly_white",
    )

    return fig

def make_summary_figure(flex_data: dict[str, np.ndarray], ext_data: dict[str, np.ndarray]) -> go.Figure:

    # Create subplots: 1 row, 3 columns
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=("Path Length", "Excursion", "Gradients"),
        specs=[[{}, {}, {}]]
    )
    
    # Get individual figures
    fig_length = make_length_vs_mcp_figure(flex_data, ext_data)
    fig_excursion = make_excursion_vs_mcp_figure(flex_data, ext_data)
    fig_gradient = make_gradient_figure(flex_data, ext_data)
    
    # Extract traces from each figure and add to subplots
    for trace in fig_length.data:
        fig.add_trace(trace, row=1, col=1)
    
    for trace in fig_excursion.data:
        fig.add_trace(trace, row=1, col=2)
    
    for trace in fig_gradient.data:
        fig.add_trace(trace, row=1, col=3)
    
    # Update layout with shared styling
    fig.update_layout(
        height=400,
        width=1400,
        template="plotly_white",
        title_text="Tendon Routing Analysis Summary",
        showlegend=True,
    )
    
    # Update x-axis labels
    fig.update_xaxes(title_text="MCP angle (deg)", row=1, col=1)
    fig.update_xaxes(title_text="MCP angle (deg)", row=1, col=2)
    fig.update_xaxes(title_text="MCP angle (deg)", row=1, col=3)
    
    # Update y-axis labels
    fig.update_yaxes(title_text="Path length", row=1, col=1)
    fig.update_yaxes(title_text="Excursion", row=1, col=2)
    fig.update_yaxes(title_text="Gradient", row=1, col=3)
    
    return fig




if __name__ == "__main__":
    geom = FingerGeometry(7.0, 6.0, 6.0)

    h = 5.0   # channel offset in the 2D flexion plane
    u = 5.0   # element location along each phalanx
    x_entry = -20.0

    flexion_path = RoutingPath(
        "flexion_path",
        (
            RoutingElement("flex_entry", "world", "entry", np.array([x_entry, -h], dtype=float)),
            RoutingElement("flex_prox", "proximal", "guide", np.array([u, -h], dtype=float)),
            RoutingElement("flex_mid", "middle", "guide", np.array([u, -h], dtype=float)),
            RoutingElement("flex_dist", "distal", "anchor", np.array([u, -h], dtype=float)),
        ),
    )

    extension_path = RoutingPath(
        "extension_path",
        (
            RoutingElement("ext_entry", "world", "entry", np.array([x_entry, +h], dtype=float)),
            RoutingElement("ext_prox", "proximal", "guide", np.array([u, +h], dtype=float)),
            RoutingElement("ext_mid", "middle", "guide", np.array([u, +h], dtype=float)),
            RoutingElement("ext_dist", "distal", "anchor", np.array([u, +h], dtype=float)),
        ),
    )

    q = (
        np.deg2rad(-10.0),
        np.deg2rad(-25.0),
        np.deg2rad(-30.0),
    )

    fk = forward_kinematics(geom, q)

    flex_total, flex_segments, flex_points = tendon_path_length(fk, flexion_path)
    ext_total, ext_segments, ext_points = tendon_path_length(fk, extension_path)

    print(f"{flex_total=}, {flex_segments=}, {flex_points=}")
    print(f"{ext_total=}, {ext_segments=}, {ext_points=}")

    flex_exc = tendon_excursion(geom, flexion_path, q)
    ext_exc = tendon_excursion(geom, extension_path, q)

    flex_grad = tendon_gradient(geom, flexion_path, q)
    ext_grad = tendon_gradient(geom, extension_path, q)

    print(f"{flex_exc=}")
    print(f"{ext_exc=}")
    print(f"{flex_grad=}")
    print(f"{ext_grad=}")

    print("flex_tau_T1 =", tendon_torque(flexion_path, geom, q, 1.0))
    print("ext_tau_T1 =", tendon_torque(extension_path, geom, q, 1.0))

    q_sweep = coordinated_flexion_sweep(n=40)

    flex_data = evaluate_path_over_sweep(geom, flexion_path, q_sweep)
    ext_data = evaluate_path_over_sweep(geom, extension_path, q_sweep)

    print(flex_data["L"])
    print(flex_data["dL"])
    print(flex_data["grad"])

    fig1 = make_length_vs_mcp_figure(flex_data, ext_data)
    fig2 = make_excursion_vs_mcp_figure(flex_data, ext_data)
    fig3 = make_gradient_figure(flex_data, ext_data)

    fig4 = make_summary_figure(flex_data, ext_data)
    fig4.show()


