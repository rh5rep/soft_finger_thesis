from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from itertools import product
from pathlib import Path
import csv
import re

import numpy as np

from simulation_modeling import v01_model


RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_IMAGE_DIR = RESULTS_DIR / "candidate_run_images"


@dataclass(frozen=True)
class ModelParams:
    name: str
    size_name: str
    stiffness_name: str
    geom: v01_model.FingerGeometry
    joint_rest: tuple[float, float, float]
    stiffness: tuple[float, float, float]
    abstraction_name: str = "joint_space"


@dataclass(frozen=True)
class SharedRoutingGeometry:
    entry_body: str
    entry_local: tuple[float, float]
    splitter_body: str | None
    splitter_local: tuple[float, float] | None


@dataclass(frozen=True)
class BranchGeometry:
    """
    Branch-local routing description.

    `guide_longs` and `distal_anchor_long` are normalized longitudinal
    coordinates along the corresponding body segment, not absolute mm values.
    `guide_offsets` and `distal_anchor_offset` remain local perpendicular
    offsets in mm.
    """
    guide_bodies: tuple[str, ...]
    guide_longs: tuple[float, ...]
    guide_offsets: tuple[float, ...]
    distal_anchor_long: float
    distal_anchor_offset: float


@dataclass(frozen=True)
class CandidateGeometry:
    family: str
    shared: SharedRoutingGeometry
    branches: tuple[BranchGeometry, ...]


@dataclass(frozen=True)
class CandidateSpec:
    name: str
    geometry: CandidateGeometry


@dataclass(frozen=True)
class SweepSpec:
    name: str
    q_sweep: list[tuple[float, float, float]]


@dataclass(frozen=True)
class RejectLimits:
    max_tension: float
    max_pull: float
    max_tau_error: float
    max_branch_imbalance: float
    min_moment_arm_norm: float


@dataclass(frozen=True)
class CandidateSweepOutput:
    abstraction_name: str
    model_case_name: str
    size_name: str
    stiffness_name: str
    candidate_family: str
    candidate_name: str
    sweep_name: str
    q_sweep: np.ndarray
    tip_traj: np.ndarray
    tension_req: np.ndarray
    tau_req: np.ndarray
    tau_fit: np.ndarray
    tau_error: np.ndarray
    tau_error_rel: np.ndarray
    r_total: np.ndarray
    branch_pull: dict[str, np.ndarray]
    branch_imbalance: np.ndarray


@dataclass(frozen=True)
class CandidateResult:
    abstraction_name: str
    model_case_name: str
    size_name: str
    stiffness_name: str
    candidate_family: str
    candidate_name: str
    sweep_name: str
    peak_tension: float
    mean_tension: float
    peak_pull: float
    peak_branch_imbalance: float
    tau_error_rms: float
    tau_error_peak: float
    tau_error_rel_rms: float
    tau_error_rel_peak: float
    score: float | None
    rejected: bool
    reject_reasons: list[str]


@dataclass(frozen=True)
class ScoreWeights:
    w_tension: float
    w_tau_error: float
    w_pull: float
    w_balance: float
    w_smoothness: float


@dataclass(frozen=True)
class ExperimentRun:
    outputs: list[CandidateSweepOutput]
    results: list[CandidateResult]


def scale_finger_geometry(
    geom: v01_model.FingerGeometry,
    scale: float,
) -> v01_model.FingerGeometry:
    return v01_model.FingerGeometry(
        geom.l1 * scale,
        geom.l2 * scale,
        geom.l3 * scale,
        geom.d1 * scale,
        geom.d2 * scale,
        geom.d3 * scale,
    )


def make_coordinated_flexion_sweep(
    mcp_start_deg: float = 0.0,
    mcp_stop_deg: float = -40.0,
    n: int = 40,
    pip_over_mcp: float = 1.5,
    dip_over_pip: float = 0.8,
) -> list[tuple[float, float, float]]:
    mcp_vals = np.deg2rad(np.linspace(mcp_start_deg, mcp_stop_deg, n))
    q_sweep = []

    for mcp in mcp_vals:
        pip = mcp * pip_over_mcp
        dip = pip * dip_over_pip
        q_sweep.append((float(mcp), float(pip), float(dip)))

    return q_sweep


