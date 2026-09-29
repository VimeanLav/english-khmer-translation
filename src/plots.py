"""Generate every comparison figure in ``results/figures/``.

Figures (each is skipped if its input files do not exist yet):

* ``learning_curves.png``: training vs. validation loss for every approach
  (to diagnose over- or underfitting).
* ``val_chrf_curves.png``: validation chrF++ vs. training examples seen,
  all approaches overlaid.
* ``test_metrics.png``: test chrF++, chrF and BLEU side by side.
* ``efficiency.png``: test chrF++ vs. trainable parameters.
* ``tuning_<approach>.png``: validation chrF++ over the tuning grid.
* ``error_categories.png``: share of test sentences per error category.
* ``chrf_by_length.png``: sentence chrF++ by English sentence length.

Run from the project root:

    python -m src.plots
"""

from __future__ import annotations

import csv

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

from src.config import APPROACHES, ERROR_ANALYSIS_DIR, TUNING_DIR
from src.utils.plotting import (
    APPROACH_COLORS,
    SEQUENTIAL,
    TEXT,
    TEXT_SECONDARY,
    save_figure,
    setup_style,
)
from src.utils.reporting import load_json

TRAINED = [k for k, a in APPROACHES.items() if a.trained]
# Compact axis labels (e.g. 50k, 1.5M) so long numbers never overlap.
THOUSANDS = FuncFormatter(
    lambda x, _: f"{x / 1e6:g}M" if abs(x) >= 1e6 else f"{x / 1e3:g}k" if abs(x) >= 1e3 else f"{x:g}"
)


def load_histories() -> dict[str, dict]:
    """Histories of the approaches that have been trained."""
    return {
        k: load_json(APPROACHES[k].history_path)
        for k in TRAINED if APPROACHES[k].history_path.is_file()
    }


def plot_learning_curves(histories: dict[str, dict]) -> None:
    """One panel per approach: training loss vs. validation loss."""
    fig, axes = plt.subplots(1, len(histories), figsize=(4.6 * len(histories), 3.8),
                             layout="constrained", squeeze=False)
    for ax, (key, h) in zip(axes[0], histories.items()):
        color, eps = APPROACH_COLORS[key], h["examples_per_step"]
        train_x = [p["step"] * eps for p in h["train"]]
        eval_x = [p["step"] * eps for p in h["eval"]]
        ax.plot(train_x, [p["loss"] for p in h["train"]], color=color, alpha=0.55,
                linewidth=1.5, label="Training loss")
        ax.plot(eval_x, [p["loss"] for p in h["eval"]], color=color, linestyle="--",
                marker="o", label="Validation loss")
        ax.set_title(APPROACHES[key].label, fontsize=11)
        ax.set_xlabel("Training sentence pairs seen")
        ax.xaxis.set_major_formatter(THOUSANDS)
        ax.legend(fontsize=9)
    axes[0][0].set_ylabel("Cross-entropy loss")
    fig.suptitle("Learning curves: training vs. validation loss", color=TEXT, fontweight="bold")
    save_figure(fig, "learning_curves")


def plot_val_chrf(histories: dict[str, dict]) -> None:
    """Validation chrF++ of every approach on one axis (log x: budgets differ a lot)."""
    fig, ax = plt.subplots(figsize=(8, 4.2), layout="constrained")
    for key, h in histories.items():
        xs = [p["step"] * h["examples_per_step"] for p in h["eval"]]
        ys = [p["chrf++"] for p in h["eval"]]
        ax.plot(xs, ys, color=APPROACH_COLORS[key], marker="o", label=APPROACHES[key].label)
        ax.annotate(f"{ys[-1]:.1f}", (xs[-1], ys[-1]), xytext=(6, 0), textcoords="offset points",
                    va="center", color=TEXT, fontsize=9)
    ax.set_xscale("log")
    ax.set_xlabel("Training sentence pairs seen (log scale)")
    ax.set_ylabel("Validation chrF++")
    ax.set_title("Validation chrF++ during training")
    ax.legend()
    save_figure(fig, "val_chrf_curves")


