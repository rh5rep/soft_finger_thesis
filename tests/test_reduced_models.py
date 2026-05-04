import numpy as np
import pytest

from simulation_modeling.reduced_models import (
    actuator_torque,
    default_index_finger_parameters,
    default_parameters,
    equilibrium_branch,
    find_equilibria,
    index_finger_applied_torques,
    index_finger_joint_points,
    index_finger_net_torques,
    index_finger_passive_required_torques,
    passive_required_torque,
    resolved_index_joint_angles_rad,
)


def test_linear_joint_torque_equilibrium_matches_analytic_solution():
    params = default_parameters("index_mcp")
    params.passive_law = "linear"
    params.actuator_mode = "joint_torque"
    params.k1 = 0.08
    params.theta_0_deg = 0.0
    params.joint_torque_nm = 0.04

    equilibria = find_equilibria(params)

    assert len(equilibria) == 1
    expected_deg = np.rad2deg(params.joint_torque_nm / params.k1)
    assert np.rad2deg(equilibria[0].theta_rad) == pytest.approx(expected_deg, abs=0.1)


def test_cubic_passive_required_torque_matches_formula():
    params = default_parameters("thumb_proxy")
    params.passive_law = "cubic"
    params.k1 = 0.06
    params.k3 = 0.02
    params.theta_0_deg = 5.0

    theta = np.deg2rad(25.0)
    delta = theta - np.deg2rad(params.theta_0_deg)
    expected = params.k1 * delta + params.k3 * delta**3

    assert passive_required_torque(theta, params) == pytest.approx(expected)


def test_tendon_actuator_torque_changes_with_anchor_location():
    params = default_parameters("index_mcp")
    params.actuator_mode = "tendon"
    params.tendon_force_n = 6.0
    params.anchor_x_m = -0.02
    params.anchor_y_m = 0.02
    theta = np.deg2rad(20.0)

    torque_one = actuator_torque(theta, params)
    params.anchor_y_m = 0.04
    torque_two = actuator_torque(theta, params)

    assert torque_two != pytest.approx(torque_one)


def test_equilibrium_branch_is_monotonic_for_linear_joint_torque_case():
    params = default_parameters("index_mcp")
    params.passive_law = "linear"
    params.actuator_mode = "joint_torque"
    params.k1 = 0.08
    inputs = np.linspace(0.0, 0.08, 6)

    branch = equilibrium_branch(params, inputs)

    assert np.all(np.diff(branch) >= -1e-6)


def test_index_finger_geometry_has_four_points_and_expected_neutral_tip():
    params = default_index_finger_parameters()
    params.joint_angles_deg = (0.0, 0.0, 0.0)

    points = index_finger_joint_points(params)

    assert points.shape == (4, 2)
    assert points[-1, 0] == pytest.approx(sum(params.link_lengths_m))
    assert points[-1, 1] == pytest.approx(0.0)


def test_index_finger_hard_dip_pip_coupling_overrides_dip_angle():
    params = default_index_finger_parameters()
    params.coupling_mode = "dip_pip_hard"
    params.joint_angles_deg = (10.0, 30.0, 80.0)
    params.dip_pip_ratio = 0.5

    angles = np.rad2deg(resolved_index_joint_angles_rad(params))

    assert angles[0] == pytest.approx(10.0)
    assert angles[1] == pytest.approx(30.0)
    assert angles[2] == pytest.approx(15.0)


def test_index_finger_passive_torques_match_linear_formula():
    params = default_index_finger_parameters()
    params.passive_law = "linear"
    params.joint_angles_deg = (20.0, 30.0, 40.0)
    params.neutral_angles_deg = (5.0, 10.0, 15.0)
    params.k1 = (0.1, 0.2, 0.3)

    expected = np.asarray(params.k1) * np.deg2rad(np.asarray([15.0, 20.0, 25.0]))

    assert index_finger_passive_required_torques(params) == pytest.approx(expected)


def test_index_finger_applied_mcp_torque_creates_net_residual():
    params = default_index_finger_parameters()
    params.passive_law = "linear"
    params.joint_angles_deg = (10.0, 0.0, 0.0)
    params.neutral_angles_deg = (0.0, 0.0, 0.0)
    params.k1 = (0.1, 0.1, 0.1)
    params.applied_mcp_torque_nm = 0.05

    applied = index_finger_applied_torques(params)
    passive = index_finger_passive_required_torques(params)
    net = index_finger_net_torques(params)

    assert applied == pytest.approx([0.05, 0.0, 0.0])
    assert net == pytest.approx(applied - passive)
