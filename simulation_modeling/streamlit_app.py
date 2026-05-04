from __future__ import annotations

from dataclasses import asdict

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from simulation_modeling.reduced_models import (
    INDEX_JOINT_LABELS,
    TEMPLATES,
    EquilibriumPoint,
    IndexFingerParameters,
    ModelParameters,
    actuator_torque,
    attachment_point,
    current_input_label,
    current_input_value,
    default_index_finger_parameters,
    default_parameters,
    equilibrium_branch,
    find_equilibria,
    index_finger_applied_torques,
    index_finger_joint_points,
    index_finger_local_passive_stiffness,
    index_finger_net_torques,
    index_finger_passive_required_torques,
    index_finger_tip_point,
    net_torque,
    passive_required_torque,
    resolved_index_joint_angles_rad,
    summary_text,
    sweep_input_values,
    tip_point,
)


def widget_defaults(digit_key: str, passive_law: str = "linear", actuator_mode: str = "joint_torque") -> dict[str, float | str]:
    params = default_parameters(digit_key)
    return {
        "digit_key": digit_key,
        "passive_law": passive_law,
        "actuator_mode": actuator_mode,
        "k1": params.k1,
        "k3": params.k3,
        "theta_0_deg": params.theta_0_deg,
        "link_length_mm": params.link_length_m * 1000.0,
        "joint_torque_nm": params.joint_torque_nm,
        "tendon_force_n": params.tendon_force_n,
        "anchor_x_mm": params.anchor_x_m * 1000.0,
        "anchor_y_mm": params.anchor_y_m * 1000.0,
        "attachment_fraction": params.attachment_fraction,
    }


def ensure_state_defaults(digit_key: str = "index_mcp") -> None:
    defaults = widget_defaults(digit_key)
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def state_value(key: str, default):
    return st.session_state.get(key, default)


def index_widget_defaults() -> dict[str, float | str]:
    params = default_index_finger_parameters()
    return {
        "index_passive_law": params.passive_law,
        "index_coupling_mode": params.coupling_mode,
        "index_mcp_length_mm": params.link_lengths_m[0] * 1000.0,
        "index_pip_length_mm": params.link_lengths_m[1] * 1000.0,
        "index_dip_length_mm": params.link_lengths_m[2] * 1000.0,
        "index_mcp_angle_deg": params.joint_angles_deg[0],
        "index_pip_angle_deg": params.joint_angles_deg[1],
        "index_dip_angle_deg": params.joint_angles_deg[2],
        "index_mcp_neutral_deg": params.neutral_angles_deg[0],
        "index_pip_neutral_deg": params.neutral_angles_deg[1],
        "index_dip_neutral_deg": params.neutral_angles_deg[2],
        "index_mcp_k1": params.k1[0],
        "index_pip_k1": params.k1[1],
        "index_dip_k1": params.k1[2],
        "index_mcp_k3": params.k3[0],
        "index_pip_k3": params.k3[1],
        "index_dip_k3": params.k3[2],
        "index_dip_pip_ratio": params.dip_pip_ratio,
        "index_applied_mcp_torque_nm": params.applied_mcp_torque_nm,
    }


def ensure_index_state_defaults() -> None:
    for key, value in index_widget_defaults().items():
        st.session_state.setdefault(key, value)


def reset_index_state() -> None:
    for key, value in index_widget_defaults().items():
        st.session_state[key] = value


def reset_state_for_digit(digit_key: str) -> None:
    passive_law = state_value("passive_law", "linear")
    actuator_mode = state_value("actuator_mode", "joint_torque")
    defaults = widget_defaults(digit_key, passive_law=passive_law, actuator_mode=actuator_mode)
    for key, value in defaults.items():
        if key == "digit_key":
            continue
        st.session_state[key] = value


def on_digit_template_change() -> None:
    reset_state_for_digit(state_value("digit_key", "index_mcp"))


def on_reset_selected_digit() -> None:
    reset_state_for_digit(state_value("digit_key", "index_mcp"))


