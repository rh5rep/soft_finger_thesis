from dataclasses import dataclass
import numpy as np
import math


@dataclass(frozen=True)
class StraightFingerGeometry:
    l1: float
    l2: float
    l3: float


@dataclass(frozen=True)
class RoutingElement:
    name: str
    frame: str
    kind: str
    local: tuple[float, float]

@dataclass(frozen=True)
class RoutingPath:
    name: str
    elements: tuple[RoutingElement, ...]

@dataclass(frozen=True)
class StraightTendonInput:
    name: str
    branches: tuple[RoutingPath, ...]

'''
start at neutral
have a certain MCP stiffness
have a certain angle to reach
calculate fingertip position
calculate routing points
calcualte tendon length
calcualte excursion
calculate sensitivity
calculate momentarm
calculate passive restoring 
'''

Vec2 = np.ndarray
ORIGIN = np.array([0.0, 0.0], dtype= float)

def rot2d(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=float)

def local_to_world(local_coords: Vec2, base_world_coords: Vec2, phi: float) -> Vec2:
    return base_world_coords + rot2d(phi) @ local_coords


def dist(p1: Vec2, p2: Vec2) -> float:
    return float(np.linalg.norm(p2-p1))

def fingertip_position(theta: float, geom: StraightFingerGeometry) -> Vec2:

    finger_length = geom.l1 + geom.l2+ geom.l3

    return np.array([finger_length*np.cos(theta), finger_length*np.sin(theta)], dtype=float)


def routing_point_world(elements: RoutingElement, theta: float) -> np.ndarray:
    frame = elements.frame.strip()
    if frame == "world":
        return np.asarray(elements.local, dtype=float)
    
    possible_frames = {"world", "finger"}

    if frame not in possible_frames:
        raise ValueError("expected world or finger")

    return local_to_world(np.asarray(elements.local, dtype=float), ORIGIN, theta)


def tendon_points_world(path: RoutingPath, theta: float) -> np.ndarray:

    world_points = []

    for element in path.elements:
        world_points.append(routing_point_world(element, theta))

    return np.asarray(world_points, dtype=float)

def tendon_path_length(path: RoutingPath, theta: float) -> float:

    elements = tendon_points_world(path, theta)

    return sum(dist(elements[i], elements[i+1]) for i in range(len(elements)-1))


def tendon_excursion(path: RoutingPath, theta: float, theta_ref: float) -> float:

    length_ref = tendon_path_length(path, theta_ref)
    length_path = tendon_path_length(path, theta)

    return length_ref-length_path


def tendon_sensitivity(path: RoutingPath, theta: float, eps: float) -> float:

    theta_plus = theta + eps
    theta_minus = theta - eps

    return (tendon_path_length(path, theta_plus) - tendon_path_length(path, theta_minus))/(2*eps)


def moment_arm(path: RoutingPath, theta: float, eps: float = 1e-6) -> float:

    return -tendon_sensitivity(path, theta, eps)


def passive_restoring_torque(theta: float, theta_neutral: float, k: float) -> float:
    return -k*(theta-theta_neutral)

def required_holding_torque(theta: float, theta_neutral: float, k: float) -> float:
    return -(passive_restoring_torque(theta, theta_neutral, k))

def tension_to_torque(T: float, path: RoutingPath, theta: float) -> float:
    return T * moment_arm(path, theta)


def required_tension(path: RoutingPath, theta: float, theta_neutral: float, k: float ) -> float:
    moment = moment_arm(path, theta)
    safe_moment = moment if abs(moment) > 1e-6 else math.copysign(1e-6, moment)

    return -passive_restoring_torque(theta, theta_neutral, k)/(safe_moment)
