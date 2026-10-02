"""Qualitative probe: translate a fixed set of everyday sentences with every model.

Automatic metrics on the in-domain test set cannot show how the models behave
on ordinary sentences that are unlike the training data. This script translates
a fixed list of such sentences with every approach available in the current
EXPERIMENT and writes a side-by-side table for manual judgement.

Outputs ``results/[experiment/]qualitative_probe.md`` (with an empty column for
a Khmer speaker's judgement) and ``qualitative_probe.json``.

Run from the project root:

    python -m src.probe
    $env:EXPERIMENT = "augmented"; python -m src.probe     # experiment 2 (PowerShell)
"""

from __future__ import annotations

from pathlib import Path

from src.config import APPROACHES, EVAL_NUM_BEAMS, EXPERIMENT, RESULTS_DIR
from src.evaluate import resolve_model_path
from src.translate import load_translator
from src.utils.reporting import save_json

PROBE_SENTENCES = [
    # From the qualitative evaluation report.
    "i want to hug you",
    "i want to kiss you",
    "i want to study english in my parents school",
    "i want you to believe in me, i know i can do it",
    "can you start the project? i want to see what you can do.",
    # Everyday sentences tested during development.
    "I love you.",
    "I love my mother.",
    "The weather is very hot today.",
    "Where is the nearest hospital?",
    "I am a student at Kirirom Institute of Technology.",
    "Can you help me find my phone?",
    "I have 3 brothers and 2 sisters.",
    "Machine learning is changing the world.",
    "Please call me when you arrive at the airport.",
]


def available_approaches() -> list[str]:
    """Approaches whose model exists in the current experiment (zero-shot is always available)."""
    return [
        key for key, approach in APPROACHES.items()
        if not approach.trained or Path(resolve_model_path(approach.model_path)).is_dir()
    ]


def main() -> None:
    """Translate the probe sentences with every available approach and save the table."""
    keys = available_approaches()
    outputs = {}
    for key in keys:
        print(f"Translating with {APPROACHES[key].label}...")
        outputs[key] = load_translator(key, EVAL_NUM_BEAMS)(PROBE_SENTENCES)

    lines = [
        f"# Qualitative probe ({EXPERIMENT} experiment)\n",
        "Everyday sentences unlike the training templates, translated by every model with "
        f"beam search ({EVAL_NUM_BEAMS} beams). Fill in the last column: ✅ correct, "
        "⚠️ understandable but wrong register or word, ❌ wrong or nonsense.\n",
    ]
    for i, sentence in enumerate(PROBE_SENTENCES):
        lines += [f"\n**{i + 1}. {sentence}**\n", "| Model | Khmer output | Judgement |", "|---|---|---|"]
        lines += [f"| {APPROACHES[k].label} | {outputs[k][i]} | |" for k in keys]

    md_path = RESULTS_DIR / "qualitative_probe.md"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    save_json(
        {"experiment": EXPERIMENT, "sentences": PROBE_SENTENCES,
         "translations": {k: outputs[k] for k in keys}},
        RESULTS_DIR / "qualitative_probe.json",
    )
    print(f"Saved {md_path}")


if __name__ == "__main__":
    main()