def plot_test_metrics(results: dict[str, dict]) -> None:
    """Grouped bars: chrF++, chrF and BLEU on the test set for every approach."""
    metrics = [("chrf++", "chrF++ (primary)"), ("chrf", "chrF"), ("bleu", "BLEU (spBLEU)")]
    keys = list(results)
    width = 0.8 / len(keys)
    x = np.arange(len(metrics))
    fig, ax = plt.subplots(figsize=(8.5, 4.2), layout="constrained")
    for i, key in enumerate(keys):
        values = [results[key][m] for m, _ in metrics]
        bars = ax.bar(x + (i - (len(keys) - 1) / 2) * width, values, width * 0.92,
                      color=APPROACH_COLORS[key], label=APPROACHES[key].label)
        ax.bar_label(bars, fmt="%.1f", padding=2, fontsize=8, color=TEXT)
    ax.set_xticks(x, [label for _, label in metrics])
    ax.set_ylabel("Score (0–100)")
    ax.set_title(f"Test-set scores ({next(iter(results.values()))['num_samples']:,} sentences)")
    # Legend below the axes so it never covers a bar or its value label.
    fig.legend(*ax.get_legend_handles_labels(), loc="outside lower center", ncols=2, fontsize=9)
    ax.set_ylim(0, max(max(r[m] for m, _ in metrics) for r in results.values()) * 1.12)
    save_figure(fig, "test_metrics")


def plot_efficiency(results: dict[str, dict]) -> None:
    """Test chrF++ against the number of trainable parameters."""
    points = []
    for key in TRAINED:
        path = APPROACHES[key].summary_path
        if key in results and path.is_file():
            points.append((key, load_json(path)["trainable_params"], results[key]["chrf++"]))
    if len(points) < 2:
        return
    fig, ax = plt.subplots(figsize=(7.5, 4.2), layout="constrained")
    label_box = {"facecolor": "#fcfcfb", "edgecolor": "none", "pad": 1.5}
    scores = [chrf for _, _, chrf in points]
    # Zoom the y-axis onto the trained approaches so close scores stay distinguishable;
    # the zero-shot score is far below, so it is stated in the title instead of plotted.
    spread = max(max(scores) - min(scores), 1.0)
    ax.set_ylim(min(scores) - 0.8 * spread, max(scores) + 0.8 * spread)
    # Alternate labels above/below the points (in x order) so they never overlap.
    for i, (key, params, chrf) in enumerate(sorted(points, key=lambda p: p[1])):
        ax.scatter(params, chrf, s=80, color=APPROACH_COLORS[key], zorder=3,
                   edgecolor="#fcfcfb", linewidth=2)
        above = i % 2 == 1
        ax.annotate(f"{APPROACHES[key].label}\n{params / 1e6:.1f}M params · chrF++ {chrf:.2f}",
                    (params, chrf), xytext=(0, 12 if above else -12), textcoords="offset points",
                    ha="center", va="bottom" if above else "top", fontsize=8.5, color=TEXT,
                    bbox=label_box, zorder=4)
    ax.set_xscale("log")
    ax.set_xlim(min(p for _, p, _ in points) / 3, max(p for _, p, _ in points) * 3)
    ax.xaxis.set_major_formatter(FuncFormatter(
        lambda x, _: f"{x / 1e9:g}B" if x >= 1e9 else f"{x / 1e6:g}M"))
    ax.set_xlabel("Trainable parameters (log scale)")
    ax.set_ylabel("Test chrF++")
    title = "Parameter efficiency"
    if "baseline" in results:
        title += f"\n(zero-shot NLLB reference: {results['baseline']['chrf++']:.1f} chrF++, off this scale)"
    ax.set_title(title, fontsize=11)
    save_figure(fig, "efficiency")


