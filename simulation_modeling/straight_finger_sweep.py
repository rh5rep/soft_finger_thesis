from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from simulation_modeling import straight_finger_model
from simulation_modeling.candidate_sweep_utils import (
    CandidateSpec,
    RejectLimits,
    ScoreWeights,
)


@dataclass(frozen=True)
class ModelParams:
    name: str
    size_name: str
    stiffness_name: str
    geom: straight_finger_model.StraightFingerGeometry
    joint_rest: float
    stiffness: float
    abstraction_name: str = "straight_finger"


@dataclass(frozen=True)
class SweepSpec:
    name: str
    theta_sweep: list[float]


@dataclass(frozen=True)
class CandidateSweepOutput:
    abstraction_name: str
    model_case_name: str
    size_name: str
    stiffness_name: str
    candidate_family: str
    candidate_name: str
    sweep_name: str
    theta_sweep: np.ndarray
    tau_req: np.ndarray
    tip_traj: np.ndarray
    tension_req: np.ndarray
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
    score: float | None
    rejected: bool
    reject_reasons: list[str]



def make_tendon_input(candidate: CandidateSpec, model: ModelParams) -> straight_finger_model.StraightTendonInput:
    sg = candidate.geometry.shared
    bg = candidate.geometry.branches

    branches = []


    assert ((sg.splitter_body is None) == (sg.splitter_local is None)), "splitter_body and splitter_local must be both set or both None"

    
    for branch_idx, branch in enumerate(bg):
        elements = []

        elements.append(straight_finger_model.RoutingElement(name="entry", kind="entry", frame="world", local=sg.entry_local))



        if sg.splitter_body is not None and sg.splitter_local is not None:
            elements.append(straight_finger_model.RoutingElement(name="splitter", kind="splitter", frame="finger", local=sg.splitter_local))

        body_starts = {
            "proximal": 0.0,
            "middle": model.geom.l1,
            "distal": model.geom.l1 + model.geom.l2,
        }
        
        body_lengths = {
            "proximal": model.geom.l1,
            "middle": model.geom.l2,
            "distal": model.geom.l3,
        }

        for i, (body, u, offset) in enumerate(zip(branch.guide_bodies, branch.guide_longs, branch.guide_offsets)):
            s = body_starts[body] + u * body_lengths[body]
            elements.append(straight_finger_model.RoutingElement(name=f"guide_{i}",  kind="guide",  frame="finger", local=(s, offset)))


        s_anchor = body_starts["distal"] + branch.distal_anchor_long * model.geom.l3

        elements.append(straight_finger_model.RoutingElement(name="distal_anchor", kind="anchor", frame="finger", local=(s_anchor, branch.distal_anchor_offset)))

        branch = straight_finger_model.RoutingPath(
            name=f"{candidate.geometry.family}_branch_{branch_idx}",
            elements=tuple(elements),
        )

        branches.append(branch)

    return straight_finger_model.StraightTendonInput(name=candidate.name, branches=tuple(branches))

def moment_arm_per_branch(
        tendon: straight_finger_model.StraightTendonInput,
        theta: float,
        eps: float = 1e-6,
) -> dict[str, float]:
    
    return {
        branch.name: straight_finger_model.moment_arm(branch, theta, eps=eps)
        for branch in tendon.branches
    }


def total_moment_arm(tendon: straight_finger_model.StraightTendonInput,
                     theta: float,
                     eps: float = 1e-6,) -> float:
    
    moment_arms = moment_arm_per_branch(tendon, theta, eps)
    return float(sum(moment_arms.values()))

def branch_pull_at_theta(
    tendon: straight_finger_model.StraightTendonInput,
    theta: float,
    theta_ref: float,
) -> dict[str, np.ndarray]:
    return {
        branch.name: straight_finger_model.tendon_excursion(branch, theta, theta_ref)
        for branch in tendon.branches
    }


def required_tension_total(tendon: straight_finger_model.StraightTendonInput, theta: float, theta_neutral: float, k: float) -> float:

    tau_hold = straight_finger_model.required_holding_torque(theta, theta_neutral, k)
    r_total = total_moment_arm(tendon, theta)

    safe_r_total = r_total if abs(r_total) > 1e-6 else math.copysign(1e-6, r_total)
    
    return tau_hold/safe_r_total


def branch_imbalance_at_theta(branch_pulls: dict[str, float]) -> float:
    pull_values = list(branch_pulls.values())
    if len(pull_values) <= 1:
        return 0.0
    return float(max(pull_values) - min(pull_values))



