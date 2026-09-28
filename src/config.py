"""Project-wide constants: paths, languages, seeds and the approaches compared.

Every script imports its settings from here, so all approaches share the same
data split, test subset, seed and output locations.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# --------------------------------------------------------------------------- #
# Paths (all relative to the project root, so the project runs anywhere)
# --------------------------------------------------------------------------- #
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
TOKENIZED_DIR = PROCESSED_DIR / "nllb_eng_khm"
CHECKPOINTS_DIR = PROJECT_ROOT / "checkpoints"
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"
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


@dataclass(frozen=True)
class Approach:
    """One row of the comparison table."""

    key: str
    label: str
    model_path: str
    trained: bool

    @property
    def results_path(self) -> Path:
        return RESULTS_DIR / f"{self.key}_results.json"

    @property
    def predictions_path(self) -> Path:
        return PREDICTIONS_DIR / f"{self.key}.jsonl"

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