def fmt_num(x: float) -> str:
    return f"{x:.2f}".replace("+", "").replace(" ", "")


def make_candidate_name(
    family: str,
    guide_bodies: tuple[str, ...],
    guide_longs: tuple[float, ...],
    guide_offsets: tuple[float, ...],
    distal_anchor_long: float,
    distal_anchor_offset: float,
    tendon_entry: tuple[float, float],
) -> str:
    body_code = "_".join(b[0] for b in guide_bodies)
    long_code = "_".join(fmt_num(x) for x in guide_longs)
    offset_code = "_".join(fmt_num(x) for x in guide_offsets)
    entry_x, entry_y = tendon_entry

    return (
        f"{family}"
        f"_b-{body_code}"
        f"_l-{long_code}"
        f"_o-{offset_code}"
        f"_al-{fmt_num(distal_anchor_long)}"
        f"_ao-{fmt_num(distal_anchor_offset)}"
        f"_ex-{fmt_num(entry_x)}"
        f"_ey-{fmt_num(entry_y)}"
    )


def make_branch(
    guide_bodies: tuple[str, ...],
    guide_longs: tuple[float, ...],
    guide_offsets: tuple[float, ...],
    distal_anchor_long: float,
    distal_anchor_offset: float,
) -> BranchGeometry:
    # Longitudinal positions are normalized by body length; offsets stay in mm.
    assert len(guide_bodies) == len(guide_longs) == len(guide_offsets), \
    "guide_bodies, guide_longs, and guide_offsets must have the same length"

    valid_bodies = {"proximal", "middle", "distal", "world"}
    assert all(body in valid_bodies for body in guide_bodies), \
        f"guide_bodies must contain only valid body names: {valid_bodies}"
    return BranchGeometry(
    guide_bodies=guide_bodies,
    guide_longs=guide_longs,
    guide_offsets=guide_offsets,
    distal_anchor_long=distal_anchor_long,
    distal_anchor_offset=distal_anchor_offset,
    )


def validate_branch_geom(branch: BranchGeometry) -> bool:
    
    for long in branch.guide_longs:
        if long >= 1 or long <=0:
            return False
    
    if branch.distal_anchor_long <= 0 or branch.distal_anchor_long >= 1:
        return False
    
    return True

def validate_shared_geom(shared: SharedRoutingGeometry) -> bool:
    valid_bodies = {"world", "proximal", "middle", "distal"}

    if shared.entry_body not in valid_bodies:
        return False

    if (shared.splitter_body is None) != (shared.splitter_local is None):
        return False

    if shared.splitter_body is not None and shared.splitter_body not in valid_bodies:
        return False

    return True

def validate_candidate_geom(candidate: CandidateSpec) -> bool:
    if not validate_shared_geom(candidate.geometry.shared):
        return False

    if len(candidate.geometry.branches) == 0:
        return False

    for branch in candidate.geometry.branches:
        if not validate_branch_geom(branch):
            return False

    return True    

def make_candidate(
        family: str,
        shared: SharedRoutingGeometry,
        branches: tuple[BranchGeometry, ...],
        name: str,
) -> CandidateSpec:
    assert len(branches) > 0, \
    "branches must not be empty"

    return CandidateSpec(name, CandidateGeometry(family, shared, branches))


