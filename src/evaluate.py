"""Evaluate any approach on the English -> Khmer test set.

Every approach is scored identically: the same first ``TEST_EVAL_SIZE``
sentences of the fixed test split, the same raw English input, beam search
with ``EVAL_NUM_BEAMS`` beams, and the same metric code. Only the tokenizer
differs (NLLB's own tokenizer vs. the scratch model's SentencePiece model),
because each model can only read its own vocabulary.

Run from the project root. Use ``-m`` so this file does not hide the
``evaluate`` package:

    python -m src.evaluate --approach baseline   # zero-shot NLLB (reference)
    python -m src.evaluate --approach scratch    # A
    python -m src.evaluate --approach frozen     # B
    python -m src.evaluate --approach full       # C
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import torch
from tqdm import tqdm
from transformers import AutoModelForSeq2SeqLM, PreTrainedModel, PreTrainedTokenizerBase

from src.config import (
    APPROACHES,
    EVAL_NUM_BEAMS,
    MAX_LENGTH,
    PROJECT_ROOT,
    SEED,
    SRC_COLUMN,
    SRC_LANG,
    TEST_EVAL_SIZE,
    TGT_COLUMN,
    TGT_LANG,
)
from src.data import get_tokenizer, load_tokenized_datasets
from src.model_scratch import ScratchTranslator
from src.utils.metrics import compute_translation_metrics
from src.utils.reporting import save_json, utc_timestamp
from src.utils.seed import set_seed


def resolve_model_path(model_path: str) -> str:
    """Resolve a local model directory relative to the project root.

    Args:
        model_path: A local directory (absolute, relative to the CWD or to the
            project root) or a Hugging Face Hub model id.

    Returns:
        A path string for local models, or the unchanged Hub id.
    """
    for candidate in (Path(model_path), PROJECT_ROOT / model_path):
        if candidate.is_dir():
            return str(candidate.resolve())
    return model_path


def load_nllb(
    model_path: str, device: torch.device
) -> tuple[PreTrainedModel, PreTrainedTokenizerBase]:
    """Load an NLLB model for inference (fp16 on GPU) and its tokenizer."""
    tokenizer = get_tokenizer(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    if device.type == "cuda":
        model = model.half()
    return model.to(device).eval(), tokenizer


def translate_nllb(
    texts: list[str],
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizerBase,
    batch_size: int = 32,
    num_beams: int = EVAL_NUM_BEAMS,
    max_new_tokens: int = MAX_LENGTH,
) -> list[str]:
    """Translate English sentences to Khmer with NLLB.

    Sentences are sorted by length before batching to reduce padding, then put
    back in their original order.
    """
    khmer_bos_id = tokenizer.convert_tokens_to_ids(TGT_LANG)
    order = sorted(range(len(texts)), key=lambda i: len(texts[i]), reverse=True)
    translations = [""] * len(texts)

    for start in tqdm(range(0, len(order), batch_size), desc="Translating"):
        indices = order[start : start + batch_size]
        encoded = tokenizer(
            [texts[i] for i in indices],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_LENGTH,
        ).to(model.device)
        with torch.inference_mode():
            generated = model.generate(
                **encoded,
                forced_bos_token_id=khmer_bos_id,
                num_beams=num_beams,
                max_new_tokens=max_new_tokens,
            )
        decoded = tokenizer.batch_decode(generated, skip_special_tokens=True)
        for index, text in zip(indices, decoded):
            translations[index] = text.strip()
    return translations


def translate_texts(
    model_path: str, texts: list[str], batch_size: int, num_beams: int
) -> list[str]:
    """Translate with either a scratch model directory or an NLLB model."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if ScratchTranslator.is_scratch_dir(model_path):
        translator = ScratchTranslator.load(Path(model_path), device)
        translations: list[str] = []
        step = batch_size * 8  # The small model can decode bigger batches.
        for start in tqdm(range(0, len(texts), step), desc="Translating"):
            translations += translator.translate(
                texts[start : start + step], batch_size=step, num_beams=num_beams
            )
        return translations
    model, tokenizer = load_nllb(model_path, device)
    return translate_nllb(texts, model, tokenizer, batch_size=batch_size, num_beams=num_beams)