def params_from_state() -> ModelParameters:
    digit_key = state_value("digit_key", "index_mcp")
    params = default_parameters(digit_key)
    params.passive_law = state_value("passive_law", "linear")
    params.actuator_mode = state_value("actuator_mode", "joint_torque")
    params.k1 = float(state_value("k1", params.k1))
    params.k3 = float(state_value("k3", params.k3))
    params.theta_0_deg = float(state_value("theta_0_deg", params.theta_0_deg))
    params.link_length_m = float(state_value("link_length_mm", params.link_length_m * 1000.0)) / 1000.0
    params.joint_torque_nm = float(state_value("joint_torque_nm", params.joint_torque_nm))
    params.tendon_force_n = float(state_value("tendon_force_n", params.tendon_force_n))
    params.anchor_x_m = float(state_value("anchor_x_mm", params.anchor_x_m * 1000.0)) / 1000.0
    params.anchor_y_m = float(state_value("anchor_y_mm", params.anchor_y_m * 1000.0)) / 1000.0
    params.attachment_fraction = float(state_value("attachment_fraction", params.attachment_fraction))
    return params


def index_params_from_state() -> IndexFingerParameters:
    params = default_index_finger_parameters()
    params.passive_law = state_value("index_passive_law", params.passive_law)
    params.coupling_mode = state_value("index_coupling_mode", params.coupling_mode)
    params.link_lengths_m = (
        float(state_value("index_mcp_length_mm", params.link_lengths_m[0] * 1000.0)) / 1000.0,
        float(state_value("index_pip_length_mm", params.link_lengths_m[1] * 1000.0)) / 1000.0,
        float(state_value("index_dip_length_mm", params.link_lengths_m[2] * 1000.0)) / 1000.0,
    )
    params.joint_angles_deg = (
        float(state_value("index_mcp_angle_deg", params.joint_angles_deg[0])),
        float(state_value("index_pip_angle_deg", params.joint_angles_deg[1])),
        float(state_value("index_dip_angle_deg", params.joint_angles_deg[2])),
    )
    params.neutral_angles_deg = (
        float(state_value("index_mcp_neutral_deg", params.neutral_angles_deg[0])),
        float(state_value("index_pip_neutral_deg", params.neutral_angles_deg[1])),
        float(state_value("index_dip_neutral_deg", params.neutral_angles_deg[2])),
    )
    params.k1 = (
        float(state_value("index_mcp_k1", params.k1[0])),
        float(state_value("index_pip_k1", params.k1[1])),
        float(state_value("index_dip_k1", params.k1[2])),
    )
    params.k3 = (
        float(state_value("index_mcp_k3", params.k3[0])),
        float(state_value("index_pip_k3", params.k3[1])),
        float(state_value("index_dip_k3", params.k3[2])),
    )
    params.dip_pip_ratio = float(state_value("index_dip_pip_ratio", params.dip_pip_ratio))
    params.applied_mcp_torque_nm = float(state_value("index_applied_mcp_torque_nm", params.applied_mcp_torque_nm))
    return params


def compute_snapshot(params: ModelParameters) -> dict[str, object]:
    theta_grid = np.deg2rad(np.linspace(params.angle_min_deg, params.angle_max_deg, 400))
    passive_curve = passive_required_torque(theta_grid, params)
    actuator_curve = actuator_torque(theta_grid, params)
    net_curve = net_torque(theta_grid, params)
    equilibria = find_equilibria(params)
    selected_equilibrium = equilibria[0] if equilibria else None
    sweep_inputs = sweep_input_values(params)
    sweep_branch_deg = equilibrium_branch(params, sweep_inputs)

    return {
        "theta_grid": theta_grid,
        "passive_curve": passive_curve,
        "actuator_curve": actuator_curve,
        "net_curve": net_curve,
        "equilibria": equilibria,
        "selected_equilibrium": selected_equilibrium,
        "sweep_inputs": sweep_inputs,
        "sweep_branch_deg": sweep_branch_deg,
    }


def compute_index_snapshot(params: IndexFingerParameters) -> dict[str, object]:
    joint_angles_rad = resolved_index_joint_angles_rad(params)
    points = index_finger_joint_points(params, joint_angles_rad)
    neutral_params = IndexFingerParameters(**vars(params))
    neutral_params.joint_angles_deg = params.neutral_angles_deg
    neutral_points = index_finger_joint_points(neutral_params)
    passive_torques = index_finger_passive_required_torques(params)
    applied_torques = index_finger_applied_torques(params)
    net_torques = index_finger_net_torques(params)
    local_stiffness = index_finger_local_passive_stiffness(params)

    return {
        "joint_angles_rad": joint_angles_rad,
        "points": points,
        "neutral_points": neutral_points,
        "passive_torques": passive_torques,
        "applied_torques": applied_torques,
        "net_torques": net_torques,
        "local_stiffness": local_stiffness,
        "tip": index_finger_tip_point(params),
    }


