import importlib

from simulation_modeling.reduced_models import default_index_finger_parameters, default_parameters


def test_gui_launcher_points_to_streamlit_app():
    gui_app = importlib.import_module("simulation_modeling.gui_app")
    command = gui_app.launcher_command()

    assert command[1:4] == ["-m", "streamlit", "run"]
    assert command[4].endswith("simulation_modeling/streamlit_app.py")


def test_streamlit_app_builds_figures():
    streamlit_app = importlib.import_module("simulation_modeling.streamlit_app")
    params = default_parameters("index_mcp")
    snapshot = streamlit_app.compute_snapshot(params)

    geometry = streamlit_app.build_schematic_figure(params, snapshot["selected_equilibrium"])
    torque = streamlit_app.build_torque_figure(
        params,
        snapshot["theta_grid"],
        snapshot["passive_curve"],
        snapshot["actuator_curve"],
        snapshot["net_curve"],
        snapshot["equilibria"],
    )
    sweep = streamlit_app.build_sweep_figure(params, snapshot["sweep_inputs"], snapshot["sweep_branch_deg"])

    assert len(geometry.data) >= 2
    assert len(torque.data) == 3
    assert len(sweep.data) == 1


def test_streamlit_app_builds_index_finger_figures():
    streamlit_app = importlib.import_module("simulation_modeling.streamlit_app")
    params = default_index_finger_parameters()
    snapshot = streamlit_app.compute_index_snapshot(params)

    geometry = streamlit_app.build_index_finger_figure(params, snapshot["points"], snapshot["neutral_points"])
    joint_loads = streamlit_app.build_index_passive_torque_figure(
        snapshot["passive_torques"],
        snapshot["applied_torques"],
        snapshot["net_torques"],
        snapshot["local_stiffness"],
    )

    assert len(geometry.data) == 2
    assert len(joint_loads.data) == 4
