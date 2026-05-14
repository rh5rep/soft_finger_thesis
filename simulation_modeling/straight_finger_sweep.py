from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from simulation_modeling import straight_finger_model
from simulation_modeling.candidate_sweep_utils import (
    SharedRoutingGeometry,
    BranchGeometry,
    CandidateGeometry,
    CandidateSpec,
    RejectLimits,
    ScoreWeights,
    ExperimentRun,
    make_branch,
    make_candidate,
    make_candidate_name,
    validate_branch_geom,
    validate_shared_geom,
    validate_candidate_geom,
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
) -> dict[str, np.ndarray]:
    
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
) -> dict[str, float]:
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
        theta_sweep=np.asarray([[theta] for theta in theta_sweep]),
        tip_traj=np.asarray(tip_traj),  
        tau_req=np.asarray([[tau] for tau in tau_req]),  
        tension_req=np.asarray([[t] for t in tension_req]),  
        r_total=np.asarray([[r] for r in r_total]), 
        branch_pull={k: np.asarray(v) for k, v in branch_pull.items()},
        branch_imbalance=np.asarray(branch_imbalance),
    )