def build_schematic_figure(params: ModelParameters, equilibrium: EquilibriumPoint | None) -> go.Figure:
    figure = go.Figure()
    neutral_theta = np.deg2rad(params.theta_0_deg)
    theta = neutral_theta if equilibrium is None else equilibrium.theta_rad

    neutral_tip = tip_point(neutral_theta, params)
    tip = tip_point(theta, params)
    attachment = attachment_point(theta, params)[0]
    anchor = np.array([params.anchor_x_m, params.anchor_y_m])

    figure.add_trace(
        go.Scatter(
            x=[0.0, neutral_tip[0]],
            y=[0.0, neutral_tip[1]],
            mode="lines",
            name="Neutral",
            line={"color": "#b7b7b7", "dash": "dash"},
        )
    )
    figure.add_trace(
        go.Scatter(
            x=[0.0, tip[0]],
            y=[0.0, tip[1]],
            mode="lines+markers",
            name="Digit link",
            line={"color": "#005f73", "width": 5},
            marker={"size": [10, 12], "color": ["#111111", "#0a9396"]},
        )
    )

    if params.actuator_mode == "tendon":
        figure.add_trace(
            go.Scatter(
                x=[anchor[0], attachment[0]],
                y=[anchor[1], attachment[1]],
                mode="lines+markers",
                name="Tendon path",
                line={"color": "#bb3e03", "width": 3},
                marker={"size": [10, 10], "color": ["#ae2012", "#ee9b00"]},
            )
        )

    radius = params.link_length_m * 1.35
    figure.update_layout(
        title="Geometry View",
        template="plotly_white",
        xaxis_title="x [m]",
        yaxis_title="y [m]",
        showlegend=True,
        margin={"l": 20, "r": 20, "t": 50, "b": 20},
    )
    figure.update_xaxes(range=[-radius, radius], zeroline=True)
    figure.update_yaxes(range=[-radius * 0.4, radius], scaleanchor="x", scaleratio=1.0, zeroline=True)
    return figure


def build_index_finger_figure(params: IndexFingerParameters, points: np.ndarray, neutral_points: np.ndarray) -> go.Figure:
    figure = go.Figure()
    joint_labels = ["MCP/base", "PIP", "DIP", "Tip"]

    figure.add_trace(
        go.Scatter(
            x=neutral_points[:, 0],
            y=neutral_points[:, 1],
            mode="lines+markers",
            name="Neutral",
            line={"color": "#b7b7b7", "dash": "dash", "width": 3},
            marker={"size": 7, "color": "#b7b7b7"},
        )
    )
    figure.add_trace(
        go.Scatter(
            x=points[:, 0],
            y=points[:, 1],
            mode="lines+markers+text",
            name="Index finger",
            text=joint_labels,
            textposition="top center",
            line={"color": "#005f73", "width": 5},
            marker={"size": [11, 10, 10, 12], "color": ["#111111", "#0a9396", "#0a9396", "#ee9b00"]},
        )
    )

    total_length = sum(params.link_lengths_m)
    margin = total_length * 0.2
    figure.update_layout(
        title="3-Link Index Finger Geometry",
        template="plotly_white",
        xaxis_title="x [m]",
        yaxis_title="y [m]",
        showlegend=True,
        margin={"l": 20, "r": 20, "t": 50, "b": 20},
    )
    figure.update_xaxes(range=[-margin, total_length + margin], zeroline=True)
    figure.update_yaxes(range=[-total_length * 0.35, total_length], scaleanchor="x", scaleratio=1.0, zeroline=True)
    return figure