def evaluate_candidate_over_sweep_straight_finger(candidate: CandidateSpec,
    model: ModelParams,
    sweep: SweepSpec,) -> CandidateSweepOutput:


    tendon = make_tendon_input(candidate, model)
    theta_sweep = np.asarray(sweep.theta_sweep, dtype=float)
    theta_neutral = model.joint_rest

    tip_traj = []
    tau_req = []
    tension_req = []
    r_total = []
    branch_pull = {
        branch.name: []
        for branch in tendon.branches
    }
    branch_imbalance = []

    for theta in theta_sweep:

        tip = straight_finger_model.fingertip_position(theta, model.geom)
        tip_traj.append(tip)

        tau_holding_req = straight_finger_model.required_holding_torque(theta, theta_neutral, model.stiffness)
        tau_req.append(tau_holding_req)

        r_theta = total_moment_arm(tendon, theta)
        r_total.append(r_theta)

        tension = required_tension_total(tendon, theta, theta_neutral, model.stiffness)
        tension_req.append(tension)

        branch_pulls_theta = branch_pull_at_theta(tendon, theta, theta_neutral)
        for name, pull in branch_pulls_theta.items():
            branch_pull[name].append(pull)

        branch_imbalance.append(branch_imbalance_at_theta(branch_pulls_theta))

    return CandidateSweepOutput(
        abstraction_name="straight_finger",
        model_case_name=model.name,
        size_name=model.size_name,
        stiffness_name=model.stiffness_name,
        candidate_family=candidate.geometry.family,
        candidate_name=candidate.name,
        sweep_name=sweep.name,
        theta_sweep=np.asarray(theta_sweep, dtype=float),
        tau_req=np.asarray(tau_req, dtype=float),
        tip_traj=np.asarray(tip_traj, dtype=float),
        tension_req=np.asarray(tension_req, dtype=float),
        r_total=np.asarray(r_total, dtype=float),
        branch_pull={k: np.asarray(v) for k, v in branch_pull.items()},
        branch_imbalance=np.asarray(branch_imbalance),
    )


def vector_norm_rows(values: np.ndarray) -> np.ndarray:
    return np.linalg.norm(values)

def branch_peak_pull(branch_pull: dict[str, np.ndarray]) -> float:
    return max(float(np.max(np.abs(values))) for values in branch_pull.values())

def summarize_candidate_output_straight(
        output: CandidateSweepOutput,
        reject_limits: RejectLimits,
        score_weights: ScoreWeights,
) -> CandidateResult:
    
    peak_tension = float(np.max(output.tension_req))
    mean_tension = float(np.mean(output.tension_req))
    peak_pull = float(branch_peak_pull(output.branch_pull))
    peak_branch_imbalance = float(np.max(output.branch_imbalance))
    r_total_norm = vector_norm_rows(output.r_total)

    reject_reasons: list[str] = []

    if peak_tension > reject_limits.max_tension:
        reject_reasons.append("peak_tension")

    if peak_pull > reject_limits.max_pull:
        reject_reasons.append("peak_pull")

    if float(np.min(r_total_norm)) < reject_limits.min_moment_arm_norm:
        reject_reasons.append("moment_arm_too_small")


    rejected = len(reject_reasons) > 0

    smoothness_penalty = (np.mean(vector_norm_rows(np.diff(output.r_total, axis=0)))) if len(output.r_total) > 1 else 0.0


    score = None
    if not rejected:
        score = (
            score_weights.w_tension * (peak_tension / max(reject_limits.max_tension, 1e-9))
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
    score=score,
    rejected=rejected,
    reject_reasons=reject_reasons,
    )



def raw_rows_from_output_straight(output: CandidateSweepOutput) -> list[dict[str, float | str | int]]:
    rows = []
    branch_names = list(output.branch_pull.keys())

    for idx, theta in enumerate(output.theta_sweep):
        row = {
            "abstraction_name": output.abstraction_name,
            "model_case_name": output.model_case_name,
            "size_name": output.size_name,
            "stiffness_name": output.stiffness_name,
            "candidate_family": output.candidate_family,
            "candidate_name": output.candidate_name,
            "sweep_name": output.sweep_name,
            "posture_idx": idx,
            "q_mcp": float(theta),
            "tip_x": float(output.tip_traj[idx, 0]),
            "tip_y": float(output.tip_traj[idx, 1]),
            "T_req": float(output.tension_req[idx]),
            "tau_req_mcp": float(output.tau_req[idx]),
            "r_total_mcp_mm": float(output.r_total[idx]),
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
        "score": result.score,
        "rejected": result.rejected,
        "reject_reasons": "|".join(result.reject_reasons),
    }


