from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from simulation_modeling import v0_model


DEFAULT_GEOMETRY_MM = v0_model.FingerGeometry(41.0, 26.0, 20.0)
DEFAULT_ENTRY_X_MM = -20.0
DEFAULT_MCP_RANGE_DEG = (0.0, -40.0)
DEFAULT_PIP_SCALE = 25.0 / 40.0
DEFAULT_DIP_SCALE = 10.0 / 25.0
LENGTH_SCALE_M = 1e-3
DEFAULT_TORQUE_TARGET_NM = 0.45


def make_candidate_path(
    name: str,
    *,
    h: float,
    prox_u: float | None = None,
    mid_u: float | None = None,
    dist_u: float = 5.0,
    entry_x: float = DEFAULT_ENTRY_X_MM,
) -> v0_model.RoutingPath:
    elements = [
        v0_model.RoutingElement("entry", "world", "entry", np.array([entry_x, -h], dtype=float)),
    ]
    if prox_u is not None:
        elements.append(
            v0_model.RoutingElement("prox_guide", "proximal", "guide", np.array([prox_u, -h], dtype=float))
        )
    if mid_u is not None:
        elements.append(
            v0_model.RoutingElement("mid_guide", "middle", "guide", np.array([mid_u, -h], dtype=float))
        )
    elements.append(
        v0_model.RoutingElement("dist_anchor", "distal", "anchor", np.array([dist_u, -h], dtype=float))
    )
    return v0_model.RoutingPath(name, tuple(elements))


def default_candidate_paths() -> dict[str, v0_model.RoutingPath]:
    return {
        "V0 thimble only": make_candidate_path("V0_thimble_only", h=5.0, prox_u=None, mid_u=None, dist_u=5.0),
        "V1 baseline two guides": make_candidate_path(
            "V1_baseline_two_guides", h=5.0, prox_u=5.0, mid_u=5.0, dist_u=5.0
        ),
        "V2 high offset two guides": make_candidate_path(
            "V2_high_offset_two_guides", h=9.0, prox_u=5.0, mid_u=5.0, dist_u=5.0
        ),
        "V3 proximal bias": make_candidate_path("V3_proximal_bias", h=5.0, prox_u=12.0, mid_u=4.0, dist_u=4.0),
        "V4 low offset two guides": make_candidate_path(
            "V4_low_offset_two_guides", h=2.5, prox_u=5.0, mid_u=5.0, dist_u=5.0
        ),
    }


def default_postures() -> tuple[np.ndarray, np.ndarray]:
    q_sweep = v0_model.coordinated_flexion_sweep(
        n=41,
        mcp_range_deg=DEFAULT_MCP_RANGE_DEG,
        pip_scale=DEFAULT_PIP_SCALE,
        dip_scale=DEFAULT_DIP_SCALE,
    )
    return q_sweep[0], q_sweep[-1]


def default_sweep() -> np.ndarray:
    return v0_model.coordinated_flexion_sweep(
        n=41,
        mcp_range_deg=DEFAULT_MCP_RANGE_DEG,
        pip_scale=DEFAULT_PIP_SCALE,
        dip_scale=DEFAULT_DIP_SCALE,
    )


def evaluate_candidates(
    geom: v0_model.FingerGeometry,
    candidate_paths: dict[str, v0_model.RoutingPath],
    q_sweep: np.ndarray,
) -> dict[str, dict[str, np.ndarray]]:
    return {
        name: v0_model.evaluate_path_over_sweep(geom, path, q_sweep)
        for name, path in candidate_paths.items()
    }


def finger_points(fk: v0_model.FingerKinematics) -> np.ndarray:
    return np.vstack([fk.J1, fk.J2, fk.J3, fk.Fingertip])


def add_pose_trace(
    fig: go.Figure,
    *,
    row: int,
    col: int,
    fk: v0_model.FingerKinematics,
    path: v0_model.RoutingPath,
    finger_name: str,
    tendon_name: str,
    finger_color: str,
    tendon_color: str,
    dash: str,
    showlegend: bool,
) -> None:
    hand_pts = finger_points(fk)
    tendon_pts = v0_model.tendon_path_points_world(fk, path)

    fig.add_trace(
        go.Scatter(
            x=hand_pts[:, 0],
            y=hand_pts[:, 1],
            mode="lines+markers",
            name=finger_name,
            line={"color": finger_color, "width": 5, "dash": dash},
            marker={"size": 7, "color": finger_color},
            showlegend=showlegend,
        ),
        row=row,
        col=col,
    )
    fig.add_trace(
        go.Scatter(
            x=tendon_pts[:, 0],
            y=tendon_pts[:, 1],
            mode="lines+markers",
            name=tendon_name,
            line={"color": tendon_color, "width": 3, "dash": dash},
            marker={"size": 6, "color": tendon_color},
            showlegend=showlegend,
        ),
        row=row,
        col=col,
    )


