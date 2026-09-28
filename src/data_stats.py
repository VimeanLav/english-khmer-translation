"""Describe the dataset: sizes, length distributions, text properties and overlap.

Writes ``results/data_stats.json`` and ``results/figures/length_distribution.png``.
The overlap numbers quantify how close the test set is to the training set,
which matters because this corpus contains many templated sentences.

Run from the project root (after ``python -m src.data``):

    python -m src.data_stats
"""

from __future__ import annotations

import re
import string

import numpy as np
from datasets import load_dataset

from src.config import DATASET_NAME, RAW_DIR, RESULTS_DIR, SRC_COLUMN, TGT_COLUMN
from src.data import load_tokenized_datasets
from src.utils.plotting import APPROACH_COLORS, TEXT, setup_style, save_figure
from src.utils.reporting import save_json

WORD_RE = re.compile(r"[a-z]+(?:'[a-z]+)?")
LATIN_RE = re.compile(r"[A-Za-z]")
ZWSP = chr(0x200B)  # Zero-width space.
# Arabic digits and Khmer digits (U+17E0 to U+17E9).
DIGIT_RE = re.compile(f"[0-9{chr(0x17E0)}-{chr(0x17E9)}]")


def normalise_english(text: str) -> str:
    """Lowercase, drop punctuation and collapse spaces, to find near-duplicates."""
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return " ".join(text.split())


def describe(values: list[int]) -> dict[str, float]:
    """Summary statistics of a length distribution."""
    arr = np.asarray(values)
    return {
        "mean": round(float(arr.mean()), 2),
        "median": float(np.median(arr)),
        "p95": float(np.percentile(arr, 95)),
        "max": int(arr.max()),
    }


def main() -> None:
    """Compute dataset statistics and the length-distribution figure."""
    raw_rows = len(load_dataset(DATASET_NAME, split="train", cache_dir=str(RAW_DIR)))
    splits = load_tokenized_datasets()
    stats: dict = {
        "dataset": DATASET_NAME,
        "raw_rows": raw_rows,
        "rows_after_cleaning": sum(len(s) for s in splits.values()),
        "splits": {},
    }
    stats["removed_by_cleaning"] = raw_rows - stats["rows_after_cleaning"]

    for name, split in splits.items():
        eng, kh = list(split[SRC_COLUMN]), list(split[TGT_COLUMN])
        stats["splits"][name] = {
            "examples": len(split),
            "english_words": describe([len(t.split()) for t in eng]),
            "khmer_characters": describe([len(t.replace(" ", "")) for t in kh]),
            "nllb_source_tokens": describe([len(ids) for ids in split["input_ids"]]),
            "nllb_target_tokens": describe([len(ids) for ids in split["labels"]]),
            "khmer_with_spaces_pct": round(100 * np.mean([" " in t for t in kh]), 2),
            "khmer_with_zero_width_space_pct": round(100 * np.mean([ZWSP in t for t in kh]), 2),
            "khmer_with_latin_letters_pct": round(100 * np.mean([bool(LATIN_RE.search(t)) for t in kh]), 2),
            "english_with_digits_pct": round(100 * np.mean([bool(DIGIT_RE.search(t)) for t in eng]), 2),
        }

    # ---- Train/test overlap (a known limitation of templated corpora) -------
    train, test = splits["train"], splits["test"]
    train_norm = {normalise_english(t) for t in train[SRC_COLUMN]}
    train_refs = set(train[TGT_COLUMN])
    train_vocab = {w for t in train[SRC_COLUMN] for w in WORD_RE.findall(t.lower())}
    test_src, test_ref = list(test[SRC_COLUMN]), list(test[TGT_COLUMN])
    test_words = [WORD_RE.findall(t.lower()) for t in test_src]
    stats["overlap"] = {
        "test_source_near_duplicate_of_train_pct": round(
            100 * np.mean([normalise_english(t) in train_norm for t in test_src]), 2),
        "test_reference_seen_in_train_pct": round(
            100 * np.mean([t in train_refs for t in test_ref]), 2),
        "test_sentences_with_unseen_english_word_pct": round(
            100 * np.mean([any(w not in train_vocab for w in ws) for ws in test_words]), 2),
        "english_train_vocabulary_size": len(train_vocab),
        "note": "Exact English duplicates were removed before splitting; these figures "
                "measure the remaining near-duplicates (case/punctuation) and shared "
                "Khmer references.",
    }
    save_json(stats, RESULTS_DIR / "data_stats.json")
    print(f"Saved {RESULTS_DIR / 'data_stats.json'}")

    # ---- Figure: token-length distributions (training split) ----------------
    setup_style()
    import matplotlib.pyplot as plt

    from matplotlib.ticker import StrMethodFormatter

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True, layout="constrained")
    panels = [
        ("English source (NLLB tokens)", [len(i) for i in train["input_ids"]]),
        ("Khmer target (NLLB tokens)", [len(i) for i in train["labels"]]),
    ]
    for ax, (title, lengths) in zip(axes, panels):
        bins = np.arange(0, max(lengths) + 2)
        ax.hist(lengths, bins=bins, color=APPROACH_COLORS["scratch"], edgecolor="#fcfcfb", linewidth=0.5)
        median = float(np.median(lengths))
        ax.axvline(median, color=TEXT, linewidth=1, linestyle="--")
        ax.annotate(f"median {median:.0f}", (median, ax.get_ylim()[1] * 0.92),
                    xytext=(4, 0), textcoords="offset points", color=TEXT, fontsize=9)
        ax.set_title(title)
        ax.set_xlabel("Tokens (incl. language tag and </s>)")
    axes[0].set_ylabel("Training sentence pairs")
    axes[0].yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    fig.suptitle(f"Sentence length distribution — training split ({len(train):,} pairs)",
                 color=TEXT, fontweight="bold")
    save_figure(fig, "length_distribution")


if __name__ == "__main__":
    main()
