"""Grid search over learning rate x dropout (plus optional weight decay).

Each trial is a short training run of one approach, scored by chrF++ on the
validation subset. The test set is never touched, so choosing the best
configuration cannot leak test information. Each trial runs in its own
subprocess, so GPU memory is fully released between trials.

Results are appended to ``results/tuning/<approach>_trials.csv`` after every
trial. Rerunning the command skips finished trials, which makes tuning
resumable after a Colab disconnect. The best configuration is written to
``results/tuning/<approach>_best.json``, and the final training run can reuse it.

Run from the project root:

    python -m src.tune --approach scratch
    python -m src.tune --approach full
    python -m src.tune --approach full --learning-rates 1e-5 3e-5 --dropouts 0.1 --max-steps 100
"""

from __future__ import annotations

import argparse
import csv
import itertools
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from src.config import APPROACHES, PROJECT_ROOT, TUNING_DIR
from src.utils.reporting import load_json, save_json, utc_timestamp

TRAIN_MODULES = {"scratch": "src.train_scratch", "frozen": "src.train_frozen", "full": "src.train_finetune"}

# Default grids and per-trial budgets, sized to fit a free Colab session.
DEFAULT_GRIDS: dict[str, dict[str, Any]] = {
    # Scratch: 3 epochs over an 80k-pair subset (~2.5 min per trial on an RTX 4070 Laptop GPU).
    "scratch": {"learning_rates": [3e-4, 5e-4, 1e-3], "dropouts": [0.1, 0.3],
                "budget": ["--epochs", "3", "--max-train-samples", "80000"]},
    "frozen": {"learning_rates": [3e-5, 1e-4, 3e-4], "dropouts": [0.1, 0.3], "budget": ["--max-steps", "500"]},
    "full": {"learning_rates": [1e-5, 3e-5, 1e-4], "dropouts": [0.1, 0.3], "budget": ["--max-steps", "300"]},
}

CSV_FIELDS = [
    "approach", "learning_rate", "dropout", "weight_decay", "budget",
    "val_chrf++", "val_chrf", "val_bleu", "val_loss",
    "steps", "seconds_per_step", "train_step_seconds", "timestamp",
]


def trials_path(approach: str) -> Path:
    return TUNING_DIR / f"{approach}_trials.csv"


def best_path(approach: str) -> Path:
    return TUNING_DIR / f"{approach}_best.json"


def read_trials(approach: str) -> list[dict[str, str]]:
    """Load finished trials (empty if none)."""
    path = trials_path(approach)
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def append_trial(approach: str, row: dict[str, Any]) -> None:
    """Append one finished trial to the CSV, writing the header if needed."""
    path = trials_path(approach)
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.is_file()
    with path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(row)


def trial_key(lr: float, dropout: float, weight_decay: float, budget: str) -> tuple:
    """Identify a trial so finished ones can be skipped."""
    return (float(lr), float(dropout), float(weight_decay), budget)


def run_trial(
    approach: str, lr: float, dropout: float, weight_decay: float,
    budget: list[str], max_eval_samples: int,
) -> dict[str, Any]:
    """Run one training trial in a subprocess and return its summary."""
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp) / "summary.json"
        command = [
            sys.executable, "-m", TRAIN_MODULES[approach],
            "--learning-rate", str(lr),
            "--dropout", str(dropout),
            "--weight-decay", str(weight_decay),
            "--max-eval-samples", str(max_eval_samples),
            *budget,
            "--tuning-output", str(output),
        ]
        print("\n$ " + " ".join(command[1:]), flush=True)
        subprocess.run(command, check=True, cwd=PROJECT_ROOT)
        return load_json(output)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Hyperparameter grid search on the validation set.")
    parser.add_argument("--approach", choices=list(TRAIN_MODULES), required=True)
    parser.add_argument("--learning-rates", type=float, nargs="+", default=None)
    parser.add_argument("--dropouts", type=float, nargs="+", default=None)
    parser.add_argument("--weight-decays", type=float, nargs="+", default=[0.01])
    budget = parser.add_mutually_exclusive_group()
    budget.add_argument("--max-steps", type=int, default=None, help="Per-trial budget (NLLB approaches).")
    budget.add_argument("--epochs", type=int, default=None, help="Per-trial budget (scratch).")
    parser.add_argument("--max-eval-samples", type=int, default=500, help="Validation sentences per trial.")
    parser.add_argument(
        "--max-train-samples", type=int, default=None,
        help="Train each trial on a random subset of this many pairs.",
    )
    return parser.parse_args()


def main() -> None:
    """Run every missing trial in the grid and report the best configuration."""
    args = parse_args()
    grid = DEFAULT_GRIDS[args.approach]
    learning_rates = args.learning_rates or grid["learning_rates"]
    dropouts = args.dropouts or grid["dropouts"]
    if args.max_steps is not None:
        budget = ["--max-steps", str(args.max_steps)]
    elif args.epochs is not None:
        budget = ["--epochs", str(args.epochs)]
    else:
        budget = list(grid["budget"])
    if args.max_train_samples is not None:
        budget += ["--max-train-samples", str(args.max_train_samples)]
    budget_label = " ".join(budget)

    done = {
        trial_key(r["learning_rate"], r["dropout"], r["weight_decay"], r["budget"])
        for r in read_trials(args.approach)
    }
    for lr, dropout, wd in itertools.product(learning_rates, dropouts, args.weight_decays):
        if trial_key(lr, dropout, wd, budget_label) in done:
            print(f"Skipping finished trial lr={lr} dropout={dropout} weight_decay={wd}")
            continue
        summary = run_trial(args.approach, lr, dropout, wd, budget, args.max_eval_samples)
        val = summary["val_metrics"]
        append_trial(args.approach, {
            "approach": args.approach,
            "learning_rate": lr,
            "dropout": dropout,
            "weight_decay": wd,
            "budget": budget_label,
            "val_chrf++": val.get("chrf++"),
            "val_chrf": val.get("chrf"),
            "val_bleu": val.get("bleu"),
            "val_loss": val.get("loss"),
            "steps": summary["steps_completed"],
            "seconds_per_step": summary["seconds_per_step"],
            "train_step_seconds": summary["train_step_seconds"],
            "timestamp": utc_timestamp(),
        })

    trials = [r for r in read_trials(args.approach) if r["budget"] == budget_label]
    best = max(trials, key=lambda r: float(r["val_chrf++"]))
    save_json({
        "approach": args.approach,
        "label": APPROACHES[args.approach].label,
        "selection_metric": "validation chrF++",
        "budget": budget_label,
        "learning_rate": float(best["learning_rate"]),
        "dropout": float(best["dropout"]),
        "weight_decay": float(best["weight_decay"]),
        "val_chrf++": float(best["val_chrf++"]),
        "num_trials": len(trials),
    }, best_path(args.approach))

    print(f"\n{'lr':>10}{'dropout':>9}{'wd':>7}{'val chrF++':>12}{'val loss':>10}")
    for r in sorted(trials, key=lambda r: -float(r["val_chrf++"])):
        print(f"{float(r['learning_rate']):>10.0e}{float(r['dropout']):>9}{float(r['weight_decay']):>7}"
              f"{float(r['val_chrf++']):>12.2f}{float(r['val_loss']):>10.3f}")
    print(f"\nBest: lr={best['learning_rate']} dropout={best['dropout']} "
          f"weight_decay={best['weight_decay']} -> {best_path(args.approach)}")


if __name__ == "__main__":
    main()