def build_index_passive_torque_figure(
    passive_torques: np.ndarray,
    applied_torques: np.ndarray,
    net_torques: np.ndarray,
    local_stiffness: np.ndarray,
) -> go.Figure:
    figure = go.Figure()
    labels = list(INDEX_JOINT_LABELS)
    figure.add_trace(
        go.Bar(
            x=labels,
            y=passive_torques,
            name="Required passive torque [N·m]",
            marker={"color": "#2a9d8f"},
        )
    )
    figure.add_trace(
        go.Bar(
            x=labels,
            y=applied_torques,
            name="Applied torque [N·m]",
            marker={"color": "#e76f51"},
        )
    )
    figure.add_trace(
        go.Bar(
            x=labels,
            y=net_torques,
            name="Net torque residual [N·m]",
            marker={"color": "#264653"},
        )
    )
    figure.add_trace(
        go.Scatter(
            x=labels,
            y=local_stiffness,
            mode="lines+markers",
            name="Local passive stiffness [N·m/rad]",
            yaxis="y2",
            line={"color": "#bb3e03", "width": 3},
        )
    )
    figure.update_layout(
        title="Passive Joint Loads",
        template="plotly_white",
        xaxis_title="Joint",
        yaxis_title="Torque [N·m]",
        yaxis2={"title": "Local stiffness [N·m/rad]", "overlaying": "y", "side": "right"},
        barmode="group",
        margin={"l": 20, "r": 20, "t": 50, "b": 20},
    )
    return figure


def build_torque_figure(
    params: ModelParameters,
    theta_grid: np.ndarray,
    passive_curve: np.ndarray,
    actuator_curve: np.ndarray,
    net_curve: np.ndarray,
    equilibria: list[EquilibriumPoint],
) -> go.Figure:
    theta_deg = np.rad2deg(theta_grid)
    interpretation = TEMPLATES[params.digit_key].interpretation_window_deg

    figure = go.Figure()
    figure.add_vrect(
        x0=interpretation[0],
        x1=interpretation[1],
        fillcolor="#d9f2d9",
        opacity=0.25,
        line_width=0,
        annotation_text="interpretation window",
        annotation_position="top left",
    )
    figure.add_trace(
        go.Scatter(x=theta_deg, y=passive_curve, mode="lines", name="Required passive torque", line={"color": "#2a9d8f"})
    )
    figure.add_trace(
        go.Scatter(x=theta_deg, y=actuator_curve, mode="lines", name="Actuator torque", line={"color": "#e76f51"})
    )
    figure.add_trace(
        go.Scatter(x=theta_deg, y=net_curve, mode="lines", name="Net torque", line={"color": "#264653", "dash": "dash"})
    )

    for equilibrium in equilibria:
        eq_deg = np.rad2deg(equilibrium.theta_rad)
        figure.add_vline(x=eq_deg, line_dash="dot", line_color="#7b2cbf")

    figure.update_layout(
        title="Torque Balance",
        template="plotly_white",
        xaxis_title="Angle [deg]",
        yaxis_title="Torque [N·m]",
        margin={"l": 20, "r": 20, "t": 50, "b": 20},
    )
    return figure


def build_sweep_figure(params: ModelParameters, sweep_inputs: np.ndarray, sweep_branch_deg: np.ndarray) -> go.Figure:
    interpretation = TEMPLATES[params.digit_key].interpretation_window_deg
    current_input = current_input_value(params)

    figure = go.Figure()
    figure.add_hrect(
        y0=interpretation[0],
        y1=interpretation[1],
        fillcolor="#d9f2d9",
        opacity=0.25,
        line_width=0,
        annotation_text="interpretation window",
        annotation_position="top left",
    )
    figure.add_trace(
        go.Scatter(
            x=sweep_inputs,
            y=sweep_branch_deg,
            mode="lines",
            name="Selected equilibrium branch",
            line={"color": "#005f73", "width": 3},
        )
    )
    figure.add_vline(x=current_input, line_dash="dash", line_color="#bb3e03")
    figure.update_layout(
        title="Equilibrium Sweep",
        template="plotly_white",
        xaxis_title=current_input_label(params),
        yaxis_title="Selected equilibrium angle [deg]",
        margin={"l": 20, "r": 20, "t": 50, "b": 20},
    )
    return figure


def summary_lines(params: ModelParameters, equilibria: list[EquilibriumPoint]) -> list[str]:
    lines = summary_text(params, equilibria).splitlines()
    lines.append(f"{current_input_label(params)}: {current_input_value(params):.3f}")
    return lines


