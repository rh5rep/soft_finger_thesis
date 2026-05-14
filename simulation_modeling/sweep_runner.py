from __future__ import annotations

from datetime import datetime
from pathlib import Path
from collections.abc import Mapping, Sequence
import csv
import re


RESULTS_DIR = Path(__file__).resolve().parent / "results"
RESULTS_IMAGE_DIR = RESULTS_DIR / "candidate_run_images"


def _fieldnames_from_rows(rows: list[dict]) -> list[str]:
    fieldnames: list[str] = []
    seen: set[str] = set()

    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)

    return fieldnames


def _sweep_specs_for_model(
    model,
    sweep_specs,
):
    if isinstance(sweep_specs, Mapping):
        try:
            return sweep_specs[model.abstraction_name]
        except KeyError as exc:
            raise ValueError(
                f"Missing sweep specs for abstraction_name: {model.abstraction_name}"
            ) from exc

    if isinstance(sweep_specs, Sequence):
        return sweep_specs

    raise TypeError(
        "sweep_specs must be either a sequence of sweep specs or a mapping from "
        "abstraction_name to sweep-spec sequences"
    )


def evaluate_candidate_over_sweep(candidate, model, sweep):
    if model.abstraction_name == "straight_finger":
        from simulation_modeling import straight_finger_sweep

        return straight_finger_sweep.evaluate_candidate_over_sweep_straight_finger(
            candidate,
            model,
            sweep,
        )

    if model.abstraction_name == "joint_space":
        from simulation_modeling import candidate_sweep_utils as joint_space_sweep

        return joint_space_sweep.evaluate_candidate_over_sweep_joint_space(
            candidate,
            model,
            sweep,
        )

    raise ValueError(f"Unsupported abstraction_name: {model.abstraction_name}")


def summarize_candidate_output(output, reject_limits, score_weights):
    if output.abstraction_name == "straight_finger":
        from simulation_modeling import straight_finger_sweep

        return straight_finger_sweep.summarize_candidate_output_straight(
            output,
            reject_limits,
            score_weights,
        )

    if output.abstraction_name == "joint_space":
        from simulation_modeling import candidate_sweep_utils as joint_space_sweep

        return joint_space_sweep.summarize_candidate_output_joint_space(
            output,
            reject_limits,
            score_weights,
        )

    raise ValueError(f"Unsupported abstraction_name: {output.abstraction_name}")


def raw_rows_from_output(output):
    if output.abstraction_name == "straight_finger":
        from simulation_modeling import straight_finger_sweep

        return straight_finger_sweep.raw_rows_from_output_straight(output)

    if output.abstraction_name == "joint_space":
        from simulation_modeling import candidate_sweep_utils as joint_space_sweep

        return joint_space_sweep.raw_rows_from_output_joint_space(output)

    raise ValueError(f"Unsupported abstraction_name: {output.abstraction_name}")


def summary_row_from_result(result):
    if result.abstraction_name == "straight_finger":
        from simulation_modeling import straight_finger_sweep

        return straight_finger_sweep.summary_row_from_result(result)

    if result.abstraction_name == "joint_space":
        from simulation_modeling import candidate_sweep_utils as joint_space_sweep

        return joint_space_sweep.summary_row_from_result_joint_space(result)

    raise ValueError(f"Unsupported abstraction_name: {result.abstraction_name}")


def write_csv_rows(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    fieldnames = _fieldnames_from_rows(rows)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_csv_rows(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return

    if not path.exists():
        fieldnames = _fieldnames_from_rows(rows)
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        return

    with path.open("r", newline="") as handle:
        reader = csv.DictReader(handle)
        existing_rows = list(reader)

    combined_rows = existing_rows + rows
    fieldnames = _fieldnames_from_rows(combined_rows)

    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(combined_rows)


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
    outputs,
    results,
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


def sort_candidate_results(results):
    return sorted(
        results,
        key=lambda result: (
            result.rejected,
            float("inf") if result.score is None else result.score,
            result.peak_tension,
        ),
    )


def run_experiment(
    model_cases,
    candidates,
    sweep_specs,
    reject_limits,
    score_weights,
):
    from simulation_modeling.candidate_sweep_utils import ExperimentRun

    outputs = []
    results = []

    for model_case in model_cases:
        model_sweep_specs = _sweep_specs_for_model(model_case, sweep_specs)
        for candidate in candidates:
            for sweep in model_sweep_specs:
                output = evaluate_candidate_over_sweep(candidate, model_case, sweep)
                result = summarize_candidate_output(output, reject_limits, score_weights)
                outputs.append(output)
                results.append(result)

    return ExperimentRun(
        outputs=outputs,
        results=sort_candidate_results(results),
    )
