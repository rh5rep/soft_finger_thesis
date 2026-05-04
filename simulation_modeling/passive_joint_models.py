'''
This module defines passive joint torque laws for the reduced-order index finger.
It does not define tendon routing, actuator behavior, design scoring, or CAD geometry.
Angles follow the routing model convention: negative joint angles represent physiological flexion.
Returned torques are the actuator-side torques required to balance passive joint resistance.

'''

import numpy as np 
from dataclasses import dataclass


@dataclass
class PassiveJointParameters:
    joint_name: str
    neutral_angle: float
    k1_nm_per_rad: float
    k3_nm_per_rad3: float = 0.0
    law: str = "linear"


@dataclass
class PassiveFingerParameters:
    mcp: PassiveJointParameters
    pip: PassiveJointParameters
    dip: PassiveJointParameters


# passive torque = k(q-q0)

def passive_required_torque(theta_rad: float, params: PassiveJointParameters) -> float:
    delta = theta_rad - params.neutral_angle
    if params.law.lower().strip() == "linear":
        return params.k1_nm_per_rad * delta
    
    if params.law.lower().strip() == "cubic":
        return params.k1_nm_per_rad*delta + params.k3_nm_per_rad3*(delta**3)
    
    raise ValueError("not a law available.")
    

def passive_required_torque_vector(q_rad: tuple[float, float, float], finger_params: PassiveFingerParameters) -> np.ndarray:
    return np.array([
        passive_required_torque(q_rad[0], finger_params.mcp),
        passive_required_torque(q_rad[1], finger_params.pip),
        passive_required_torque(q_rad[2], finger_params.dip),
    ], dtype=float)