def equation_block(params: ModelParameters) -> list[str]:
    equations = [r"\tau_{\mathrm{net}}(\theta) = \tau_{\mathrm{act}}(\theta) + \tau_{\mathrm{passive}}(\theta)"]
    if params.passive_law == "linear":
        equations.append(r"\tau_{\mathrm{passive}}(\theta) = -k_1(\theta - \theta_0)")
    else:
        equations.append(r"\tau_{\mathrm{passive}}(\theta) = -\left[k_1(\theta - \theta_0) + k_3(\theta - \theta_0)^3\right]")

    if params.actuator_mode == "joint_torque":
        equations.append(r"\tau_{\mathrm{act}}(\theta) = \tau_{\mathrm{app}}")
    else:
        equations.append(r"\tau_{\mathrm{act}}(\theta) = \mathbf{r}(\theta) \times \mathbf{F}_{\mathrm{tendon}}")

    equations.append(r"\text{Equilibrium occurs when } \tau_{\mathrm{net}}(\theta) = 0")
    return equations


def interpretation_points(params: ModelParameters) -> list[str]:
    input_name = "applied joint torque" if params.actuator_mode == "joint_torque" else "tendon force"
    return [
        "Geometry view: shows the current reduced finger pose and, in tendon mode, the straight-line actuator path from anchor to attachment.",
        "Torque balance: the equilibrium angle is where the actuator torque and passive resisting torque cancel, so the dashed net-torque curve crosses zero.",
        f"Equilibrium sweep: shows how the selected equilibrium angle changes as {input_name} is increased from zero.",
        "Green highlighted bands are only interpretation windows for the current thesis focus. They are not final anatomical limits.",
    ]


def literature_justification_points() -> list[str]:
    return [
        "The current thesis positioning memo argues that a reduced-order model is the right first step, because direct Parkinson tapping hardware is sparse while task-level observables are strong ([docs/TOPIC_MEMOS/08_thesis_positioning_and_research_questions.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/TOPIC_MEMOS/08_thesis_positioning_and_research_questions.md)).",
        "The repo synthesis says the strongest mechanical bridge comes from near-adjacent MCP and index-finger exoskeleton papers such as Sun 2021, Peperoni 2023, and Peperoni 2024, which justify starting from MCP-dominant or index-dominant abstractions rather than a full hand ([docs/TOPIC_MEMOS/08_thesis_positioning_and_research_questions.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/TOPIC_MEMOS/08_thesis_positioning_and_research_questions.md)).",
        "The finger-tapping technology memo also says the direct tapping literature is stronger on assessment than on actuation, so it is reasonable to let task papers define observables while near-adjacent exoskeleton papers define the mechanism baseline ([docs/TOPIC_MEMOS/06_pinch_finger_tapping_technologies.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/TOPIC_MEMOS/06_pinch_finger_tapping_technologies.md)).",
        "The paper tracker already flags Gallup 2025 as a strong match for a quasi-static reduced-order tendon-and-spring finger model and Zhou 2024 as useful for tendon-path variables and interpretable performance metrics, which is exactly the modeling direction this page is exploring ([refs/PAPER_TRACKER.csv](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/refs/PAPER_TRACKER.csv)).",
        "The thumb proxy is included as a comparison bucket because the repo also treats thumb-index opposition devices such as T-GRIP 2022 as relevant adjacent precedents, even if they are not the primary repetitive-motion hardware bridge ([docs/TOPIC_MEMOS/06_pinch_finger_tapping_technologies.md](/Users/rami/Documents/DTU/Thesis/soft_finger_thesis/docs/TOPIC_MEMOS/06_pinch_finger_tapping_technologies.md)).",
    ]


