from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np


'''
v01_model.py remains a planar sagittal-plane reduced-order model. 
Left/right side branches are represented as separate effective routing paths sharing one tension input. 
Full 3D routing is deferred until lateral clearance, branch imbalance, or CAD geometry becomes a limiting design factor.

'''

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
MM_TO_M = 1e-3


@dataclass 
class FingerGeometry:
    """
    Reduced-order 2D finger model.

    Assumptions:
    - planar 2D
    - 3 rigid phalanges
    - tendon routed through fixed element points attached to phalanges
    - total tendon length = sum of straight-line distances between consecutive routing points
    """

    l1: float
    l2: float
    l3: float

    d1: float
    d2: float
    d3: float


@dataclass
class FingerKinematics:
    joint_angles: tuple[float, float, float]
    J1: Vec2
    J2: Vec2
    J3: Vec2
    Fingertip: Vec2
    phi_mcp: float
    phi_pip: float
    phi_dip: float


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

@dataclass
class TendonInput:
    name: str
    branches: tuple[RoutingPath, ...]

@dataclass
class UnderactuatedTerms:
    r_total: np.ndarray
    tau_req: np.ndarray
    T_req: float

'''
method to implement rotation matrix
input: theta (float, rads)
output: np.ndarray of rotation
'''
def rot2d(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)

'''
metheod ot calcualte euclidean distance
inputs: 2 2d vectors (Vec2) of your points
output: float of the distance between teh two points
'''

def dist(p1: Vec2, p2: Vec2) -> float:
    return float(np.linalg.norm(p2-p1))

'''
method to translate local coords to world coords
input: local_coords (Vec2), base_world_coords (Vec2), phi (float) 
output: Vec2 of world coords
'''

def local_to_world(local_coords: Vec2, base_world_coords: Vec2, phi: float) -> Vec2:
    return base_world_coords + rot2d(phi) @ local_coords


'''
method to calcualte forward kinematics of finger based on certain joint angles 
inputs: geom (FingerGeometry), joint_angles tuple[float, float, float]
output: FingerKinematics
'''

def forward_kinematics(geom: FingerGeometry, joint_angles: tuple[float, float, float]) -> FingerKinematics:
    theta_mcp, theta_pip, theta_dip = joint_angles[0], joint_angles[1], joint_angles[2]

    phi_mcp = theta_mcp
    phi_pip = phi_mcp+theta_pip
    phi_dip = phi_pip+theta_dip

    J1 = np.array(ORIGIN, dtype=float)
    J2 = J1 + np.array([geom.l1 * np.cos(phi_mcp), geom.l1 * np.sin(phi_mcp)])
    J3 = J2 + np.array([(geom.l2) * np.cos(phi_pip), geom.l2 * np.sin(phi_pip)])
    Fingertip = J3 + np.array([geom.l3 * np.cos(phi_dip), geom.l3 * np.sin(phi_dip)])

    return FingerKinematics(
        joint_angles=joint_angles, J1=J1, J2=J2, J3=J3, Fingertip=Fingertip,
        phi_mcp = phi_mcp, phi_pip = phi_pip, phi_dip = phi_dip
    )


def element_world_position(element: RoutingElement, fk: FingerKinematics | None = None) -> Vec2:

    if element.body.strip().lower() == "world":
        return element.local
    
    if fk is None:
        raise ValueError(f"{element.body} requires finger kinematics on {element.name}.")
    
    frame_map = {
        "proximal": (fk.J1, fk.phi_mcp),
        "middle": (fk.J2, fk.phi_pip),
        "distal": (fk.J3, fk.phi_dip)
    }

    if element.body not in frame_map:
        raise ValueError(f"{element.body} not known.")
    
    base_world, phi = frame_map[element.body.strip().lower()]
    return local_to_world(element.local, base_world, phi)


def tendon_points_world(fk: FingerKinematics, path: RoutingPath) -> np.ndarray:
    
    points = []

    for element in path.elements:        
        points.append(element_world_position(element, fk))

    return np.asarray(points)


def tendon_path_length(fk: FingerKinematics, path: RoutingPath) -> tuple[float, list[float], np.array]:
    
    points = tendon_points_world(fk, path)
    segment_lengths = [dist(points[i], points[i+1]) for i in range(len(points)-1)]
    total = sum(segment_lengths)
    
    return total, segment_lengths, points


def branch_lengths_over_sweep(joint_angles_list: np.ndarray, geom: FingerGeometry, tendon: TendonInput) -> dict[str, np.ndarray]:
    
    lengths_by_branch = {}
    
    for branch in tendon.branches:
        branch_lengths = []
        for joint_angle in joint_angles_list:
                
            fk = forward_kinematics(geom, joint_angle)
            branch_lengths.append(tendon_path_length(fk, branch)[0])

        lengths_by_branch[branch.name] = np.asarray(branch_lengths)

    return lengths_by_branch