def make_tendon_input(candidate: CandidateSpec, model: ModelParams) -> v01_model.TendonInput:
    geom = model.geom
    c_geom = candidate.geometry 
    sg = c_geom.shared
    
    body_lengths = {
        "proximal": geom.l1,
        "middle": geom.l2,
        "distal": geom.l3,
    }

    branches = [] 

    assert ((sg.splitter_body is None) == (sg.splitter_local is None)), "splitter_body and splitter_local must be both set or both None"


    for branch_idx, bg in enumerate(c_geom.branches):
        elements = [] 

        elements.append(
            v01_model.RoutingElement(
                name="entry",
                body=sg.entry_body, 
                kind="entry",
                local=np.array(sg.entry_local, dtype=float),
            )
        )
                
        if sg.splitter_body is not None and sg.splitter_local is not None:
            elements.append(
            v01_model.RoutingElement(
                name="splitter",
                body=sg.splitter_body, 
                kind="splitter",
                local=np.array(sg.splitter_local, dtype=float),
            )
            )


        for i, (body, u, offset) in enumerate(
            zip(bg.guide_bodies, bg.guide_longs, bg.guide_offsets, strict=True)
        ):
            elements.append(
                v01_model.RoutingElement(
                    name=f"{body}_guide_{i}",
                    body=body,
                    kind="guide",
                    # `u` is a normalized fraction of the local body length.
                    local=np.array([u * body_lengths[body], offset], dtype=float),
                )
            )
        


        elements.append(
            v01_model.RoutingElement(
                name="distal_anchor",
                body="distal",
                kind="anchor",
                local=np.array(
                    # Distal anchor longitudinal position is also normalized.
                    [bg.distal_anchor_long * geom.l3, bg.distal_anchor_offset],
                    dtype=float,
                ),
            )
        )

        branch = v01_model.RoutingPath(
            name=f"{c_geom.family}_branch_{branch_idx}", 
            elements=tuple(elements),
        )

        branches.append(branch)

    return v01_model.TendonInput(
        name=candidate.name,  
        branches=tuple(branches), 
    )


def generate_two_guide_family(
        family: str,
        shared: SharedRoutingGeometry,
        guide_bodies: tuple[str, str],
        guide_long_sets: tuple[tuple[float, float], ...],
        guide_offset_sets: tuple[tuple[float, float], ...],
        distal_anchor_longs: tuple[float, ...],
        distal_anchor_offsets: tuple[float, ...],
) -> list[CandidateSpec]:
    
    candidates = []

    for guide_longs, guide_offsets, distal_anchor_long, distal_anchor_offset in product(
        guide_long_sets,
        guide_offset_sets,
        distal_anchor_longs,
        distal_anchor_offsets,
    ):
        branch = make_branch(
            guide_bodies=guide_bodies,
            guide_longs=guide_longs,
            guide_offsets=guide_offsets,
            distal_anchor_long=distal_anchor_long,
            distal_anchor_offset=distal_anchor_offset,
        )

        if not validate_branch_geom(branch):
            continue

        name = make_candidate_name(
            family=family,
            guide_bodies=guide_bodies,
            guide_longs=guide_longs,
            guide_offsets=guide_offsets,
            distal_anchor_long=distal_anchor_long,
            distal_anchor_offset=distal_anchor_offset,
            tendon_entry=shared.entry_local,
        )

        candidate = make_candidate(
            family=family,
            shared=shared,
            branches=(branch,),
            name=name,
        )

        if not validate_candidate_geom(candidate):
            continue

        candidates.append(candidate)

    return candidates

    
def compute_tau_error_relative(
    tau_error: np.ndarray,
    tau_req: np.ndarray,
    eps: float = 1e-9,
) -> np.ndarray:
    denom = np.maximum(np.abs(tau_req), eps)
    return tau_error / denom


def vector_norm_rows(values: np.ndarray) -> np.ndarray:
    return np.linalg.norm(values, axis=1)


def branch_peak_pull(branch_pull: dict[str, np.ndarray]) -> float:
    return max(float(np.max(np.abs(values))) for values in branch_pull.values())