def build_routing_family_figure(
    geom: v0_model.FingerGeometry = DEFAULT_GEOMETRY_MM,
    candidate_paths: dict[str, v0_model.RoutingPath] | None = None,
) -> go.Figure:
    paths = default_candidate_paths() if candidate_paths is None else candidate_paths
    q_neutral, q_flexed = default_postures()
    fk_neutral = v0_model.forward_kinematics(geom, tuple(q_neutral))
    fk_flexed = v0_model.forward_kinematics(geom, tuple(q_flexed))

    cols = 3
    rows = int(np.ceil(len(paths) / cols))
    subplot_titles = list(paths.keys()) + [""] * (rows * cols - len(paths))
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)

    total_length = geom.l1 + geom.l2 + geom.l3
    x_min = DEFAULT_ENTRY_X_MM - 10.0
    x_max = total_length + 10.0
    y_min = -total_length
    y_max = total_length * 0.25

    for idx, (label, path) in enumerate(paths.items(), start=1):
        row = (idx - 1) // cols + 1
        col = (idx - 1) % cols + 1

        add_pose_trace(
            fig,
            row=row,
            col=col,
            fk=fk_neutral,
            path=path,
            finger_name="Neutral finger",
            tendon_name="Neutral routing",
            finger_color="#b0b0b0",
            tendon_color="#7a7a7a",
            dash="dash",
            showlegend=(idx == 1),
        )
        add_pose_trace(
            fig,
            row=row,
            col=col,
            fk=fk_flexed,
            path=path,
            finger_name="Flexed finger",
            tendon_name="Flexed routing",
            finger_color="#1f2937",
            tendon_color="#c2410c",
            dash="solid",
            showlegend=(idx == 1),
        )

        fig.update_xaxes(range=[x_min, x_max], zeroline=True, row=row, col=col)
        fig.update_yaxes(range=[y_min, y_max], zeroline=True, scaleanchor=f"x{idx}", scaleratio=1, row=row, col=col)

    fig.update_layout(
        title="Routing Families: Neutral and Flexed Overlays",
        template="plotly_white",
        height=350 * rows,
        width=420 * cols,
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "left", "x": 0.0},
        margin={"l": 30, "r": 30, "t": 80, "b": 30},
    )
    return fig