def render_sidebar() -> ModelParameters:
    ensure_state_defaults()

    digit_options = list(TEMPLATES.keys())
    st.sidebar.selectbox(
        "Digit template",
        options=digit_options,
        format_func=lambda key: TEMPLATES[key].label,
        key="digit_key",
        on_change=on_digit_template_change,
    )

    st.sidebar.selectbox("Passive law", options=["linear", "cubic"], key="passive_law")
    st.sidebar.selectbox("Actuator mode", options=["joint_torque", "tendon"], key="actuator_mode")

    st.sidebar.button("Reset selected digit", on_click=on_reset_selected_digit)

    st.sidebar.header("Parameters")
    st.sidebar.slider("k1 [N·m/rad]", 0.01, 0.30, key="k1", step=0.005)
    st.sidebar.slider(
        "k3 [N·m/rad³]",
        0.0,
        0.20,
        key="k3",
        step=0.002,
        disabled=state_value("passive_law", "linear") != "cubic",
    )
    st.sidebar.slider("Neutral angle [deg]", -30.0, 45.0, key="theta_0_deg", step=1.0)
    st.sidebar.slider("Link length [mm]", 20.0, 120.0, key="link_length_mm", step=1.0)
    st.sidebar.slider(
        "Joint torque [N·m]",
        -0.05,
        0.20,
        key="joint_torque_nm",
        step=0.002,
        disabled=state_value("actuator_mode", "joint_torque") != "joint_torque",
    )
    st.sidebar.slider(
        "Tendon force [N]",
        0.0,
        30.0,
        key="tendon_force_n",
        step=0.1,
        disabled=state_value("actuator_mode", "joint_torque") != "tendon",
    )
    st.sidebar.slider(
        "Anchor x [mm]",
        -60.0,
        30.0,
        key="anchor_x_mm",
        step=1.0,
        disabled=state_value("actuator_mode", "joint_torque") != "tendon",
    )
    st.sidebar.slider(
        "Anchor y [mm]",
        -30.0,
        60.0,
        key="anchor_y_mm",
        step=1.0,
        disabled=state_value("actuator_mode", "joint_torque") != "tendon",
    )
    st.sidebar.slider(
        "Attachment fraction",
        0.20,
        1.00,
        key="attachment_fraction",
        step=0.01,
        disabled=state_value("actuator_mode", "joint_torque") != "tendon",
    )

    st.sidebar.caption(
        "Assumptions: 1 DOF, quasi-static torque balance, no contact, no tendon wrapping, simplified thumb/index proxies."
    )
    return params_from_state()


def render_index_finger_sidebar() -> IndexFingerParameters:
    ensure_index_state_defaults()

    st.sidebar.selectbox("Passive law", options=["linear", "cubic"], key="index_passive_law")
    st.sidebar.selectbox(
        "Coupling mode",
        options=["none", "dip_pip_hard"],
        format_func=lambda key: "None" if key == "none" else "Hard DIP = ratio * PIP",
        key="index_coupling_mode",
    )
    st.sidebar.button("Reset 3-link index", on_click=reset_index_state)

    st.sidebar.header("Joint angles")
    st.sidebar.slider("MCP angle [deg]", -30.0, 110.0, key="index_mcp_angle_deg", step=1.0)
    st.sidebar.slider("PIP angle [deg]", -10.0, 120.0, key="index_pip_angle_deg", step=1.0)
    st.sidebar.slider(
        "DIP angle [deg]",
        -10.0,
        90.0,
        key="index_dip_angle_deg",
        step=1.0,
        disabled=state_value("index_coupling_mode", "none") == "dip_pip_hard",
    )
    st.sidebar.slider(
        "DIP/PIP ratio",
        0.20,
        1.00,
        key="index_dip_pip_ratio",
        step=0.01,
        disabled=state_value("index_coupling_mode", "none") != "dip_pip_hard",
    )

    st.sidebar.header("Phalanx lengths")
    st.sidebar.slider("Proximal phalanx [mm]", 25.0, 70.0, key="index_mcp_length_mm", step=1.0)
    st.sidebar.slider("Middle phalanx [mm]", 15.0, 45.0, key="index_pip_length_mm", step=1.0)
    st.sidebar.slider("Distal phalanx [mm]", 10.0, 35.0, key="index_dip_length_mm", step=1.0)

    st.sidebar.header("Neutral angles")
    st.sidebar.slider("MCP neutral [deg]", -20.0, 40.0, key="index_mcp_neutral_deg", step=1.0)
    st.sidebar.slider("PIP neutral [deg]", -20.0, 40.0, key="index_pip_neutral_deg", step=1.0)
    st.sidebar.slider("DIP neutral [deg]", -20.0, 40.0, key="index_dip_neutral_deg", step=1.0)

    st.sidebar.header("Passive stiffness")
    st.sidebar.slider("MCP k1 [N·m/rad]", 0.005, 0.30, key="index_mcp_k1", step=0.005)
    st.sidebar.slider("PIP k1 [N·m/rad]", 0.005, 0.25, key="index_pip_k1", step=0.005)
    st.sidebar.slider("DIP k1 [N·m/rad]", 0.005, 0.20, key="index_dip_k1", step=0.005)
    cubic_disabled = state_value("index_passive_law", "linear") != "cubic"
    st.sidebar.slider("MCP k3 [N·m/rad³]", 0.0, 0.20, key="index_mcp_k3", step=0.002, disabled=cubic_disabled)
    st.sidebar.slider("PIP k3 [N·m/rad³]", 0.0, 0.20, key="index_pip_k3", step=0.002, disabled=cubic_disabled)
    st.sidebar.slider("DIP k3 [N·m/rad³]", 0.0, 0.20, key="index_dip_k3", step=0.002, disabled=cubic_disabled)

    st.sidebar.header("Applied torque")
    st.sidebar.slider("Applied MCP torque [N·m]", -0.10, 0.20, key="index_applied_mcp_torque_nm", step=0.002)

    st.sidebar.caption(
        "Assumptions: planar 3-link kinematics, passive joint stiffness, applied MCP torque diagnostic only, no equilibrium solve yet."
    )
    return index_params_from_state()


