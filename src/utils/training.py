"""Shared training pipeline for the two NLLB approaches (B: frozen, C: full).

Both approaches use the same data, batch size, schedule, evaluation and
logging. They differ only in which parameters are trainable and in the
optimizer and memory settings passed in by each script.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

import torch
from datasets import Dataset
from transformers import (
    AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq,
    PreTrainedModel,
    PreTrainedTokenizerBase,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    TrainerCallback,
)

from src.config import (
    LABEL_PAD_ID,
    MAX_LENGTH,
    MODEL_NAME,
    SEED,
    TGT_LANG,
    VAL_EVAL_SIZE,
    Approach,
)
from src.data import get_tokenizer, load_tokenized_datasets
from src.utils.metrics import build_compute_metrics
from src.utils.reporting import (
    count_parameters,
    hardware_info,
    history_from_trainer_logs,
    peak_vram_gb,
    save_json,
    utc_timestamp,
)
from src.utils.seed import set_seed

# Effective batch size: 8 sentence pairs x 2 gradient-accumulation steps.
TRAIN_BATCH_SIZE = 8
GRAD_ACCUM_STEPS = 2
EXAMPLES_PER_STEP = TRAIN_BATCH_SIZE * GRAD_ACCUM_STEPS


def require_cuda() -> None:
    """Exit with a helpful message if no CUDA GPU is available (fp16 needs one)."""
    if not torch.cuda.is_available():
        raise SystemExit(
            "CUDA GPU not found, but fp16 training requires one. Install the CUDA "
            "build of PyTorch (see requirements.txt) and run `python src/check_gpu.py`."
        )


def load_model(
    tokenizer: PreTrainedTokenizerBase,
    model_name: str = MODEL_NAME,
    dropout: float | None = None,
) -> PreTrainedModel:
    """Load NLLB and configure generation to always produce Khmer.

    Args:
        tokenizer: NLLB tokenizer, used to look up the ``khm_Khmr`` token id.
        model_name: Hub model id or local checkpoint directory.
        dropout: Optional override of the model's dropout rate (0.1 by default).
            It must be passed at load time because each layer copies the rate
            from the config when it is built.

    Returns:
        The seq2seq model with ``forced_bos_token_id`` set to Khmer.
    """
    overrides = {} if dropout is None else {"dropout": dropout}
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, **overrides)
    model.generation_config.forced_bos_token_id = tokenizer.convert_tokens_to_ids(TGT_LANG)
    return model


def load_train_eval_datasets(
    max_train_samples: int | None = None,
    max_eval_samples: int | None = VAL_EVAL_SIZE,
    seed: int = SEED,
) -> tuple[Dataset, Dataset]:
    """Load the tokenized train split and a fixed validation subset.

    Generating translations for the full validation split at every evaluation
    step is slow, so only its first ``max_eval_samples`` sentences are used.
    """
    datasets = load_tokenized_datasets()
    train, validation = datasets["train"], datasets["validation"]
    if max_train_samples is not None and max_train_samples < len(train):
        train = train.shuffle(seed=seed).select(range(max_train_samples))
    if max_eval_samples is not None and max_eval_samples < len(validation):
        validation = validation.select(range(max_eval_samples))
    return train, validation


class TimingCallback(TrainerCallback):
    """Measure pure optimizer-step time, excluding evaluation and checkpointing.

    Totals are written next to the checkpoints at every save, so the reported
    training time stays correct when a run is resumed after a disconnect.
    """

    def __init__(self, state_file: Path | None) -> None:
        self.state_file = state_file
        self.step_seconds = 0.0
        self.timed_steps = 0
        self.wall_seconds = 0.0
        self._wall_base = 0.0
        self._wall_start = 0.0
        self._step_start = 0.0

    def on_train_begin(self, args, state, control, **kwargs):
        if self.state_file and self.state_file.is_file() and state.global_step > 0:
            saved = json.loads(self.state_file.read_text(encoding="utf-8"))
            if saved["global_step"] == state.global_step:
                self.step_seconds = saved["step_seconds"]
                self.timed_steps = saved["timed_steps"]
                self.wall_seconds = saved["wall_seconds"]
        self._wall_base = self.wall_seconds
        self._wall_start = time.perf_counter()

    def on_step_begin(self, args, state, control, **kwargs):
        self._step_start = time.perf_counter()

    def on_step_end(self, args, state, control, **kwargs):
        torch.cuda.synchronize()
        self.step_seconds += time.perf_counter() - self._step_start
        self.timed_steps += 1

    def on_save(self, args, state, control, **kwargs):
        self._write(state.global_step)

    def on_train_end(self, args, state, control, **kwargs):
        self._write(state.global_step)

    def _write(self, global_step: int) -> None:
        self.wall_seconds = self._wall_base + time.perf_counter() - self._wall_start
        if self.state_file:
            save_json(
                {
                    "global_step": global_step,
                    "step_seconds": self.step_seconds,
                    "timed_steps": self.timed_steps,
                    "wall_seconds": self.wall_seconds,
                },
                self.state_file,
            )


def add_common_args(
    parser: argparse.ArgumentParser,
    *,
    learning_rate: float,
    max_steps: int,
    eval_steps: int,
    save_steps: int,
) -> None:
    """Add the command-line options shared by both NLLB training scripts."""
    parser.add_argument("--learning-rate", type=float, default=learning_rate)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument(
        "--dropout", type=float, default=None,
        help="Override NLLB's dropout rate (pretrained default: 0.1).",
    )
    parser.add_argument(
        "--max-steps", type=int, default=max_steps,
        help=f"Optimizer steps of {EXAMPLES_PER_STEP} sentence pairs. -1 = use --epochs.",
    )
    parser.add_argument("--epochs", type=float, default=1.0, help="Used only if --max-steps is -1.")
    parser.add_argument("--warmup-ratio", type=float, default=0.1, help="Linear warmup fraction.")
    parser.add_argument("--eval-steps", type=int, default=eval_steps)
    parser.add_argument(
        "--save-steps", type=int, default=save_steps,
        help="Checkpoint interval; must be a multiple of --eval-steps.",
    )
    parser.add_argument("--logging-steps", type=int, default=50)
    parser.add_argument("--max-train-samples", type=int, default=None)
    parser.add_argument("--max-eval-samples", type=int, default=VAL_EVAL_SIZE)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument(
        "--resume", "--resume-from-checkpoint", "--resume_from_checkpoint",
        action="store_true", help="Resume from the latest checkpoint.",
    )
    parser.add_argument(
        "--tuning-output", type=Path, default=None,
        help="Run as a tuning trial (nothing saved) and write the summary JSON here. "
        "Used by src.tune.",
    )


def run_from_cli(
    approach: Approach,
    args: argparse.Namespace,
    configure_model: Callable[[PreTrainedModel], None],
    extra_training_args: dict[str, Any],
    checkpoint_dir: Path,
    final_model_dir: Path,
) -> None:
    """Entry point shared by the NLLB scripts: a full run or a tuning trial."""
    if args.tuning_output is None:
        run_nllb_experiment(
            approach, args, configure_model, extra_training_args, checkpoint_dir, final_model_dir
        )
        return
    trial_dir = checkpoint_dir.parent / "tuning" / approach.key
    try:
        summary = run_nllb_experiment(
            approach, args, configure_model, extra_training_args, trial_dir, final_model_dir=None
        )
    finally:
        remove_dir(trial_dir)
    save_json(summary, args.tuning_output)


def run_nllb_experiment(
    approach: Approach,
    args: argparse.Namespace,
    configure_model: Callable[[PreTrainedModel], None],
    extra_training_args: dict[str, Any],
    checkpoint_dir: Path,
    final_model_dir: Path | None,
) -> dict[str, Any]:
    """Train one NLLB approach and write its model, history and summary.

    Args:
        approach: The approach being trained (from ``src.config.APPROACHES``).
        args: Parsed options from :func:`add_common_args`.
        configure_model: Called on the loaded model, e.g. to freeze layers.
        extra_training_args: Approach-specific ``Seq2SeqTrainingArguments``
            (optimizer, gradient checkpointing, ...).
        checkpoint_dir: Where the Trainer writes checkpoints.
        final_model_dir: Where the best model is saved. ``None`` runs a
            hyperparameter-tuning trial: no checkpoints, no saved model and no
            result files, only the returned validation metrics.

    Returns:
        The training summary (also saved to ``results/`` unless tuning).
    """
    tuning = final_model_dir is None
    require_cuda()
    set_seed(args.seed)
    torch.cuda.reset_peak_memory_stats()

    tokenizer = get_tokenizer()
    model = load_model(tokenizer, dropout=args.dropout)
    configure_model(model)
    trainable, total = count_parameters(model)
    print(f"Trainable parameters: {trainable:,} / {total:,} ({100 * trainable / total:.2f}%)")

    train_dataset, eval_dataset = load_train_eval_datasets(
        args.max_train_samples, args.max_eval_samples, args.seed
    )
    max_steps = (
        args.max_steps if args.max_steps > 0
        else math.ceil(len(train_dataset) / EXAMPLES_PER_STEP * args.epochs)
    )

    training_args = Seq2SeqTrainingArguments(
        output_dir=str(checkpoint_dir),
        # Batch / precision.
        per_device_train_batch_size=TRAIN_BATCH_SIZE,
        per_device_eval_batch_size=16,
        gradient_accumulation_steps=GRAD_ACCUM_STEPS,
        fp16=True,
        # Optimisation: linear warmup, then linear decay to zero.
        learning_rate=args.learning_rate,
        lr_scheduler_type="linear",
        warmup_steps=math.ceil(args.warmup_ratio * max_steps),
        weight_decay=args.weight_decay,
        max_steps=max_steps,
        # Evaluation and checkpointing (tuning trials only evaluate once, at the end).
        eval_strategy="no" if tuning else "steps",
        eval_steps=args.eval_steps,
        save_strategy="no" if tuning else "steps",
        save_steps=args.save_steps,
        save_total_limit=1,  # Keeps the latest and the best checkpoint.
        load_best_model_at_end=not tuning,
        metric_for_best_model="chrf++",
        greater_is_better=True,
        # Greedy decoding on the validation subset keeps evaluation cheap.
        predict_with_generate=True,
        generation_max_length=MAX_LENGTH,
        generation_num_beams=1,
        # Logging and reproducibility. Windows: load data in the main process.
        logging_steps=args.logging_steps,
        dataloader_num_workers=0,
        report_to="none",
        seed=args.seed,
        data_seed=args.seed,
        **extra_training_args,
    )

    timing = TimingCallback(None if tuning else checkpoint_dir / "timing.json")
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=DataCollatorForSeq2Seq(
            tokenizer, model=model, label_pad_token_id=LABEL_PAD_ID, pad_to_multiple_of=8
        ),
        processing_class=tokenizer,
        compute_metrics=build_compute_metrics(tokenizer),
        callbacks=[timing],
    )
    # NLLB's forward() accepts **kwargs, so the Trainer assumes the model averages
    # the loss over gradient-accumulation steps itself (via `num_items_in_batch`)
    # and skips its own division. NLLB ignores that argument and returns a plain
    # per-batch mean, which would make the gradients and the logged training loss
    # GRAD_ACCUM_STEPS times too large. This makes the Trainer do the division.
    trainer.model_accepts_loss_kwargs = False
    trainer.train(resume_from_checkpoint=(args.resume and not tuning) or None)
    val_metrics = trainer.evaluate()

    summary = {
        "approach": approach.key,
        "label": approach.label,
        "trainable_params": trainable,
        "total_params": total,
        "hyperparameters": {
            "learning_rate": args.learning_rate,
            "weight_decay": args.weight_decay,
            "dropout": model.config.dropout,
            "max_steps": max_steps,
            "effective_batch_size": EXAMPLES_PER_STEP,
            "warmup_steps": training_args.warmup_steps,
            "optimizer": getattr(training_args.optim, "value", str(training_args.optim)),
            "gradient_checkpointing": training_args.gradient_checkpointing,
            "fp16": True,
            "seed": args.seed,
        },
        "steps_completed": trainer.state.global_step,
        "examples_seen": trainer.state.global_step * EXAMPLES_PER_STEP,
        "train_step_seconds": round(timing.step_seconds, 1),
        "seconds_per_step": round(timing.step_seconds / max(timing.timed_steps, 1), 4),
        "wall_seconds": round(timing.wall_seconds, 1),
        "peak_vram_gb": peak_vram_gb(),
        "val_metrics": {k.removeprefix("eval_"): v for k, v in val_metrics.items()},
        "hardware": hardware_info(),
        "timestamp": utc_timestamp(),
    }
    if tuning:
        return summary

    # Save the best model in fp16: half the disk space, same inference quality.
    final_model_dir.mkdir(parents=True, exist_ok=True)
    trainer.model.to(torch.float16).save_pretrained(str(final_model_dir))
    tokenizer.save_pretrained(str(final_model_dir))
    save_json(
        history_from_trainer_logs(approach.key, trainer.state.log_history, EXAMPLES_PER_STEP),
        approach.history_path,
    )
    save_json(summary, approach.summary_path)
    print(f"Saved final model to {final_model_dir}")
    print(f"Saved training summary to {approach.summary_path}")
    return summary


def remove_dir(path: Path) -> None:
    """Delete a directory tree if it exists (used to clean up tuning trials)."""
    if path.exists():
        shutil.rmtree(path)