def build_routing_sweep_animation(
    geom: v0_model.FingerGeometry = DEFAULT_GEOMETRY_MM,
    candidate_paths: dict[str, v0_model.RoutingPath] | None = None,
) -> go.Figure:
    paths = default_candidate_paths() if candidate_paths is None else candidate_paths
    q_sweep = default_sweep()

    cols = 3
    rows = int(np.ceil(len(paths) / cols))
    subplot_titles = list(paths.keys()) + [""] * (rows * cols - len(paths))
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)

    total_length = geom.l1 + geom.l2 + geom.l3
    x_min = DEFAULT_ENTRY_X_MM - 10.0
    x_max = total_length + 10.0
    y_min = -total_length
    y_max = total_length * 0.25

    path_items = list(paths.items())
    initial_q = tuple(q_sweep[0])
    for idx, (label, path) in enumerate(path_items, start=1):
        row = (idx - 1) // cols + 1
        col = (idx - 1) % cols + 1
        fk = v0_model.forward_kinematics(geom, initial_q)
        hand_pts = finger_points(fk)
        tendon_pts = v0_model.tendon_path_points_world(fk, path)

        fig.add_trace(
            go.Scatter(
                x=hand_pts[:, 0],
                y=hand_pts[:, 1],
                mode="lines+markers",
                name="Finger",
                line={"color": "#1f2937", "width": 5},
                marker={"size": 7, "color": "#1f2937"},
                showlegend=(idx == 1),
            ),
            row=row,
            col=col,
        )
        fig.add_trace(
            go.Scatter(
                x=tendon_pts[:, 0],
                y=tendon_pts[:, 1],
                mode="lines+markers",
                name="Routing",
                line={"color": "#c2410c", "width": 3},
                marker={"size": 6, "color": "#c2410c"},
                showlegend=(idx == 1),
            ),
            row=row,
            col=col,
        )

        fig.update_xaxes(range=[x_min, x_max], zeroline=True, row=row, col=col)
        fig.update_yaxes(range=[y_min, y_max], zeroline=True, scaleanchor=f"x{idx}", scaleratio=1, row=row, col=col)

    frames = []
    for frame_idx, q in enumerate(q_sweep):
        frame_data = []
        mcp_deg = np.rad2deg(q[0])
        for _, path in path_items:
            fk = v0_model.forward_kinematics(geom, tuple(q))
            hand_pts = finger_points(fk)
            tendon_pts = v0_model.tendon_path_points_world(fk, path)
            frame_data.append(
                go.Scatter(
                    x=hand_pts[:, 0],
                    y=hand_pts[:, 1],
                    mode="lines+markers",
                    line={"color": "#1f2937", "width": 5},
                    marker={"size": 7, "color": "#1f2937"},
                    showlegend=False,
                )
            )
            frame_data.append(
                go.Scatter(
                    x=tendon_pts[:, 0],
                    y=tendon_pts[:, 1],
                    mode="lines+markers",
                    line={"color": "#c2410c", "width": 3},
                    marker={"size": 6, "color": "#c2410c"},
                    showlegend=False,
                )
            )
        frames.append(go.Frame(data=frame_data, name=str(frame_idx), layout={"title": f"Routing Sweep Animation (MCP {mcp_deg:.1f} deg)"}))

    fig.frames = frames
    fig.update_layout(
        title="Routing Sweep Animation",
        template="plotly_white",
        height=350 * rows,
        width=420 * cols,
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "left", "x": 0.0},
        margin={"l": 30, "r": 30, "t": 80, "b": 80},
        updatemenus=[
            {
                "type": "buttons",
                "showactive": False,
                "x": 0.0,
                "y": -0.08,
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [None, {"frame": {"duration": 80, "redraw": True}, "transition": {"duration": 0}, "fromcurrent": True}],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [[None], {"frame": {"duration": 0, "redraw": False}, "transition": {"duration": 0}, "mode": "immediate"}],
                    },
                ],
            }
        ],
        sliders=[
            {
                "x": 0.15,
                "y": -0.08,
                "len": 0.8,
                "currentvalue": {"prefix": "Frame: "},
                "steps": [
                    {
                        "label": str(i),
                        "method": "animate",
                        "args": [[str(i)], {"frame": {"duration": 0, "redraw": True}, "transition": {"duration": 0}, "mode": "immediate"}],
                    }
                    for i in range(len(q_sweep))
                ],
            }
        ],
    )
    return fig