def plot_tuning() -> None:
    """Heatmap of validation chrF++ over learning rate x dropout, per tuned approach."""
    for key in TRAINED:
        path = TUNING_DIR / f"{key}_trials.csv"
        if not path.is_file():
            continue
        with path.open(encoding="utf-8", newline="") as f:
            trials = list(csv.DictReader(f))
        lrs = sorted({float(t["learning_rate"]) for t in trials})
        dropouts = sorted({float(t["dropout"]) for t in trials})
        grid = np.full((len(dropouts), len(lrs)), np.nan)
        for t in trials:  # Later trials with the same (lr, dropout) overwrite earlier ones.
            grid[dropouts.index(float(t["dropout"])), lrs.index(float(t["learning_rate"]))] = float(t["val_chrf++"])
        fig, ax = plt.subplots(figsize=(1.6 * len(lrs) + 2.2, 1.0 * len(dropouts) + 1.6),
                               layout="constrained")
        image = ax.imshow(grid, cmap=SEQUENTIAL, aspect="auto")
        ax.grid(False)
        ax.set_xticks(range(len(lrs)), [f"{lr:.0e}" for lr in lrs])
        ax.set_yticks(range(len(dropouts)), [f"{d:g}" for d in dropouts])
        ax.set_xlabel("Learning rate")
        ax.set_ylabel("Dropout")
        best = np.nanmax(grid)
        for (row, col), value in np.ndenumerate(grid):
            if not np.isnan(value):
                dark = value > np.nanmin(grid) + 0.55 * (best - np.nanmin(grid))
                ax.text(col, row, f"{value:.1f}" + (" ★" if value == best else ""), ha="center",
                        va="center", fontsize=9, color="#ffffff" if dark else TEXT)
        fig.colorbar(image, ax=ax, label="Validation chrF++")
        ax.set_title(f"Tuning: {APPROACHES[key].label}\n({trials[0]['budget']} per trial)", fontsize=11)
        save_figure(fig, f"tuning_{key}")


def plot_error_analysis() -> None:
    """Error-category shares and chrF++ by sentence length, from src.error_analysis."""
    path = ERROR_ANALYSIS_DIR / "summary.json"
    if not path.is_file():
        return
    summary = load_json(path)["approaches"]
    keys = list(summary)
    categories = [c for c in next(iter(summary.values()))["categories_pct"]
                  if any(summary[k]["categories_pct"][c] > 0 for k in keys)]

    fig, ax = plt.subplots(figsize=(8.5, 0.28 * len(categories) * len(keys) + 1.5),
                           layout="constrained")
    height = 0.8 / len(keys)
    y = np.arange(len(categories))
    for i, key in enumerate(keys):
        values = [summary[key]["categories_pct"][c] for c in categories]
        bars = ax.barh(y + (i - (len(keys) - 1) / 2) * height, values, height * 0.92,
                       color=APPROACH_COLORS[key], label=summary[key]["label"])
        # Label only non-zero bars to keep the chart readable.
        ax.bar_label(bars, labels=[f"{v:.1f}" if v > 0 else "" for v in values],
                     padding=2, fontsize=7.5, color=TEXT)
    ax.set_yticks(y, [c.replace("_", " ") for c in categories])
    ax.invert_yaxis()
    ax.grid(axis="x")
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("Share of test sentences (%)")
    ax.set_title("Translation outcome categories")
    ax.legend(fontsize=8.5, loc="lower right")
    save_figure(fig, "error_categories")

    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
    for key in keys:
        buckets = summary[key]["chrf_by_source_length"]
        labels = list(buckets)
        values = [buckets[b]["mean_sentence_chrf++"] for b in labels]
        ax.plot(labels, values, marker="o", color=APPROACH_COLORS[key], label=summary[key]["label"])
    ax.set_xlabel("English source length (words)")
    ax.set_ylabel("Mean sentence chrF++")
    ax.set_title("Quality by sentence length (test set)")
    ax.legend(fontsize=9)
    save_figure(fig, "chrf_by_length")


def main() -> None:
    """Draw every figure whose inputs exist."""
    setup_style()
    histories = load_histories()
    if histories:
        plot_learning_curves(histories)
        plot_val_chrf(histories)
    results = {k: load_json(a.results_path) for k, a in APPROACHES.items() if a.results_path.is_file()}
    if results:
        plot_test_metrics(results)
        plot_efficiency(results)
    plot_tuning()
    plot_error_analysis()


if __name__ == "__main__":
    main()