def _get_branch_length_at_pose(fk: FingerKinematics, tendon: TendonInput) -> dict[str, float]:
    length_at_pose = {}
    for branch in tendon.branches:
        total_length, _, _ = tendon_path_length(fk, branch)
        length_at_pose[branch.name] = total_length

    return length_at_pose

def branch_pull_excursion(fk: FingerKinematics, fk_ref: FingerKinematics, tendon: TendonInput) -> dict[str, float]:
    length_current = _get_branch_length_at_pose(fk, tendon)
    length_ref = _get_branch_length_at_pose(fk_ref, tendon)

    return {
        branch_name: length_ref[branch_name]- length_current[branch_name] for branch_name in length_current
    }

def total_branch_length_delta(geom: FingerGeometry, 
                     tendon: TendonInput,
                     joint_angles: tuple[float, float, float], 
                     joint_reference_angles: tuple[float, float, float]) -> float:


    length = []
    length_ref = []

    fk = forward_kinematics(geom, joint_angles)
    fk_ref = forward_kinematics(geom, joint_reference_angles)

    length = _get_branch_length_at_pose(fk, tendon)
    length_ref = _get_branch_length_at_pose(fk_ref, tendon)

    # Before: zip(length, length_ref) iterated over dictionary keys, not the
    # numerical branch lengths. After: preserve branch names and compare each
    # branch with its own reference length.
    return float(sum(
        length[branch_name] - length_ref[branch_name]
        for branch_name in length
    ))

def branch_imbalance(fk: FingerKinematics, fk_ref: FingerKinematics, tendon: TendonInput) -> float:

    excursions = branch_pull_excursion(fk, fk_ref, tendon)
    excursion_values = np.array(list(excursions.values()))
    
    if len(tendon.branches) == 2:
        return abs(excursion_values[0] - excursion_values[1])
    
    else:
        return float(np.std(excursion_values))

def tendon_sensitivity(geom: FingerGeometry, tendon: TendonInput,
                        joint_angles: tuple[float, float, float],
                        eps=1e-6) -> dict[str, np.ndarray]:
    
    num_joints = len(joint_angles)
    num_branches = len(tendon.branches)
    
    # Gradient matrix: rows = branches, columns = joints
    gradients = np.zeros((num_branches, num_joints))
    
    # For each joint angle
    for i in range(num_joints):
        # Perturb angle positively
        angles_plus = list(joint_angles)
        angles_plus[i] += eps
        fk_plus = forward_kinematics(geom, tuple(angles_plus))
        length_plus = _get_branch_length_at_pose(fk_plus, tendon)
        
        # Perturb angle negatively
        angles_minus = list(joint_angles)
        angles_minus[i] -= eps
        fk_minus = forward_kinematics(geom, tuple(angles_minus))
        length_minus = _get_branch_length_at_pose(fk_minus, tendon)
        
        # Central difference: (f+ - f-) / (2*h)
        for branch_index, branch in enumerate(tendon.branches):
            gradients[branch_index, i] = (length_plus[branch.name] - length_minus[branch.name])/(2*eps)
    
    # Before: the result was keyed by joint name, so each value was "all branch
    # sensitivities for MCP". That made it awkward to compute R_j(q).
    #
    # After: the result is keyed by branch name, so each value is one branch's
    # full gradient vector:
    #     dL_j/dq = [dL_j/dMCP, dL_j/dPIP, dL_j/dDIP]
    # This matches the math: R_total(q) = sum_j -dL_j/dq.
    return {
        branch.name: gradients[branch_index, :]
        for branch_index, branch in enumerate(tendon.branches)
    }


def moment_arms_by_branch(
    geom: FingerGeometry,
    tendon: TendonInput,
    joint_angles: tuple[float, float, float],
    eps: float = 1e-6,
) -> dict[str, np.ndarray]:
    # Before: R_j(q) only existed implicitly inside tendon_torque().
    # After: expose it directly so branch contributions can be inspected,
    # summed, plotted, and reused in least-squares tension fitting.
    sensitivity_by_branch = tendon_sensitivity(geom, tendon, joint_angles, eps=eps)
    return {
        branch_name: -gradient
        for branch_name, gradient in sensitivity_by_branch.items()
    }


def total_moment_arm(
    geom: FingerGeometry,
    tendon: TendonInput,
    joint_angles: tuple[float, float, float],
    eps: float = 1e-6,
) -> np.ndarray:
    # R_total is kept in the same geometric length unit as the routing model
    # (currently mm/rad). This is useful for design interpretation and plotting.
    r_by_branch = moment_arms_by_branch(geom, tendon, joint_angles, eps=eps)
    return np.sum(list(r_by_branch.values()), axis=0)