def save_predictions(
    sources: list[str], references: list[str], hypotheses: list[str], path: Path
) -> None:
    """Write one JSON object per line with source, reference and hypothesis."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for src, ref, hyp in zip(sources, references, hypotheses):
            f.write(json.dumps({"src": src, "ref": ref, "hyp": hyp}, ensure_ascii=False) + "\n")


def load_saved_hypotheses(
    path: Path, sources: list[str], references: list[str]
) -> list[str]:
    """Read translations saved by an earlier run, checking they cover this exact test set.

    Args:
        path: A predictions JSONL file (``{"src", "ref", "hyp"}`` per line).
        sources: The current test sources, in order.
        references: The current test references, in order.

    Returns:
        The saved hypotheses, in test-set order.

    Raises:
        ValueError: If the file does not match the test set sentence for sentence.
    """
    with path.open(encoding="utf-8") as f:
        rows = [json.loads(line) for line in f]
    if len(rows) != len(sources):
        raise ValueError(f"{path} has {len(rows)} predictions; the test set has {len(sources)}.")
    for i, (row, src, ref) in enumerate(zip(rows, sources, references)):
        if row["src"] != src or row["ref"] != ref:
            raise ValueError(f"{path} does not match the test set at sentence {i}.")
    return [row["hyp"] for row in rows]


def evaluate_model(
    approach_key: str,
    model_path: str,
    output_path: Path,
    predictions_path: Path,
    batch_size: int = 32,
    num_beams: int = EVAL_NUM_BEAMS,
    max_samples: int | None = TEST_EVAL_SIZE,
    from_predictions: Path | None = None,
) -> dict:
    """Translate the test subset, score it, and save metrics and predictions.

    Args:
        approach_key: Name recorded in the results file.
        model_path: Hub id, NLLB directory or scratch-model directory.
        output_path: JSON file for the metrics.
        predictions_path: JSONL file for every source / reference / hypothesis.
        batch_size: Sentences per generation batch (NLLB).
        num_beams: Beam size for decoding.
        max_samples: Number of test sentences (``None`` = the whole test split).
        from_predictions: Re-score translations saved by an earlier run instead
            of translating again (verified against the test set first).

    Returns:
        The metrics dictionary that was saved.
    """
    set_seed(SEED)
    model_path = resolve_model_path(model_path)
    print(f"Evaluating {approach_key}: {model_path}")

    test = load_tokenized_datasets()["test"]
    if max_samples is not None and max_samples < len(test):
        test = test.select(range(max_samples))
    sources, references = list(test[SRC_COLUMN]), list(test[TGT_COLUMN])

    if from_predictions is not None:
        print(f"Re-scoring saved translations from {from_predictions}")
        hypotheses = load_saved_hypotheses(from_predictions, sources, references)
        elapsed = None
    else:
        start = time.perf_counter()
        hypotheses = translate_texts(model_path, sources, batch_size, num_beams)
        elapsed = round(time.perf_counter() - start, 2)

    results = {
        "approach": approach_key,
        "model": model_path,
        "source_lang": SRC_LANG,
        "target_lang": TGT_LANG,
        "split": "test",
        "num_samples": len(sources),
        "num_beams": num_beams,
        **compute_translation_metrics(hypotheses, references),
        "inference_seconds": elapsed,
        "rescored_from": from_predictions.name if from_predictions else None,
        "timestamp": utc_timestamp(),
    }
    save_json(results, output_path)
    save_predictions(sources, references, hypotheses, predictions_path)
    return results


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Evaluate an approach on the test set.")
    parser.add_argument(
        "--approach", choices=list(APPROACHES), default="baseline",
        help="Which approach to evaluate; sets the model path and output files.",
    )
    parser.add_argument("--model-path", default=None, help="Override the approach's model path.")
    parser.add_argument("--output", type=Path, default=None, help="Override the metrics JSON path.")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--num-beams", type=int, default=EVAL_NUM_BEAMS)
    parser.add_argument(
        "--max-samples", type=int, default=TEST_EVAL_SIZE,
        help="Test sentences to use; -1 = the whole test split.",
    )
    parser.add_argument(
        "--from-predictions", type=Path, default=None,
        help="Re-score a predictions JSONL from an earlier run instead of translating again "
        "(must match the test set exactly, and must use the same --num-beams).",
    )
    return parser.parse_args()


def main() -> None:
    """Evaluate one approach and print its scores."""
    args = parse_args()
    approach = APPROACHES[args.approach]
    output = args.output or approach.results_path
    if not output.is_absolute():
        output = PROJECT_ROOT / output
    predictions = (
        approach.predictions_path if args.output is None
        else output.with_name(f"{output.stem}_predictions.jsonl")
    )
    results = evaluate_model(
        approach_key=approach.key,
        model_path=args.model_path or approach.model_path,
        output_path=output,
        predictions_path=predictions,
        batch_size=args.batch_size,
        num_beams=args.num_beams,
        max_samples=None if args.max_samples == -1 else args.max_samples,
        from_predictions=args.from_predictions,
    )
    print(f"chrF++ : {results['chrf++']:.2f}")
    print(f"chrF   : {results['chrf']:.2f}")
    print(f"BLEU   : {results['bleu']:.2f} (tokenizer={results['bleu_tokenizer']})")
    print(f"Saved metrics to {output}")


if __name__ == "__main__":
    main()