def evaluate_candidate_over_sweep(
    candidate: CandidateSpec,
    model: ModelParams,
    sweep: SweepSpec,
) -> CandidateSweepOutput:
    tendon = make_tendon_input(candidate, model)
    q_sweep = np.asarray(sweep.q_sweep, dtype=float)
    fk_ref = v01_model.forward_kinematics(model.geom, model.joint_rest)

    tip_traj = []
    tension_req = []
    tau_req = []
    tau_fit = []
    tau_error = []
    r_total = []
    branch_imbalance = []
    branch_pull = {branch.name: [] for branch in tendon.branches}

    for q in q_sweep:
        q_tuple = tuple(float(x) for x in q)
        fk = v01_model.forward_kinematics(model.geom, q_tuple)

        tip_traj.append(v01_model.fingertip_position(model.geom, q_tuple))

        current_tau_req = v01_model.required_holding_torque(q_tuple, model.joint_rest, model.stiffness)
        current_tau_fit = v01_model.tau_fit(q_tuple, model.joint_rest, model.stiffness, model.geom, tendon)
        current_tau_error = v01_model.tau_error(q_tuple, model.joint_rest, model.stiffness, model.geom, tendon)
        current_r_total = v01_model.total_moment_arm(model.geom, tendon, q_tuple)
        current_tension = v01_model.least_squares_tension(q_tuple, model.joint_rest, model.stiffness, model.geom, tendon)
        current_branch_pull = v01_model.branch_pull_excursion(fk, fk_ref, tendon)
        current_branch_imbalance = v01_model.branch_imbalance(fk, fk_ref, tendon)

        tension_req.append(current_tension)
        tau_req.append(current_tau_req)
        tau_fit.append(current_tau_fit)
        tau_error.append(current_tau_error)
        r_total.append(current_r_total)
        branch_imbalance.append(current_branch_imbalance)

        for branch_name, value in current_branch_pull.items():
            branch_pull[branch_name].append(value)

    tau_req_arr = np.asarray(tau_req, dtype=float)
    tau_fit_arr = np.asarray(tau_fit, dtype=float)
    tau_error_arr = np.asarray(tau_error, dtype=float)

    return CandidateSweepOutput(
        abstraction_name=model.abstraction_name,
        model_case_name=model.name,
        size_name=model.size_name,
        stiffness_name=model.stiffness_name,
        candidate_family=candidate.geometry.family,
        candidate_name=candidate.name,
        sweep_name=sweep.name,
        q_sweep=q_sweep,
        tip_traj=np.asarray(tip_traj, dtype=float),
        tension_req=np.asarray(tension_req, dtype=float),
        tau_req=tau_req_arr,
        tau_fit=tau_fit_arr,
        tau_error=tau_error_arr,
        tau_error_rel=compute_tau_error_relative(tau_error_arr, tau_req_arr),
        r_total=np.asarray(r_total, dtype=float),
        branch_pull={name: np.asarray(values, dtype=float) for name, values in branch_pull.items()},
        branch_imbalance=np.asarray(branch_imbalance, dtype=float),
    )


def summarize_candidate_output(
    output: CandidateSweepOutput,
    reject_limits: RejectLimits,
    score_weights: ScoreWeights,
) -> CandidateResult:
    tau_error_norm = vector_norm_rows(output.tau_error)
    tau_error_rel_norm = vector_norm_rows(output.tau_error_rel)
    r_total_norm = vector_norm_rows(output.r_total)

    peak_tension = float(np.max(np.abs(output.tension_req)))
    mean_tension = float(np.mean(np.abs(output.tension_req)))
    peak_pull = branch_peak_pull(output.branch_pull)
    peak_branch_imbalance = float(np.max(np.abs(output.branch_imbalance)))
    tau_error_rms = float(np.sqrt(np.mean(tau_error_norm**2)))
    tau_error_peak = float(np.max(tau_error_norm))
    tau_error_rel_rms = float(np.sqrt(np.mean(tau_error_rel_norm**2)))
    tau_error_rel_peak = float(np.max(tau_error_rel_norm))

    reject_reasons: list[str] = []
    if peak_tension > reject_limits.max_tension:
        reject_reasons.append("peak_tension")
    if peak_pull > reject_limits.max_pull:
        reject_reasons.append("peak_pull")
    if tau_error_peak > reject_limits.max_tau_error:
        reject_reasons.append("tau_error_peak")
    if peak_branch_imbalance > reject_limits.max_branch_imbalance:
        reject_reasons.append("branch_imbalance")
    if float(np.min(r_total_norm)) < reject_limits.min_moment_arm_norm:
        reject_reasons.append("moment_arm_too_small")

    rejected = len(reject_reasons) > 0
    smoothness_penalty = float(np.mean(vector_norm_rows(np.diff(output.r_total, axis=0)))) if len(output.r_total) > 1 else 0.0

    score = None
    if not rejected:
        score = (
            score_weights.w_tension * (peak_tension / max(reject_limits.max_tension, 1e-9))
            + score_weights.w_tau_error * tau_error_rel_rms
            + score_weights.w_pull * (peak_pull / max(reject_limits.max_pull, 1e-9))
            + score_weights.w_balance * (peak_branch_imbalance / max(reject_limits.max_branch_imbalance, 1e-9))
            + score_weights.w_smoothness * smoothness_penalty
        )

    return CandidateResult(
        abstraction_name=output.abstraction_name,
        model_case_name=output.model_case_name,
        size_name=output.size_name,
        stiffness_name=output.stiffness_name,
        candidate_family=output.candidate_family,
        candidate_name=output.candidate_name,
        sweep_name=output.sweep_name,
        peak_tension=peak_tension,
        mean_tension=mean_tension,
        peak_pull=peak_pull,
        peak_branch_imbalance=peak_branch_imbalance,
        tau_error_rms=tau_error_rms,
        tau_error_peak=tau_error_peak,
        tau_error_rel_rms=tau_error_rel_rms,
        tau_error_rel_peak=tau_error_rel_peak,
        score=score,
        rejected=rejected,
        reject_reasons=reject_reasons,
    )


