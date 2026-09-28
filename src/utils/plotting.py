"""Shared matplotlib style so every figure in ``results/figures`` looks consistent.

Colors follow a colorblind-validated categorical palette: approaches A/B/C take
the first three slots (blue, orange, aqua), and the zero-shot reference is
neutral gray because it is a reference line, not a competing approach. Values
are also printed on the marks, so identity never depends on color alone.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # Render to files; no display needed (Colab, servers).
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

from src.config import FIGURES_DIR  # noqa: E402

SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e4e3df"
REFERENCE_GRAY = "#8a8985"

APPROACH_COLORS = {
    "baseline": REFERENCE_GRAY,
    "scratch": "#2a78d6",
    "frozen": "#eb6834",
    "full": "#1baf7a",
}

# Single-hue sequential ramp (light -> dark blue) for heatmaps.
SEQUENTIAL = LinearSegmentedColormap.from_list(
    "seq_blue", ["#cde2fb", "#86b6ef", "#3987e5", "#256abf", "#184f95", "#0d366b"]
)


def setup_style() -> None:
    """Apply the shared figure style."""
    plt.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "axes.edgecolor": GRID,
        "axes.labelcolor": TEXT_SECONDARY,
        "axes.titlecolor": TEXT,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "xtick.color": TEXT_SECONDARY,
        "ytick.color": TEXT_SECONDARY,
        "legend.frameon": False,
        "legend.labelcolor": TEXT,
        "lines.linewidth": 2,
        "lines.markersize": 5,
        "font.size": 10,
    })


def save_figure(fig: plt.Figure, name: str) -> Path:
    """Save ``fig`` as ``results/figures/<name>.png`` and close it."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURES_DIR / f"{name}.png"
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")
    return path