def build_metrics_dashboard_animation(
    geom: v0_model.FingerGeometry = DEFAULT_GEOMETRY_MM,
    candidate_paths: dict[str, v0_model.RoutingPath] | None = None,
    torque_target_nm: float = DEFAULT_TORQUE_TARGET_NM,
) -> go.Figure:
    paths = default_candidate_paths() if candidate_paths is None else candidate_paths
    q_sweep = default_sweep()
    candidate_results = evaluate_candidates(geom, paths, q_sweep)
    path_items = list(paths.items())
    colors = ["#c2410c", "#2563eb", "#059669", "#7c3aed", "#dc2626"]
    color_map = {label: colors[i % len(colors)] for i, (label, _) in enumerate(path_items)}

    subplot_titles = list(paths.keys()) + ["Excursion vs MCP Angle", "Required Tension vs MCP Angle"]
    fig = make_subplots(
        rows=3,
        cols=3,
        subplot_titles=subplot_titles,
        specs=[
            [{}, {}, {}],
            [{}, {}, {}],
            [{"colspan": 2}, None, {}],
        ],
    )

    total_length = geom.l1 + geom.l2 + geom.l3
    x_min = DEFAULT_ENTRY_X_MM - 10.0
    x_max = total_length + 10.0
    y_min = -total_length
    y_max = total_length * 0.25
    mcp_deg = np.rad2deg(q_sweep[:, 0])

    routing_trace_count = 0
    marker_trace_count = 0
    initial_q = tuple(q_sweep[0])

    for idx, (label, path) in enumerate(path_items, start=1):
        row = (idx - 1) // 3 + 1
        col = (idx - 1) % 3 + 1
        fk = v0_model.forward_kinematics(geom, initial_q)
        hand_pts = finger_points(fk)
        tendon_pts = v0_model.tendon_path_points_world(fk, path)
        color = color_map[label]

        fig.add_trace(
            go.Scatter(
                x=hand_pts[:, 0],
                y=hand_pts[:, 1],
                mode="lines+markers",
                name=f"{label} finger",
                line={"color": "#1f2937", "width": 5},
                marker={"size": 6, "color": "#1f2937"},
                showlegend=False,
            ),
            row=row,
            col=col,
        )
        fig.add_trace(
            go.Scatter(
                x=tendon_pts[:, 0],
                y=tendon_pts[:, 1],
                mode="lines+markers",
                name=f"{label} routing",
                line={"color": color, "width": 3},
                marker={"size": 5, "color": color},
                showlegend=False,
            ),
            row=row,
            col=col,
        )
        routing_trace_count += 2

        fig.update_xaxes(range=[x_min, x_max], zeroline=True, row=row, col=col)
        fig.update_yaxes(range=[y_min, y_max], zeroline=True, scaleanchor=f"x{idx}", scaleratio=1, row=row, col=col)

    for label, _ in path_items:
        color = color_map[label]
        result = candidate_results[label]
        excursion = result["dL"]
        mcp_abs_grad_m = np.abs(result["grad"][:, 0]) * LENGTH_SCALE_M
        safe_grad = np.where(mcp_abs_grad_m > 1e-6, mcp_abs_grad_m, np.nan)
        required_tension = torque_target_nm / safe_grad

        fig.add_trace(
            go.Scatter(
                x=mcp_deg,
                y=excursion,
                mode="lines",
                name=label,
                line={"color": color, "width": 2},
                showlegend=True,
            ),
            row=3,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=[mcp_deg[0]],
                y=[excursion[0]],
                mode="markers",
                name=f"{label} marker",
                marker={"size": 10, "color": color},
                showlegend=False,
            ),
            row=3,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=mcp_deg,
                y=required_tension,
                mode="lines",
                name=f"{label} tension",
                line={"color": color, "width": 2},
                showlegend=False,
            ),
            row=3,
            col=3,
        )
        fig.add_trace(
            go.Scatter(
                x=[mcp_deg[0]],
                y=[required_tension[0]],
                mode="markers",
                name=f"{label} tension marker",
                marker={"size": 10, "color": color},
                showlegend=False,
            ),
            row=3,
            col=3,
        )
        marker_trace_count += 2

    excursion_min = min(np.min(result["dL"]) for result in candidate_results.values())
    excursion_max = max(np.max(result["dL"]) for result in candidate_results.values())
    tension_max = max(
        np.nanmax(torque_target_nm / np.where(np.abs(result["grad"][:, 0]) * LENGTH_SCALE_M > 1e-6, np.abs(result["grad"][:, 0]) * LENGTH_SCALE_M, np.nan))
        for result in candidate_results.values()
    )

    fig.update_xaxes(title_text="MCP angle (deg)", row=3, col=1)
    fig.update_yaxes(title_text="Excursion (mm)", range=[excursion_min * 1.1, excursion_max * 1.1 + 1e-9], row=3, col=1)
    fig.update_xaxes(title_text="MCP angle (deg)", row=3, col=3)
    fig.update_yaxes(title_text="Required tension (N)", range=[0.0, tension_max * 1.1], row=3, col=3)

    frames = []
    for frame_idx, q in enumerate(q_sweep):
        frame_data = []
        mcp_now_deg = float(np.rad2deg(q[0]))

        for label, path in path_items:
            color = color_map[label]
            fk = v0_model.forward_kinematics(geom, tuple(q))
            hand_pts = finger_points(fk)
            tendon_pts = v0_model.tendon_path_points_world(fk, path)
            frame_data.append(
                go.Scatter(
                    x=hand_pts[:, 0],
                    y=hand_pts[:, 1],
                    mode="lines+markers",
                    line={"color": "#1f2937", "width": 5},
                    marker={"size": 6, "color": "#1f2937"},
                    showlegend=False,
                )
            )
            frame_data.append(
                go.Scatter(
                    x=tendon_pts[:, 0],
                    y=tendon_pts[:, 1],
                    mode="lines+markers",
                    line={"color": color, "width": 3},
                    marker={"size": 5, "color": color},
                    showlegend=False,
                )
            )

        for label, _ in path_items:
            result = candidate_results[label]
            color = color_map[label]
            excursion = result["dL"]
            mcp_abs_grad_m = np.abs(result["grad"][:, 0]) * LENGTH_SCALE_M
            safe_grad = np.where(mcp_abs_grad_m > 1e-6, mcp_abs_grad_m, np.nan)
            required_tension = torque_target_nm / safe_grad
            frame_data.append(
                go.Scatter(
                    x=[mcp_deg[frame_idx]],
                    y=[excursion[frame_idx]],
                    mode="markers",
                    marker={"size": 10, "color": color},
                    showlegend=False,
                )
            )
            frame_data.append(
                go.Scatter(
                    x=[mcp_deg[frame_idx]],
                    y=[required_tension[frame_idx]],
                    mode="markers",
                    marker={"size": 10, "color": color},
                    showlegend=False,
                )
            )

        frames.append(
            go.Frame(
                data=frame_data,
                name=str(frame_idx),
                layout={"title": f"Routing and Metric Sweep Dashboard (MCP {mcp_now_deg:.1f} deg)"},
            )
        )

    fig.frames = frames
    fig.update_layout(
        title="Routing and Metric Sweep Dashboard",
        template="plotly_white",
        height=1050,
        width=1260,
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "left", "x": 0.0},
        margin={"l": 30, "r": 30, "t": 90, "b": 90},
        updatemenus=[
            {
                "type": "buttons",
                "showactive": False,
                "x": 0.0,
                "y": -0.06,
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [None, {"frame": {"duration": 80, "redraw": True}, "transition": {"duration": 0}, "fromcurrent": True}],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [[None], {"frame": {"duration": 0, "redraw": False}, "transition": {"duration": 0}, "mode": "immediate"}],
                    },
                ],
            }
        ],
        sliders=[
            {
                "x": 0.15,
                "y": -0.06,
                "len": 0.8,
                "currentvalue": {"prefix": "Frame: "},
                "steps": [
                    {
                        "label": str(i),
                        "method": "animate",
                        "args": [[str(i)], {"frame": {"duration": 0, "redraw": True}, "transition": {"duration": 0}, "mode": "immediate"}],
                    }
                    for i in range(len(q_sweep))
                ],
            }
        ],
    )
    return fig


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render routing-family overlays for the current candidate set.")
    parser.add_argument(
        "--html-out",
        type=Path,
        help="Optional path to write an interactive HTML figure.",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Build the figure without opening a viewer.",
    )
    parser.add_argument(
        "--animation-html-out",
        type=Path,
        help="Optional path to write an interactive sweep animation HTML figure.",
    )
    parser.add_argument(
        "--animation-only",
        action="store_true",
        help="Build only the sweep animation figure.",
    )
    parser.add_argument(
        "--dashboard-html-out",
        type=Path,
        help="Optional path to write a synchronized routing-plus-metrics animation HTML figure.",
    )
    parser.add_argument(
        "--dashboard-only",
        action="store_true",
        help="Build only the synchronized routing-plus-metrics animation figure.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    show_static = not args.animation_only and not args.dashboard_only
    fig = build_routing_family_figure() if show_static else None
    animation_fig = build_routing_sweep_animation() if args.animation_html_out is not None or args.animation_only else None
    dashboard_fig = build_metrics_dashboard_animation() if args.dashboard_html_out is not None or args.dashboard_only else None

    if fig is not None and args.html_out is not None:
        args.html_out.parent.mkdir(parents=True, exist_ok=True)
        fig.write_html(args.html_out)
        print(args.html_out)

    if animation_fig is not None and args.animation_html_out is not None:
        args.animation_html_out.parent.mkdir(parents=True, exist_ok=True)
        animation_fig.write_html(args.animation_html_out)
        print(args.animation_html_out)

    if dashboard_fig is not None and args.dashboard_html_out is not None:
        args.dashboard_html_out.parent.mkdir(parents=True, exist_ok=True)
        dashboard_fig.write_html(args.dashboard_html_out)
        print(args.dashboard_html_out)

    if not args.no_show and fig is not None:
        fig.show()
    if not args.no_show and animation_fig is not None:
        animation_fig.show()
    if not args.no_show and dashboard_fig is not None:
        dashboard_fig.show()


if __name__ == "__main__":
    main()
