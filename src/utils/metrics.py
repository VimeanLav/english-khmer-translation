"""Translation metrics: chrF++ (primary) and BLEU.

chrF++ is the primary metric because Khmer is written without spaces between
words, so word-level metrics depend heavily on how the text is segmented.
Character n-grams avoid that problem.

BLEU is reported as spBLEU (sacrebleu's ``flores200`` SentencePiece tokenizer,
as in the NLLB paper). If that tokenizer can't be loaded (for example, when
offline), BLEU falls back to character-level tokenization. The tokenizer that
was used is always reported next to the score.

``sacrebleu`` is called directly rather than through ``evaluate.load(...)``.
This means no metric scripts are downloaded, and the ``evaluate`` package can't
clash with ``src/evaluate.py``.
"""

from __future__ import annotations

import warnings
from collections.abc import Callable, Sequence
from functools import lru_cache

import numpy as np
from sacrebleu.metrics import BLEU, CHRF
from transformers import EvalPrediction, PreTrainedTokenizerBase

DEFAULT_BLEU_TOKENIZE = "flores200"
FALLBACK_BLEU_TOKENIZE = "char"

# word_order=2 turns chrF into chrF++ (adds word 1- and 2-grams).
_CHRF_PP = CHRF(word_order=2)
# Plain chrF ignores whitespace entirely, so it is insensitive to how Khmer
# words are spaced. Spacing is inconsistent in this corpus (73% of references
# contain spaces, 27% none), and systems differ in where they put spaces.
_CHRF = CHRF(word_order=0)


@lru_cache(maxsize=None)
def _get_bleu(tokenize: str) -> tuple[BLEU, str]:
    """Build a BLEU scorer, falling back to character tokenization on failure."""
    try:
        return BLEU(tokenize=tokenize), tokenize
    except Exception as exc:  # e.g. SentencePiece model download failed
        warnings.warn(
            f"BLEU tokenizer '{tokenize}' unavailable ({exc}); "
            f"falling back to '{FALLBACK_BLEU_TOKENIZE}'."
        )
        return BLEU(tokenize=FALLBACK_BLEU_TOKENIZE), FALLBACK_BLEU_TOKENIZE


def compute_chrf_pp(hypotheses: Sequence[str], references: Sequence[str]) -> float:
    """Compute corpus-level chrF++.

    Args:
        hypotheses: Model translations.
        references: Reference translations (one per hypothesis).

    Returns:
        chrF++ score in the range 0-100.
    """
    return _CHRF_PP.corpus_score(list(hypotheses), [list(references)]).score


def compute_chrf(hypotheses: Sequence[str], references: Sequence[str]) -> float:
    """Compute corpus-level character-only chrF (whitespace-insensitive).

    Args:
        hypotheses: Model translations.
        references: Reference translations (one per hypothesis).

    Returns:
        chrF score in the range 0-100.
    """
    return _CHRF.corpus_score(list(hypotheses), [list(references)]).score


def sentence_chrf_pp(hypothesis: str, reference: str) -> float:
    """Compute sentence-level chrF++ (used for error analysis)."""
    return _CHRF_PP.sentence_score(hypothesis, [reference]).score


def compute_bleu(
    hypotheses: Sequence[str],
    references: Sequence[str],
    tokenize: str = DEFAULT_BLEU_TOKENIZE,
) -> tuple[float, str]:
    """Compute corpus-level BLEU.

    Args:
        hypotheses: Model translations.
        references: Reference translations (one per hypothesis).
        tokenize: sacrebleu tokenizer name.

    Returns:
        A ``(score, tokenizer_used)`` tuple, with the score in the range 0-100.
    """
    bleu, used = _get_bleu(tokenize)
    return bleu.corpus_score(list(hypotheses), [list(references)]).score, used


def compute_translation_metrics(
    hypotheses: Sequence[str], references: Sequence[str]
) -> dict[str, float | str]:
    """Compute chrF++ and BLEU for a set of translations.

    Args:
        hypotheses: Model translations.
        references: Reference translations (one per hypothesis).

    Returns:
        ``{"chrf++": float, "chrf": float, "bleu": float, "bleu_tokenizer": str}``.

    Raises:
        ValueError: If the inputs have different lengths.
    """
    if len(hypotheses) != len(references):
        raise ValueError(
            f"Got {len(hypotheses)} hypotheses but {len(references)} references."
        )
    bleu, bleu_tokenizer = compute_bleu(hypotheses, references)
    return {
        "chrf++": round(compute_chrf_pp(hypotheses, references), 4),
        "chrf": round(compute_chrf(hypotheses, references), 4),
        "bleu": round(bleu, 4),
        "bleu_tokenizer": bleu_tokenizer,
    }


def build_compute_metrics(
    tokenizer: PreTrainedTokenizerBase,
) -> Callable[[EvalPrediction], dict[str, float]]:
    """Create a ``compute_metrics`` function for ``Seq2SeqTrainer``.

    Requires ``predict_with_generate=True`` so predictions are token ids.

    Args:
        tokenizer: Tokenizer used to decode predictions and labels.

    Returns:
        A function that maps an ``EvalPrediction`` to ``{"chrf++", "chrf", "bleu"}``.
    """
    pad_id = tokenizer.pad_token_id

    def compute_metrics(eval_pred: EvalPrediction) -> dict[str, float]:
        predictions, labels = eval_pred.predictions, eval_pred.label_ids
        if isinstance(predictions, tuple):
            predictions = predictions[0]
        # The Trainer pads with -100 across batches; map it back to a real id.
        predictions = np.where(predictions != -100, predictions, pad_id)
        labels = np.where(labels != -100, labels, pad_id)

        hypotheses = [t.strip() for t in tokenizer.batch_decode(predictions, skip_special_tokens=True)]
        references = [t.strip() for t in tokenizer.batch_decode(labels, skip_special_tokens=True)]
        scores = compute_translation_metrics(hypotheses, references)
        # The Trainer logs only numeric values.
        return {k: v for k, v in scores.items() if isinstance(v, float)}

    return compute_metrics