def raw_rows_from_output(output: CandidateSweepOutput) -> list[dict[str, float | str | int]]:
    rows = []
    branch_names = list(output.branch_pull.keys())

    for idx, q in enumerate(output.q_sweep):
        row = {
            "abstraction_name": output.abstraction_name,
            "model_case_name": output.model_case_name,
            "size_name": output.size_name,
            "stiffness_name": output.stiffness_name,
            "candidate_family": output.candidate_family,
            "candidate_name": output.candidate_name,
            "sweep_name": output.sweep_name,
            "posture_idx": idx,
            "q_mcp": float(q[0]),
            "q_pip": float(q[1]),
            "q_dip": float(q[2]),
            "tip_x": float(output.tip_traj[idx, 0]),
            "tip_y": float(output.tip_traj[idx, 1]),
            "T_req": float(output.tension_req[idx]),
            "tau_req_mcp": float(output.tau_req[idx, 0]),
            "tau_req_pip": float(output.tau_req[idx, 1]),
            "tau_req_dip": float(output.tau_req[idx, 2]),
            "tau_fit_mcp": float(output.tau_fit[idx, 0]),
            "tau_fit_pip": float(output.tau_fit[idx, 1]),
            "tau_fit_dip": float(output.tau_fit[idx, 2]),
            "tau_err_mcp": float(output.tau_error[idx, 0]),
            "tau_err_pip": float(output.tau_error[idx, 1]),
            "tau_err_dip": float(output.tau_error[idx, 2]),
            "tau_err_rel_mcp": float(output.tau_error_rel[idx, 0]),
            "tau_err_rel_pip": float(output.tau_error_rel[idx, 1]),
            "tau_err_rel_dip": float(output.tau_error_rel[idx, 2]),
            "tau_err_norm": float(np.linalg.norm(output.tau_error[idx])),
            "tau_err_rel_norm": float(np.linalg.norm(output.tau_error_rel[idx])),
            "r_total_mcp_mm": float(output.r_total[idx, 0]),
            "r_total_pip_mm": float(output.r_total[idx, 1]),
            "r_total_dip_mm": float(output.r_total[idx, 2]),
            "branch_imbalance": float(output.branch_imbalance[idx]),
        }

        for branch_idx, branch_name in enumerate(branch_names):
            row[f"branch_{branch_idx}_name"] = branch_name
            row[f"branch_{branch_idx}_pull_mm"] = float(output.branch_pull[branch_name][idx])

        rows.append(row)

    return rows