def index_summary_lines(params: IndexFingerParameters, snapshot: dict[str, object]) -> list[str]:
    joint_angles = np.rad2deg(snapshot["joint_angles_rad"])
    tip = snapshot["tip"]
    torques = snapshot["passive_torques"]
    applied = snapshot["applied_torques"]
    net = snapshot["net_torques"]
    lines = [
        "Digit: 3-link index finger",
        f"Passive law: {params.passive_law}",
        f"Coupling mode: {params.coupling_mode}",
        f"Tip position: x={tip[0] * 1000.0:.1f} mm, y={tip[1] * 1000.0:.1f} mm",
        f"Applied MCP torque: {applied[0]:.3f} N·m",
        f"MCP net residual: {net[0]:.3f} N·m",
    ]
    for label, angle, torque in zip(INDEX_JOINT_LABELS, joint_angles, torques, strict=True):
        lines.append(f"{label}: {angle:.1f} deg, passive torque {torque:.3f} N·m")
    return lines


def index_equation_block(params: IndexFingerParameters) -> list[str]:
    equations = [
        r"q = [\theta_{\mathrm{MCP}}, \theta_{\mathrm{PIP}}, \theta_{\mathrm{DIP}}]",
        r"p_{\mathrm{tip}} = f_{\mathrm{FK}}(q, L_{\mathrm{prox}}, L_{\mathrm{mid}}, L_{\mathrm{dist}})",
    ]
    if params.passive_law == "linear":
        equations.append(r"\tau_{\mathrm{passive},i} = k_{1,i}(\theta_i - \theta_{0,i})")
    else:
        equations.append(r"\tau_{\mathrm{passive},i} = k_{1,i}(\theta_i - \theta_{0,i}) + k_{3,i}(\theta_i - \theta_{0,i})^3")
    equations.append(r"\tau_{\mathrm{app}} = [\tau_{\mathrm{MCP}}, 0, 0]")
    equations.append(r"\tau_{\mathrm{res}} = \tau_{\mathrm{app}} - \tau_{\mathrm{passive}}")
    if params.coupling_mode == "dip_pip_hard":
        equations.append(r"\theta_{\mathrm{DIP}} = \alpha \theta_{\mathrm{PIP}}")
    return equations


def index_interpretation_points(params: IndexFingerParameters) -> list[str]:
    points = [
        "Geometry view: shows a planar MCP-PIP-DIP chain with proximal, middle, and distal phalanges.",
        "Joint-load view: compares passive torque required at the current pose with the applied MCP torque and resulting residual.",
        "This mode does not solve for a new pose yet. It only shows whether the selected MCP torque is enough to balance the current MCP passive load.",
        "This is the foundation for later tendon, zig-zag, or antagonistic actuator branches.",
    ]
    if params.coupling_mode == "dip_pip_hard":
        points.append("Hard coupling overrides the DIP slider and sets DIP angle as a fixed ratio of PIP angle.")
    return points


