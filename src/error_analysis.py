"""Error analysis of test-set translations for every evaluated approach.

Each test sentence is scored with sentence-level chrF++ and put in one bucket:

* ``exact_match``: identical to the reference.
* ``spacing_only``: identical once whitespace is removed. The content is
  correct and only the Khmer word spacing differs.
* ``partially_correct``: sentence chrF++ >= ``FAIL_THRESHOLD``.
* a failure category (sentence chrF++ < ``FAIL_THRESHOLD``), assigned by the
  first rule that matches:

  1. ``empty_output``: nothing was generated.
  2. ``wrong_script``: the output is mostly Latin letters (untranslated
     English), although the reference is Khmer.
  3. ``repetition_hallucination``: a chunk repeats 3+ times, or the output is
     much longer than the reference (> ``LONG_RATIO``). This is the typical
     symptom of attention drift in autoregressive decoders.
  4. ``omission``: the output is much shorter than the reference
     (< ``SHORT_RATIO``), i.e. content was dropped.
  5. ``number_mismatch``: digits in the source are missing or changed.
  6. ``unseen_source_word``: the source contains an English word that never
     occurs in the training split (out-of-vocabulary for this corpus).
  7. ``lexical_semantic``: everything else (wrong word choice or meaning).

Outputs (in ``results/error_analysis/``): ``summary.json`` with category shares
and chrF++ by sentence length; ``<approach>_examples.md`` with the worst
translations and examples per category, for manual inspection;
``hard_for_all.md`` with sentences every trained approach fails, which often
points to noisy references.

Run from the project root (after evaluating the approaches):

    python -m src.error_analysis                   # in-domain test set
    python -m src.error_analysis --test-set alt    # out-of-domain ALT news test set
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import numpy as np

from src.config import APPROACHES, ERROR_ANALYSIS_DIR, SRC_COLUMN, TEST_SETS
from src.data import load_tokenized_datasets
from src.utils.metrics import sentence_chrf_pp
from src.utils.reporting import save_json

FAIL_THRESHOLD = 40.0
LONG_RATIO = 1.8
SHORT_RATIO = 0.5
LENGTH_BUCKETS = [(1, 4), (5, 7), (8, 10), (11, 13), (14, 99)]
FAILURE_CATEGORIES = [
    "empty_output", "wrong_script", "repetition_hallucination", "omission",
    "number_mismatch", "unseen_source_word", "lexical_semantic",
]
ALL_CATEGORIES = ["exact_match", "spacing_only", "partially_correct", *FAILURE_CATEGORIES]

WORD_RE = re.compile(r"[a-z]+(?:'[a-z]+)?")
LATIN_RE = re.compile(r"[A-Za-z]")
# The Khmer Unicode block (U+1780 to U+17FF).
KHMER_RE = re.compile(f"[{chr(0x1780)}-{chr(0x17FF)}]")
ZWSP = chr(0x200B)  # Zero-width space.
REPEAT_RE = re.compile(r"(.{3,}?)\1{2,}")
KHMER_DIGITS = str.maketrans("០១២៣៤៥៦៧៨៩", "0123456789")


def strip_spaces(text: str) -> str:
    """Remove all whitespace, including zero-width spaces."""
    return re.sub(r"[\s" + ZWSP + "]+", "", text)


def latin_share(text: str) -> float:
    """Fraction of letters that are Latin (vs. Khmer)."""
    latin, khmer = len(LATIN_RE.findall(text)), len(KHMER_RE.findall(text))
    return latin / max(latin + khmer, 1)


def digits(text: str) -> list[str]:
    """Numbers in a text, with Khmer digits mapped to Arabic ones."""
    return re.findall(r"\d+", text.translate(KHMER_DIGITS))


def categorise(src: str, ref: str, hyp: str, chrf: float, train_vocab: set[str]) -> str:
    """Assign one category to a translation (see the module docstring)."""
    if hyp == ref:
        return "exact_match"
    if strip_spaces(hyp) == strip_spaces(ref):
        return "spacing_only"
    if chrf >= FAIL_THRESHOLD:
        return "partially_correct"
    if not hyp.strip():
        return "empty_output"
    if latin_share(hyp) > 0.5 and latin_share(ref) < 0.5:
        return "wrong_script"
    length_ratio = len(strip_spaces(hyp)) / max(len(strip_spaces(ref)), 1)
    if REPEAT_RE.search(strip_spaces(hyp)) or length_ratio > LONG_RATIO:
        return "repetition_hallucination"
    if length_ratio < SHORT_RATIO:
        return "omission"
    if sorted(digits(src)) != sorted(digits(hyp)):
        return "number_mismatch"
    if any(w not in train_vocab for w in WORD_RE.findall(src.lower())):
        return "unseen_source_word"
    return "lexical_semantic"


def length_bucket(src: str) -> str:
    """Label of the English-length bucket a source sentence falls in."""
    n = len(src.split())
    for low, high in LENGTH_BUCKETS:
        if low <= n <= high:
            return f"{low}-{high}" if high < 99 else f"{low}+"
    return f"{LENGTH_BUCKETS[-1][0]}+"


def load_predictions(path: Path) -> list[dict[str, str]]:
    """Read a predictions JSONL file written by ``src.evaluate``."""
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def format_example(row: dict) -> str:
    """Markdown bullet for one translation."""
    return (
        f"- **chrF++ {row['chrf']:.1f}** · `{row['category']}`\n"
        f"  - EN: {row['src']}\n  - REF: {row['ref']}\n  - HYP: {row['hyp'] or '∅'}\n"
    )


def analysis_dir(test_set: str) -> Path:
    """Output folder: ``error_analysis/`` for the in-domain test set, a subfolder otherwise."""
    return ERROR_ANALYSIS_DIR if test_set == "seyhalite" else ERROR_ANALYSIS_DIR / test_set


def analyse_approach(key: str, rows: list[dict], train_vocab: set[str], out_dir: Path) -> dict:
    """Score, categorise and summarise one approach; write its examples file to ``out_dir``."""
    for row in rows:
        row["chrf"] = sentence_chrf_pp(row["hyp"], row["ref"])
        row["category"] = categorise(row["src"], row["ref"], row["hyp"], row["chrf"], train_vocab)
        row["bucket"] = length_bucket(row["src"])

    counts = Counter(row["category"] for row in rows)
    by_bucket: dict[str, dict] = {}
    for low, high in LENGTH_BUCKETS:
        label = f"{low}-{high}" if high < 99 else f"{low}+"
        scores = [r["chrf"] for r in rows if r["bucket"] == label]
        by_bucket[label] = {
            "sentences": len(scores),
            "mean_sentence_chrf++": round(float(np.mean(scores)), 2) if scores else None,
        }

    lines = [f"# Error analysis: {APPROACHES[key].label}\n",
             f"Failure = sentence chrF++ < {FAIL_THRESHOLD:g}. Categories are defined in "
             "`src/error_analysis.py`.\n",
             "## 15 worst translations\n"]
    lines += [format_example(r) for r in sorted(rows, key=lambda r: r["chrf"])[:15]]
    for category in ["spacing_only", *FAILURE_CATEGORIES]:
        examples = [r for r in rows if r["category"] == category][:5]
        if examples:
            lines.append(f"\n## {category} ({counts[category]} sentences)\n")
            lines += [format_example(r) for r in examples]
    path = out_dir / f"{key}_examples.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved {path}")

    total = len(rows)
    return {
        "label": APPROACHES[key].label,
        "sentences": total,
        "failures": sum(counts[c] for c in FAILURE_CATEGORIES),
        "failure_rate_pct": round(100 * sum(counts[c] for c in FAILURE_CATEGORIES) / total, 2),
        "categories": {c: counts[c] for c in ALL_CATEGORIES},
        "categories_pct": {c: round(100 * counts[c] / total, 2) for c in ALL_CATEGORIES},
        "chrf_by_source_length": by_bucket,
    }


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Error analysis of test-set translations.")
    parser.add_argument(
        "--test-set", choices=TEST_SETS, default="seyhalite",
        help="Which test set's predictions to analyse.",
    )
    return parser.parse_args()


def main() -> None:
    """Analyse every approach that has a predictions file for the chosen test set."""
    test_set = parse_args().test_set
    out_dir = analysis_dir(test_set)
    out_dir.mkdir(parents=True, exist_ok=True)
    train = load_tokenized_datasets()["train"]
    train_vocab = {w for t in train[SRC_COLUMN] for w in WORD_RE.findall(t.lower())}

    all_rows: dict[str, list[dict]] = {}
    for key, approach in APPROACHES.items():
        if approach.predictions_file(test_set).is_file():
            all_rows[key] = load_predictions(approach.predictions_file(test_set))
    if not all_rows:
        raise SystemExit(
            f"No {test_set} predictions found. Run `python -m src.evaluate --test-set {test_set}` first."
        )
    sizes = {len(rows) for rows in all_rows.values()}
    if len(sizes) > 1:
        raise SystemExit(f"Approaches were evaluated on different test sizes {sizes}; re-run evaluation.")

    summary = {
        "test_set": test_set,
        "fail_threshold_chrf++": FAIL_THRESHOLD,
        "approaches": {
            key: analyse_approach(key, rows, train_vocab, out_dir) for key, rows in all_rows.items()
        },
    }

    # Sentences that every *trained* approach fails: often noisy references.
    trained = [k for k in all_rows if APPROACHES[k].trained]
    if trained:
        n = len(all_rows[trained[0]])
        hard = [
            i for i in range(n)
            if all(all_rows[k][i]["category"] in FAILURE_CATEGORIES for k in trained)
        ]
        summary["hard_for_all_trained"] = {"approaches": trained, "sentences": len(hard)}
        lines = [f"# Sentences failed by every trained approach ({len(hard)} of {n})\n",
                 "Manually check these for noisy or misaligned references.\n"]
        for i in hard[:30]:
            first = all_rows[trained[0]][i]
            lines.append(f"- EN: {first['src']}\n  - REF: {first['ref']}")
            for k in trained:
                lines.append(f"  - {APPROACHES[k].label}: {all_rows[k][i]['hyp'] or '∅'}")
        (out_dir / "hard_for_all.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    save_json(summary, out_dir / "summary.json")
    print(f"Saved {out_dir / 'summary.json'}")
    for key, s in summary["approaches"].items():
        print(f"{s['label']:<38} failures {s['failure_rate_pct']:>6.2f}%  "
              f"exact {s['categories_pct']['exact_match']:>6.2f}%  "
              f"spacing-only {s['categories_pct']['spacing_only']:>5.2f}%")


if __name__ == "__main__":
    main()