def summary_row_from_result(result: CandidateResult) -> dict[str, float | str | bool]:
    return {
        "abstraction_name": result.abstraction_name,
        "model_case_name": result.model_case_name,
        "size_name": result.size_name,
        "stiffness_name": result.stiffness_name,
        "candidate_family": result.candidate_family,
        "candidate_name": result.candidate_name,
        "sweep_name": result.sweep_name,
        "peak_tension": result.peak_tension,
        "mean_tension": result.mean_tension,
        "peak_pull_mm": result.peak_pull,
        "peak_branch_imbalance_mm": result.peak_branch_imbalance,
        "tau_error_rms": result.tau_error_rms,
        "tau_error_peak": result.tau_error_peak,
        "tau_error_rel_rms": result.tau_error_rel_rms,
        "tau_error_rel_peak": result.tau_error_rel_peak,
        "score": result.score,
        "rejected": result.rejected,
        "reject_reasons": "|".join(result.reject_reasons),
    }


def write_csv_rows(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_csv_rows(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    file_exists = path.exists()
    with path.open("a", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(rows)


def attach_run_label(rows: list[dict], run_label: str) -> list[dict]:
    return [{"run_label": run_label, **row} for row in rows]


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")
    return slug or "unnamed"


def candidate_run_image_dir(
    run_label: str,
    image_root: Path = RESULTS_IMAGE_DIR,
) -> Path:
    image_dir = image_root / safe_slug(run_label)
    image_dir.mkdir(parents=True, exist_ok=True)
    return image_dir


def save_plotly_figure_bundle(
    fig,
    run_label: str,
    stem: str,
    image_root: Path = RESULTS_IMAGE_DIR,
) -> tuple[Path, Path | None]:
    image_dir = candidate_run_image_dir(run_label, image_root=image_root)
    html_path = image_dir / f"{safe_slug(stem)}.html"
    png_path = image_dir / f"{safe_slug(stem)}.png"

    fig.write_html(html_path, include_plotlyjs="cdn")

    try:
        fig.write_image(png_path, scale=2)
    except Exception:
        png_path = None

    return html_path, png_path


def export_candidate_results(
    outputs: list[CandidateSweepOutput],
    results: list[CandidateResult],
    results_dir: Path = RESULTS_DIR,
    run_label: str | None = None,
) -> tuple[Path, Path, Path, Path]:
    if run_label is None:
        run_label = datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_rows = []
    for output in outputs:
        raw_rows.extend(raw_rows_from_output(output))

    summary_rows = [summary_row_from_result(result) for result in results]
    raw_rows_labeled = attach_run_label(raw_rows, run_label)
    summary_rows_labeled = attach_run_label(summary_rows, run_label)

    raw_path = results_dir / "candidate_sweep_raw.csv"
    summary_path = results_dir / "candidate_sweep_summary.csv"
    raw_history_path = results_dir / "candidate_sweep_raw_history.csv"
    summary_history_path = results_dir / "candidate_sweep_summary_history.csv"

    write_csv_rows(raw_path, raw_rows_labeled)
    write_csv_rows(summary_path, summary_rows_labeled)
    append_csv_rows(raw_history_path, raw_rows_labeled)
    append_csv_rows(summary_history_path, summary_rows_labeled)

    return raw_path, summary_path, raw_history_path, summary_history_path


def sort_candidate_results(results: list[CandidateResult]) -> list[CandidateResult]:
    return sorted(
        results,
        key=lambda result: (
            result.rejected,
            float("inf") if result.score is None else result.score,
            result.peak_tension,
        ),
    )


def run_experiment(
    model_cases: list[ModelParams],
    candidates: list[CandidateSpec],
    sweep_specs: list[SweepSpec],
    reject_limits: RejectLimits,
    score_weights: ScoreWeights,
) -> ExperimentRun:
    outputs: list[CandidateSweepOutput] = []
    results: list[CandidateResult] = []

    for model_case in model_cases:
        for candidate in candidates:
            for sweep in sweep_specs:
                output = evaluate_candidate_over_sweep(candidate, model_case, sweep)
                result = summarize_candidate_output(output, reject_limits, score_weights)
                outputs.append(output)
                results.append(result)

    return ExperimentRun(
        outputs=outputs,
        results=sort_candidate_results(results),
    )
