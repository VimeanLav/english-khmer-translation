"""Helpers for writing results: JSON files, hardware info and training histories.

Every approach writes the same two files, so plotting and comparison code can
treat them identically:

* ``results/logs/<approach>_history.json``: training loss and validation
  metrics over time (for learning curves).
* ``results/<approach>_train_summary.json``: parameters, hyperparameters,
  training time, seconds per step and hardware.
"""

from __future__ import annotations

import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import torch


def save_json(data: Any, path: Path) -> None:
    """Write JSON as UTF-8 (the Windows default code page cannot encode Khmer)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(path: Path) -> Any:
    """Read a UTF-8 JSON file."""
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def utc_timestamp() -> str:
    """Current UTC time in ISO format, for provenance in result files."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def hardware_info() -> dict[str, Any]:
    """Describe the software and GPU used, for the results table."""
    info: dict[str, Any] = {
        "python": platform.python_version(),
        "torch": torch.__version__,
        "cuda": torch.version.cuda,
        "gpu": None,
        "gpu_memory_gb": None,
    }
    if torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)
        info["gpu"] = props.name
        info["gpu_memory_gb"] = round(props.total_memory / 2**30, 1)
    return info


def count_parameters(model: torch.nn.Module) -> tuple[int, int]:
    """Return ``(trainable, total)`` parameter counts."""
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return trainable, total


def peak_vram_gb() -> float | None:
    """Peak GPU memory allocated by tensors in this process, in GB."""
    if not torch.cuda.is_available():
        return None
    return round(torch.cuda.max_memory_allocated() / 2**30, 2)


def make_history(
    approach: str,
    examples_per_step: int,
    train: list[dict[str, float]],
    evals: list[dict[str, float]],
) -> dict[str, Any]:
    """Build a history record in the common format used by ``src.plots``.

    Args:
        approach: Approach key (e.g. ``"frozen"``).
        examples_per_step: Sentence pairs per optimizer step (effective batch size),
            used to put approaches with different batch sizes on one x-axis.
        train: ``[{"step", "epoch", "loss", "lr"}, ...]`` training-loss points.
        evals: ``[{"step", "epoch", "loss", "chrf++", "chrf", "bleu"}, ...]``
            validation points.
    """
    return {
        "approach": approach,
        "examples_per_step": examples_per_step,
        "train": train,
        "eval": evals,
    }


def history_from_trainer_logs(
    approach: str, log_history: list[dict[str, Any]], examples_per_step: int
) -> dict[str, Any]:
    """Convert ``trainer.state.log_history`` into the common history format."""
    train, evals = [], []
    for entry in log_history:
        if "loss" in entry and "eval_loss" not in entry:
            train.append({
                "step": entry["step"],
                "epoch": entry.get("epoch"),
                "loss": entry["loss"],
                "lr": entry.get("learning_rate"),
            })
        elif "eval_loss" in entry:
            evals.append({
                "step": entry["step"],
                "epoch": entry.get("epoch"),
                "loss": entry["eval_loss"],
                "chrf++": entry.get("eval_chrf++"),
                "chrf": entry.get("eval_chrf"),
                "bleu": entry.get("eval_bleu"),
            })
    return make_history(approach, examples_per_step, train, evals)