def render_app() -> None:
    st.set_page_config(page_title="Reduced Finger Model Explorer", layout="wide")
    st.title("Reduced-Order Finger Model Explorer")
    st.caption(
        "Browser-based GUI for quick thesis-side exploration of thumb and index reduced models, passive laws, and actuator placement."
    )

    st.sidebar.header("Model setup")
    model_family = st.sidebar.selectbox(
        "Model family",
        options=["one_dof", "index_3_link"],
        format_func=lambda key: "1-DOF torque balance" if key == "one_dof" else "3-link index kinematics",
        key="model_family",
    )

    if model_family == "index_3_link":
        render_index_finger_app()
        return

    params = render_sidebar()
    snapshot = compute_snapshot(params)

    summary_col, data_col = st.columns([1.1, 1.6], gap="large")
    with summary_col:
        st.subheader("Current state")
        for line in summary_lines(params, snapshot["equilibria"]):
            st.write(line)

        with st.expander("Parameter snapshot", expanded=False):
            st.json(asdict(params))

        with st.expander("Model equations", expanded=True):
            st.markdown("This page is currently a **1-DOF quasi-static torque-balance model**.")
            for equation in equation_block(params):
                st.latex(equation)

        with st.expander("How To Read This Page", expanded=True):
            for point in interpretation_points(params):
                st.markdown(f"- {point}")

    with data_col:
        st.subheader("Geometry")
        st.plotly_chart(build_schematic_figure(params, snapshot["selected_equilibrium"]), use_container_width=True)

    plot_col_1, plot_col_2 = st.columns(2, gap="large")
    with plot_col_1:
        st.plotly_chart(
            build_torque_figure(
                params,
                snapshot["theta_grid"],
                snapshot["passive_curve"],
                snapshot["actuator_curve"],
                snapshot["net_curve"],
                snapshot["equilibria"],
            ),
            use_container_width=True,
        )
    with plot_col_2:
        st.plotly_chart(
            build_sweep_figure(params, snapshot["sweep_inputs"], snapshot["sweep_branch_deg"]),
            use_container_width=True,
        )

    st.markdown(
        """
        **Scope**

        This remains a reduced-order exploration tool, not a validated anatomical simulator.
        The next meaningful upgrade is a 2-link index model and a thumb-index gap or pinch metric.
        """
    )

    with st.expander("Why This Model Is Defensible Right Now", expanded=False):
        st.markdown(
            "This is not justified as the final thesis model yet. It is justified as the **current first-pass thesis model** from the repo's literature synthesis:"
        )
        for point in literature_justification_points():
            st.markdown(f"- {point}")


def render_index_finger_app() -> None:
    params = render_index_finger_sidebar()
    snapshot = compute_index_snapshot(params)

    summary_col, data_col = st.columns([1.1, 1.6], gap="large")
    with summary_col:
        st.subheader("Current state")
        for line in index_summary_lines(params, snapshot):
            st.write(line)

        with st.expander("Parameter snapshot", expanded=False):
            st.json(asdict(params))

        with st.expander("Model equations", expanded=True):
            st.markdown("This page is currently a **3-link planar kinematic/passive model**.")
            for equation in index_equation_block(params):
                st.latex(equation)

        with st.expander("How To Read This Page", expanded=True):
            for point in index_interpretation_points(params):
                st.markdown(f"- {point}")

    with data_col:
        st.subheader("Geometry")
        st.plotly_chart(
            build_index_finger_figure(params, snapshot["points"], snapshot["neutral_points"]),
            use_container_width=True,
        )

    st.plotly_chart(
        build_index_passive_torque_figure(
            snapshot["passive_torques"],
            snapshot["applied_torques"],
            snapshot["net_torques"],
            snapshot["local_stiffness"],
        ),
        use_container_width=True,
    )

    st.markdown(
        """
        **Scope**

        This mode adds MCP/PIP/DIP geometry and passive joint loads only.
        The next meaningful upgrade is to connect this finger chain to a tendon or dorsal zig-zag actuator branch.
        """
    )


if __name__ == "__main__":
    render_app()