def moment_arms_by_branch_m(
    geom: FingerGeometry,
    tendon: TendonInput,
    joint_angles: tuple[float, float, float],
    eps: float = 1e-6,
) -> dict[str, np.ndarray]:
    # Convert geometric moment arms from mm/rad to m/rad before combining them
    # with torques in N·m or tensions in N.
    r_by_branch_mm = moment_arms_by_branch(geom, tendon, joint_angles, eps=eps)
    return {
        branch_name: MM_TO_M * r_branch
        for branch_name, r_branch in r_by_branch_mm.items()
    }


def total_moment_arm_m(
    geom: FingerGeometry,
    tendon: TendonInput,
    joint_angles: tuple[float, float, float],
    eps: float = 1e-6,
) -> np.ndarray:
    return MM_TO_M * total_moment_arm(geom, tendon, joint_angles, eps=eps)


def tendon_torque(geom: FingerGeometry,
                  joint_angles: tuple[float, float, float],
                  tendon: TendonInput,
                  T: float) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    # Before: this function mixed four layers:
    # dL/dq -> R_j -> R_total -> tau.
    # After: only the final mapping stays here:
    #     tau_tendon(q, T) = T * R_total(q)
    r_by_branch = moment_arms_by_branch_m(geom, tendon, joint_angles)
    r_total = total_moment_arm_m(geom, tendon, joint_angles)
    tau_total = T * r_total

    return (tau_total, r_by_branch)



def passive_restoring_torque(
    joints_angles: tuple[float, ...],
    joint_angles_rest: tuple[float, ...],
    k: tuple[float, ...],
) -> np.ndarray:
    # Restoring torque always points back toward neutral:
    # tau_passive = -k * (q - q0)
    num_joints = len(joints_angles)

    assert num_joints == len(joint_angles_rest) == len(k)

    restoring_torque_per_joint = np.zeros(num_joints)

    for i in range(num_joints):
        restoring_torque_per_joint[i] = -k[i] * (joints_angles[i] - joint_angles_rest[i])

    return restoring_torque_per_joint


def required_holding_torque(
    joints_angles: tuple[float, ...],
    joint_angles_rest: tuple[float, ...],
    k: tuple[float, ...],
) -> np.ndarray:
    # The actuator must provide the equal-and-opposite torque needed to hold the
    # displaced posture against passive restoring stiffness.
    return -passive_restoring_torque(joints_angles, joint_angles_rest, k)

def _underactuated_terms(joint_angles: tuple[float, ...],
                            joint_angles_rest: tuple[float, ...],
                            k: tuple[float, ...],
                            geom: FingerGeometry,
                            tendon: TendonInput,) -> UnderactuatedTerms:
    
    # Keep the least-squares fit in N·m by converting geometric moment arms
    # from mm/rad to m/rad at the torque/tension boundary.
    r_total = total_moment_arm_m(geom, tendon, joint_angles)
    tau_req = required_holding_torque(joint_angles, joint_angles_rest, k)
    numerator = np.dot(r_total, tau_req)
    denominator = np.dot(r_total, r_total)

    T_req = max(0.0, numerator/denominator if denominator != 0 else 0.0)

    return UnderactuatedTerms(r_total=r_total, tau_req=tau_req, T_req=T_req,)

def least_squares_tension(joint_angles: tuple[float, ...],
                            joint_angles_rest: tuple[float, ...],
                            k: tuple[float, ...],
                            geom: FingerGeometry,
                            tendon: TendonInput) -> float:
    
    return _underactuated_terms(joint_angles, joint_angles_rest, k, geom, tendon).T_req


def tau_fit(joint_angles: tuple[float, ...],
                            joint_angles_rest: tuple[float, ...],
                            k: tuple[float, ...],
                            geom: FingerGeometry,
                            tendon: TendonInput) -> np.ndarray:
    
    terms = _underactuated_terms(joint_angles, joint_angles_rest, k, geom, tendon)
    
    return terms.r_total*terms.T_req

def tau_error(joint_angles: tuple[float, ...],
                            joint_angles_rest: tuple[float, ...],
                            k: tuple[float, ...],
                            geom: FingerGeometry,
                            tendon: TendonInput) -> np.ndarray:
    
    fit = _underactuated_terms(joint_angles, joint_angles_rest, k, geom, tendon)
    
    return fit.tau_req - fit.r_total*fit.T_req


def fingertip_position(geom: FingerGeometry,
                      joint_angles: tuple[float, float, float]):
    return forward_kinematics(geom, joint_angles).Fingertip


def fingertip_trajectory(geom: FingerGeometry,
          joint_angles: tuple[float, ...]) -> np.ndarray:
    
    return np.array([fingertip_position(geom, q) for q in joint_angles])
