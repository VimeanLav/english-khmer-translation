"""Compare experiment 1 (SeyhaLite) with experiment 2 (SeyhaLite + ALT).

Reads each experiment's test results on both test sets and writes:

* ``results/experiments_comparison.md``: chrF++ and BLEU per approach, before and
  after adding ALT, on the in-domain and the out-of-domain (ALT news) test sets.
* ``results/figures/experiments_comparison.png``: the same as a grouped bar chart.

Run from the project root (after evaluating both experiments):

    python -m src.compare_experiments
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

from src.config import APPROACHES, BASE_RESULTS_DIR, TEST_SETS
from src.utils.plotting import APPROACH_COLORS, TEXT, setup_style
from src.utils.reporting import load_json

EXPERIMENT_DIRS = {"Exp. 1: SeyhaLite": BASE_RESULTS_DIR, "Exp. 2: + ALT": BASE_RESULTS_DIR / "augmented"}
SHORT_LABELS = {"baseline": "Zero-shot\nNLLB", "scratch": "A: from\nscratch", "frozen": "B: frozen\nbackbone",
                "full": "C: full\nfine-tuning"}
TEST_SET_TITLES = {"seyhalite": "In-domain test (SeyhaLite, 5,000)", "alt": "Out-of-domain test (ALT news, 1,018)"}


def load_scores() -> dict[tuple[str, str, str], dict]:
    """Map (experiment, test set, approach) to its results JSON, for every file that exists."""
    scores = {}
    for experiment, folder in EXPERIMENT_DIRS.items():
        for test_set in TEST_SETS:
            suffix = "" if test_set == "seyhalite" else f"_{test_set}"
            for key in APPROACHES:
                path = folder / f"{key}{suffix}_results.json"
                if path.is_file():
                    scores[(experiment, test_set, key)] = load_json(path)
    return scores


def fmt(value: float | None) -> str:
    return "–" if value is None else f"{value:.2f}"


def fmt_delta(new: float | None, old: float | None) -> str:
    return "–" if new is None or old is None else f"{new - old:+.2f}"


def write_table(scores: dict) -> None:
    """Markdown table: chrF++ and BLEU per approach, experiment and test set."""
    exp1, exp2 = EXPERIMENT_DIRS
    lines = ["# Experiment 1 vs. experiment 2\n"]
    for test_set in TEST_SETS:
        lines += [
            f"\n## {TEST_SET_TITLES[test_set]}\n",
            "| Approach | chrF++ Exp. 1 | chrF++ Exp. 2 | Δ chrF++ | BLEU Exp. 1 | BLEU Exp. 2 | Δ BLEU |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
        for key, approach in APPROACHES.items():
            old = scores.get((exp1, test_set, key), {})
            new = scores.get((exp2, test_set, key), {})
            if not old and not new:
                continue
            lines.append(
                f"| {approach.label} | {fmt(old.get('chrf++'))} | {fmt(new.get('chrf++'))} "
                f"| {fmt_delta(new.get('chrf++'), old.get('chrf++'))} | {fmt(old.get('bleu'))} "
                f"| {fmt(new.get('bleu'))} | {fmt_delta(new.get('bleu'), old.get('bleu'))} |"
            )
    lines.append(
        "\n*Experiment 1 trains on SeyhaLite only; experiment 2 adds ALT (professional news "
        "translations, repeated 3×) with the same hyperparameters and step budgets. The zero-shot "
        "reference is not trained, so it is identical in both experiments.*\n"
    )
    path = BASE_RESULTS_DIR / "experiments_comparison.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"Saved {path}")


def plot(scores: dict) -> None:
    """Grouped bars of chrF++: one panel per test set, experiment 1 (light) vs 2 (solid)."""
    setup_style()
    exp1, exp2 = EXPERIMENT_DIRS
    keys = [k for k in APPROACHES if any((e, t, k) in scores for e in EXPERIMENT_DIRS for t in TEST_SETS)]
    fig, axes = plt.subplots(1, len(TEST_SETS), figsize=(11, 4.2), layout="constrained")
    width = 0.38
    for ax, test_set in zip(axes, TEST_SETS):
        x = np.arange(len(keys))
        for offset, experiment, alpha, hatch in ((-width / 2, exp1, 0.45, "//"), (width / 2, exp2, 1.0, None)):
            values = [scores.get((experiment, test_set, k), {}).get("chrf++", np.nan) for k in keys]
            bars = ax.bar(x + offset, values, width * 0.92, alpha=alpha, hatch=hatch,
                          color=[APPROACH_COLORS[k] for k in keys], edgecolor="#fcfcfb")
            ax.bar_label(bars, labels=["" if np.isnan(v) else f"{v:.1f}" for v in values],
                         padding=2, fontsize=8, color=TEXT)
        ax.set_xticks(x, [SHORT_LABELS[k] for k in keys], fontsize=8.5)
        ax.set_ylim(0, 108)
        ax.set_title(TEST_SET_TITLES[test_set], fontsize=11)
    axes[0].set_ylabel("Test chrF++")
    fig.legend(handles=[Patch(facecolor="#8a8985", alpha=0.45, hatch="//", label=exp1),
                        Patch(facecolor="#8a8985", label=exp2)],
               loc="outside lower center", ncols=2, fontsize=9)
    fig.suptitle("Effect of adding ALT training data", color=TEXT, fontweight="bold")
    path = BASE_RESULTS_DIR / "figures" / "experiments_comparison.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def main() -> None:
    """Build the cross-experiment table and figure."""
    scores = load_scores()
    if not scores:
        raise SystemExit("No results found for either experiment.")
    write_table(scores)
    plot(scores)


if __name__ == "__main__":
    main()
