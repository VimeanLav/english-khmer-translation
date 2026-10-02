"""Project-wide constants: paths, languages, seeds and the approaches compared.

Every script imports its settings from here, so all approaches share the same
data split, test subset, seed and output locations.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# --------------------------------------------------------------------------- #
# Experiment
# --------------------------------------------------------------------------- #
# Which training data to use, chosen with the EXPERIMENT environment variable:
#   "base"      - Experiment 1: SeyhaLite only (the default)
#   "augmented" - Experiment 2: SeyhaLite + ALT (professional news translations)
# Each experiment keeps its own processed data, checkpoints, models and results,
# so experiment 1's files are never overwritten by experiment 2.
EXPERIMENTS = ("base", "augmented")
EXPERIMENT = os.environ.get("EXPERIMENT", "base")
if EXPERIMENT not in EXPERIMENTS:
    raise ValueError(f"EXPERIMENT must be one of {EXPERIMENTS}, got {EXPERIMENT!r}.")
_EXPERIMENT_SUBDIR = "" if EXPERIMENT == "base" else EXPERIMENT

# --------------------------------------------------------------------------- #
# Paths (all relative to the project root, so the project runs anywhere)
# --------------------------------------------------------------------------- #
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
BASE_TOKENIZED_DIR = PROCESSED_DIR / "nllb_eng_khm"
TOKENIZED_DIR = BASE_TOKENIZED_DIR if EXPERIMENT == "base" else PROCESSED_DIR / f"nllb_eng_khm_{EXPERIMENT}"
ALT_DIR = PROCESSED_DIR / "alt"
CHECKPOINTS_DIR = PROJECT_ROOT / "checkpoints" / _EXPERIMENT_SUBDIR
MODELS_DIR = PROJECT_ROOT / "models" / _EXPERIMENT_SUBDIR
BASE_RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_DIR = BASE_RESULTS_DIR / _EXPERIMENT_SUBDIR
FIGURES_DIR = RESULTS_DIR / "figures"
LOGS_DIR = RESULTS_DIR / "logs"
PREDICTIONS_DIR = RESULTS_DIR / "predictions"
TUNING_DIR = RESULTS_DIR / "tuning"
ERROR_ANALYSIS_DIR = RESULTS_DIR / "error_analysis"

# --------------------------------------------------------------------------- #
# Task
# --------------------------------------------------------------------------- #
MODEL_NAME = "facebook/nllb-200-distilled-600M"
SRC_LANG = "eng_Latn"
# FLORES-200 code: ISO 639-3 "khm" + ISO 15924 script "Khmr". The tokenizer maps
# unknown codes such as "khm_Khm" to <unk> without raising an error.
TGT_LANG = "khm_Khmr"
MAX_LENGTH = 128

DATASET_NAME = "SeyhaLite/Translate-English-Khmer-All"
SRC_COLUMN = "eng"
TGT_COLUMN = "kh"

# Asian Language Treebank: professionally translated news, standard written Khmer.
# Experiment 2 adds its training split; every experiment is tested on its test split.
ALT_DATASET = "mutiyama/alt"
ALT_CONFIG = "alt-parallel"
# ALT is small (18k pairs vs 259k), so its training pairs are repeated this many
# times in experiment 2's training data to give standard Khmer more weight.
ALT_UPSAMPLE = 3

# Test sets: "seyhalite" (in-domain, the first TEST_EVAL_SIZE test pairs) and
# "alt" (out-of-domain news, all of ALT's test split).
TEST_SETS = ("seyhalite", "alt")

# --------------------------------------------------------------------------- #
# Reproducibility and evaluation protocol
# --------------------------------------------------------------------------- #
SEED = 42
# Label id ignored by the cross-entropy loss.
LABEL_PAD_ID = -100
# Every approach is scored on the same first TEST_EVAL_SIZE sentences of the
# (already shuffled) test split, with the same decoding settings.
TEST_EVAL_SIZE = 5000
EVAL_NUM_BEAMS = 4
# Validation sentences decoded at each evaluation during training (greedy).
VAL_EVAL_SIZE = 1000


def _test_suffix(test_set: str) -> str:
    """File-name suffix for a test set ("" for the original in-domain test set)."""
    if test_set not in TEST_SETS:
        raise ValueError(f"test_set must be one of {TEST_SETS}, got {test_set!r}.")
    return "" if test_set == "seyhalite" else f"_{test_set}"


@dataclass(frozen=True)
class Approach:
    """One row of the comparison table."""

    key: str
    label: str
    model_path: str
    trained: bool

    def results_file(self, test_set: str = "seyhalite") -> Path:
        """Test metrics JSON, e.g. ``frozen_results.json`` or ``frozen_alt_results.json``."""
        return RESULTS_DIR / f"{self.key}{_test_suffix(test_set)}_results.json"

    def predictions_file(self, test_set: str = "seyhalite") -> Path:
        """Every test translation, e.g. ``predictions/frozen.jsonl`` or ``frozen_alt.jsonl``."""
        return PREDICTIONS_DIR / f"{self.key}{_test_suffix(test_set)}.jsonl"

    @property
    def results_path(self) -> Path:
        return self.results_file()

    @property
    def predictions_path(self) -> Path:
        return self.predictions_file()

    @property
    def summary_path(self) -> Path:
        return RESULTS_DIR / f"{self.key}_train_summary.json"

    @property
    def history_path(self) -> Path:
        return LOGS_DIR / f"{self.key}_history.json"


APPROACHES: dict[str, Approach] = {
    a.key: a
    for a in (
        # Reference only: the rubric requires every compared approach to be trained.
        Approach("baseline", "Zero-shot NLLB-600M (reference)", MODEL_NAME, trained=False),
        Approach("scratch", "A: Transformer from scratch", str(MODELS_DIR / "scratch"), trained=True),
        Approach("frozen", "B: NLLB frozen backbone", str(MODELS_DIR / "nllb_frozen"), trained=True),
        Approach("full", "C: NLLB full fine-tuning", str(MODELS_DIR / "nllb_full"), trained=True),
    )
}
