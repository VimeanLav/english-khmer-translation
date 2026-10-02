"""Translate your own English sentences with one or more trained approaches.

Useful for a live demo. It uses the same models and the same decoding (beam
search) as the test evaluation in ``src.evaluate``.

Run from the project root:

    python -m src.translate "I want to eat papaya salad."
    python -m src.translate --approach frozen,scratch,baseline "Where is the market?"
    python -m src.translate --approach frozen      # interactive: type sentences, empty line quits

Approaches: ``scratch`` (A), ``frozen`` (B), ``full`` (C) and ``baseline``
(zero-shot NLLB). A trained model must be present under ``models/``.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable
from pathlib import Path

import torch

from src.config import APPROACHES, EVAL_NUM_BEAMS
from src.evaluate import load_nllb, resolve_model_path, translate_nllb
from src.model_scratch import ScratchTranslator


def load_translator(approach_key: str, num_beams: int) -> Callable[[list[str]], list[str]]:
    """Load one approach's model and return a function that translates a list of sentences.

    Args:
        approach_key: ``scratch``, ``frozen``, ``full`` or ``baseline``.
        num_beams: Beam size for decoding.

    Returns:
        A function mapping English sentences to Khmer translations.

    Raises:
        SystemExit: If a trained model has not been saved or downloaded yet.
    """
    approach = APPROACHES[approach_key]
    model_path = resolve_model_path(approach.model_path)
    if approach.trained and not Path(model_path).is_dir():
        raise SystemExit(
            f"No model for '{approach_key}' at {model_path}. Train it first, or download it "
            "into models/ (see the README section \"Model weights\")."
        )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if ScratchTranslator.is_scratch_dir(model_path):
        translator = ScratchTranslator.load(Path(model_path), device)
        return lambda texts: translator.translate(texts, num_beams=num_beams)
    model, tokenizer = load_nllb(model_path, device)
    return lambda texts: translate_nllb(texts, model, tokenizer, num_beams=num_beams)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Translate English sentences to Khmer.")
    parser.add_argument(
        "--approach", default="frozen",
        help=f"Comma-separated approaches to compare, from {', '.join(APPROACHES)} "
        "(default: frozen, the best model). Example: --approach frozen,scratch",
    )
    parser.add_argument("--num-beams", type=int, default=EVAL_NUM_BEAMS)
    parser.add_argument("sentences", nargs="*", help="English sentences; omit for interactive mode.")
    return parser.parse_args()


def main() -> None:
    """Translate sentences given on the command line, or typed interactively."""
    # Khmer output must not depend on the Windows console code page.
    sys.stdout.reconfigure(encoding="utf-8")
    args = parse_args()
    keys = [k.strip() for k in args.approach.split(",") if k.strip()]
    unknown = [k for k in keys if k not in APPROACHES]
    if unknown:
        raise SystemExit(f"Unknown approach {unknown}; choose from {list(APPROACHES)}.")
    translators = {key: load_translator(key, args.num_beams) for key in keys}

    def show(sentences: list[str]) -> None:
        outputs = {key: translate(sentences) for key, translate in translators.items()}
        for i, sentence in enumerate(sentences):
            print(f"\nEN: {sentence}")
            for key in translators:
                print(f"  {APPROACHES[key].label:<34} {outputs[key][i]}")

    if args.sentences:
        show(args.sentences)
        return
    print("Type an English sentence and press Enter (empty line to quit).")
    while sentence := input("> ").strip():
        show([sentence])


if __name__ == "__main__":
    main()
