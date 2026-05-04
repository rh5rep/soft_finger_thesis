import numpy as np
import pytest

from simulation_modeling.passive_joint_models import (PassiveFingerParameters, PassiveJointParameters, passive_required_torque, passive_required_torque_vector,)


def test_linear_required_torque_matches_k_delta():
    params = PassiveJointParameters(
        joint_name = "MCP",
        neutral_angle = 0.0,
        k1_nm_per_rad = .1,
        law = "LINEAR"
        )
    
    theta = np.deg2rad(30)

    assert passive_required_torque(theta, params) == pytest.approx(.1 * theta)


def test_negative_flexion_requires_negative_torque():
    params = PassiveJointParameters(
        joint_name = "MCP",
        neutral_angle = 0.0,
        k1_nm_per_rad = .1,
        law = "LINEAR"
            )
    
    theta = np.deg2rad(-30)

    assert passive_required_torque(theta, params) < 0

def test_cubic_passive_required_torque():
        params = PassiveJointParameters(
        joint_name = "PIP",
        neutral_angle = 0.0,
        k1_nm_per_rad = 0.1,
        k3_nm_per_rad3 = 0.02,
        law = "cubic",
        )
        
        theta = np.deg2rad(20)
        expected = 0.1 * theta + 0.02 * theta**3


        assert passive_required_torque(theta, params) == pytest.approx(expected)


def test_passive_required_torque_vector_returns_three_torques():
    finger_params = PassiveFingerParameters(
        mcp=PassiveJointParameters("MCP", 0.0, 0.1),
        pip=PassiveJointParameters("PIP", 0.0, 0.2),
        dip=PassiveJointParameters("DIP", 0.0, 0.3)
    )

    q = np.deg2rad([-10.0, -20.0, -30.0])

    torques = passive_required_torque_vector(q, finger_params)

    expected = np.array([.1 * q[0], .2 * q[1], .3 * q[2]])
    assert torques == pytest.approx(expected)
    assert torques.shape == (3,)


def test_unknown_passive_law_raises_error():
    params = PassiveJointParameters(
        joint_name="MCP",
        neutral_angle=0.0,
        k1_nm_per_rad=0.1,
        law="bad_law",
    )

    with pytest.raises(ValueError):
        passive_required_torque(0.1, params)