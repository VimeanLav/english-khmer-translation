"""Approach A: train a Transformer from scratch for English -> Khmer.

Pipeline:

1. Train a joint English+Khmer SentencePiece (unigram) tokenizer on the
   training split only, so no validation or test text leaks into the vocabulary.
2. Train :class:`src.model_scratch.Seq2SeqTransformer` with a hand-written
   PyTorch loop: AdamW, linear warmup then linear decay, label smoothing, fp16
   mixed precision and gradient clipping.
3. After every epoch, compute the validation loss and chrF++/BLEU (greedy
   decoding on the validation subset), save a full training checkpoint with
   ``torch.save``, and keep the best model by validation chrF++.
4. Stop early when validation chrF++ has not improved for ``--patience`` epochs.

A checkpoint holds the model, optimizer, scheduler, grad-scaler and RNG states,
so ``--resume`` continues exactly where a disconnected Colab session stopped
(at epoch granularity).

Run from the project root:

    python -m src.train_scratch
    python -m src.train_scratch --epochs 1 --max-train-samples 5000   # smoke test
"""

from __future__ import annotations

import argparse
import math
import os
import random
import time
from pathlib import Path
from typing import Any

import numpy as np
import sentencepiece as spm
import torch
from torch import nn

from src.config import (
    APPROACHES,
    CHECKPOINTS_DIR,
    MODELS_DIR,
    SEED,
    SRC_COLUMN,
    TGT_COLUMN,
    VAL_EVAL_SIZE,
)
from src.data import load_tokenized_datasets
from src.model_scratch import (
    BOS_ID,
    EOS_ID,
    PAD_ID,
    UNK_ID,
    ScratchConfig,
    ScratchTranslator,
    Seq2SeqTransformer,
    pad_batch,
)
from src.utils.metrics import compute_translation_metrics
from src.utils.reporting import (
    count_parameters,
    hardware_info,
    make_history,
    peak_vram_gb,
    save_json,
    utc_timestamp,
)
from src.utils.seed import set_seed

CHECKPOINT_DIR = CHECKPOINTS_DIR / "scratch"
CHECKPOINT_FILE = CHECKPOINT_DIR / "last.pt"
FINAL_MODEL_DIR = MODELS_DIR / "scratch"


# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #
def train_sentencepiece(texts: list[str], model_dir: Path, vocab_size: int) -> spm.SentencePieceProcessor:
    """Train a joint unigram SentencePiece model on training text, or reuse it.

    An existing ``spm.model`` is reused when its vocabulary size matches, so a
    resumed run keeps the exact same tokenizer.

    Args:
        texts: English and Khmer training sentences.
        model_dir: Directory to write ``spm.model`` into.
        vocab_size: Size of the shared vocabulary.

    Returns:
        The loaded SentencePiece processor.
    """
    model_file = model_dir / ScratchTranslator.SPM_FILE
    if model_file.is_file():
        sp = spm.SentencePieceProcessor(model_file=str(model_file))
        if sp.get_piece_size() == vocab_size:
            return sp

    model_dir.mkdir(parents=True, exist_ok=True)
    spm.SentencePieceTrainer.train(
        sentence_iterator=iter(texts),
        model_prefix=str(model_file.with_suffix("")),
        vocab_size=vocab_size,
        model_type="unigram",
        character_coverage=1.0,  # Keep every Khmer character.
        pad_id=PAD_ID, unk_id=UNK_ID, bos_id=BOS_ID, eos_id=EOS_ID,
        minloglevel=2,
    )
    return spm.SentencePieceProcessor(model_file=str(model_file))


def batches(
    src: list[list[int]], tgt: list[list[int]], batch_size: int, generator: torch.Generator | None
) -> list[tuple[torch.Tensor, torch.Tensor]]:
    """Split encoded pairs into padded (src, tgt) batches, shuffled if a generator is given."""
    order = (
        torch.randperm(len(src), generator=generator).tolist() if generator is not None
        else list(range(len(src)))
    )
    return [
        (pad_batch([src[i] for i in chunk]), pad_batch([tgt[i] for i in chunk]))
        for chunk in (order[s : s + batch_size] for s in range(0, len(order), batch_size))
    ]


# --------------------------------------------------------------------------- #
# Checkpointing
# --------------------------------------------------------------------------- #
def save_checkpoint(path: Path, state: dict[str, Any]) -> None:
    """Save a training checkpoint atomically (write to a temp file, then rename).

    A disconnect while writing therefore never leaves a half-written checkpoint.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    torch.save(state, tmp)
    os.replace(tmp, path)


def load_checkpoint(path: Path, device: torch.device) -> dict[str, Any]:
    """Load a checkpoint written by :func:`save_checkpoint`.

    ``weights_only=False`` is needed because the file also stores Python and
    NumPy RNG states. That is safe here because we wrote the file ourselves.
    """
    return torch.load(path, map_location=device, weights_only=False)


def rng_state() -> dict[str, Any]:
    """Capture every RNG state so a resumed run continues identically."""
    return {
        "python": random.getstate(),
        "numpy": np.random.get_state(),
        "torch": torch.get_rng_state(),
        "cuda": torch.cuda.get_rng_state_all() if torch.cuda.is_available() else None,
    }


def restore_rng_state(state: dict[str, Any]) -> None:
    """Restore RNG states captured by :func:`rng_state`."""
    random.setstate(state["python"])
    np.random.set_state(state["numpy"])
    torch.set_rng_state(state["torch"].cpu())
    if state["cuda"] is not None and torch.cuda.is_available():
        torch.cuda.set_rng_state_all([s.cpu() for s in state["cuda"]])


# --------------------------------------------------------------------------- #
# Evaluation
# --------------------------------------------------------------------------- #
@torch.no_grad()
def validation_loss(
    model: Seq2SeqTransformer, val_batches: list, criterion: nn.Module, device: torch.device
) -> float:
    """Teacher-forced cross-entropy on the validation subset (token-weighted mean)."""
    model.eval()
    total, tokens = 0.0, 0
    for src, tgt in val_batches:
        src, tgt = src.to(device), tgt.to(device)
        with torch.autocast("cuda", dtype=torch.float16):
            logits = model(src, tgt[:, :-1])
        labels = tgt[:, 1:]
        n = int(labels.ne(PAD_ID).sum())
        total += criterion(logits.float().reshape(-1, logits.size(-1)), labels.reshape(-1)).item() * n
        tokens += n
    return total / max(tokens, 1)


# --------------------------------------------------------------------------- #
# Training
# --------------------------------------------------------------------------- #
def run_scratch_experiment(args: argparse.Namespace, tuning: bool = False) -> dict[str, Any]:
    """Train approach A and return its summary.

    Args:
        args: Parsed options from :func:`parse_args`.
        tuning: Hyperparameter-tuning trial: nothing is saved except the
            SentencePiece model; the returned summary holds the validation metrics.
    """
    if not torch.cuda.is_available():
        raise SystemExit("CUDA GPU not found; fp16 training requires one (see src/check_gpu.py).")
    device = torch.device("cuda")
    set_seed(args.seed)
    torch.cuda.reset_peak_memory_stats()

    # ---- Data and tokenizer (training split only) ---------------------------
    datasets = load_tokenized_datasets()
    train, validation = datasets["train"], datasets["validation"]
    # The tokenizer always sees the full training split, so tuning trials on a
    # subset and the final run share exactly the same vocabulary.
    sp = train_sentencepiece(
        list(train[SRC_COLUMN]) + list(train[TGT_COLUMN]), FINAL_MODEL_DIR, args.vocab_size
    )
    if args.max_train_samples is not None and args.max_train_samples < len(train):
        train = train.shuffle(seed=args.seed).select(range(args.max_train_samples))
    validation = validation.select(range(min(args.max_eval_samples, len(validation))))
    val_sources, val_references = list(validation[SRC_COLUMN]), list(validation[TGT_COLUMN])
    config = ScratchConfig(
        vocab_size=sp.get_piece_size(),
        d_model=args.d_model,
        nhead=args.heads,
        num_encoder_layers=args.layers,
        num_decoder_layers=args.layers,
        dim_feedforward=args.ffn_dim,
        dropout=args.dropout,
    )
    model = Seq2SeqTransformer(config).to(device)
    translator = ScratchTranslator(model, sp)
    trainable, total = count_parameters(model)
    print(f"Trainable parameters: {trainable:,} / {total:,}")

    train_src = [translator.encode_source(t) for t in train[SRC_COLUMN]]
    train_tgt = [translator.encode_target(t) for t in train[TGT_COLUMN]]
    val_batches = batches(
        [translator.encode_source(t) for t in val_sources],
        [translator.encode_target(t) for t in val_references],
        args.batch_size, generator=None,
    )

    # ---- Optimisation -------------------------------------------------------
    steps_per_epoch = math.ceil(len(train_src) / args.batch_size)
    total_steps = steps_per_epoch * args.epochs
    warmup_steps = math.ceil(args.warmup_ratio * total_steps)
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.learning_rate, betas=(0.9, 0.98), eps=1e-9,
        weight_decay=args.weight_decay,
    )

    def lr_lambda(step: int) -> float:
        """Linear warmup to the peak learning rate, then linear decay to zero."""
        if step < warmup_steps:
            return (step + 1) / warmup_steps
        return max(0.0, (total_steps - step) / max(1, total_steps - warmup_steps))

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
    scaler = torch.amp.GradScaler("cuda")
    criterion = nn.CrossEntropyLoss(ignore_index=PAD_ID, label_smoothing=args.label_smoothing)

    # ---- State (restored from a checkpoint when resuming) -------------------
    start_epoch, global_step = 0, 0
    best_chrf, epochs_without_improvement = -1.0, 0
    train_log: list[dict] = []
    eval_log: list[dict] = []
    step_seconds, wall_seconds = 0.0, 0.0
    if args.resume and not tuning and CHECKPOINT_FILE.is_file():
        ckpt = load_checkpoint(CHECKPOINT_FILE, device)
        model.load_state_dict(ckpt["model"])
        optimizer.load_state_dict(ckpt["optimizer"])
        scheduler.load_state_dict(ckpt["scheduler"])
        scaler.load_state_dict(ckpt["scaler"])
        restore_rng_state(ckpt["rng"])
        start_epoch, global_step = ckpt["epoch"] + 1, ckpt["global_step"]
        best_chrf = ckpt["best_chrf"]
        epochs_without_improvement = ckpt["epochs_without_improvement"]
        train_log, eval_log = ckpt["train_log"], ckpt["eval_log"]
        step_seconds, wall_seconds = ckpt["step_seconds"], ckpt["wall_seconds"]
        print(f"Resumed from {CHECKPOINT_FILE} at epoch {start_epoch} (step {global_step}).")

    # ---- Epoch loop ---------------------------------------------------------
    for epoch in range(start_epoch, args.epochs):
        if epochs_without_improvement >= args.patience:
            print(f"Early stopping: no improvement for {args.patience} epochs.")
            break
        epoch_start = time.perf_counter()
        model.train()
        # A per-epoch generator makes the shuffle order reproducible after a resume.
        generator = torch.Generator().manual_seed(args.seed + epoch)
        running_loss, running_steps = 0.0, 0

        for src, tgt in batches(train_src, train_tgt, args.batch_size, generator):
            step_start = time.perf_counter()
            src, tgt = src.to(device), tgt.to(device)
            with torch.autocast("cuda", dtype=torch.float16):
                # Teacher forcing: predict tgt[1:] from tgt[:-1].
                logits = model(src, tgt[:, :-1])
                loss = criterion(logits.float().reshape(-1, logits.size(-1)), tgt[:, 1:].reshape(-1))
            optimizer.zero_grad(set_to_none=True)
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
            scaler.step(optimizer)
            scaler.update()
            scheduler.step()
            global_step += 1
            running_loss += loss.item()  # .item() also synchronises the GPU for timing.
            running_steps += 1
            step_seconds += time.perf_counter() - step_start

            if global_step % args.logging_steps == 0:
                train_log.append({
                    "step": global_step,
                    "epoch": round(global_step / steps_per_epoch, 4),
                    "loss": running_loss / running_steps,
                    "lr": scheduler.get_last_lr()[0],
                })
                running_loss, running_steps = 0.0, 0

        # ---- End-of-epoch validation ----------------------------------------
        val_loss = validation_loss(model, val_batches, criterion, device)
        hypotheses = translator.translate(val_sources, batch_size=128, num_beams=1)
        scores = compute_translation_metrics(hypotheses, val_references)
        eval_log.append({
            "step": global_step, "epoch": epoch + 1, "loss": val_loss,
            "chrf++": scores["chrf++"], "chrf": scores["chrf"], "bleu": scores["bleu"],
        })
        wall_seconds += time.perf_counter() - epoch_start
        print(
            f"epoch {epoch + 1}/{args.epochs} | step {global_step} | val loss {val_loss:.3f} "
            f"| val chrF++ {scores['chrf++']:.2f} | BLEU {scores['bleu']:.2f}"
        )

        if scores["chrf++"] > best_chrf:
            best_chrf, epochs_without_improvement = scores["chrf++"], 0
            if not tuning:
                translator.save(FINAL_MODEL_DIR)  # Best weights so far, via torch.save.
        else:
            epochs_without_improvement += 1

        if not tuning:
            save_checkpoint(CHECKPOINT_FILE, {
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict(),
                "scheduler": scheduler.state_dict(),
                "scaler": scaler.state_dict(),
                "rng": rng_state(),
                "epoch": epoch,
                "global_step": global_step,
                "best_chrf": best_chrf,
                "epochs_without_improvement": epochs_without_improvement,
                "train_log": train_log,
                "eval_log": eval_log,
                "step_seconds": step_seconds,
                "wall_seconds": wall_seconds,
                "config": vars(args),
            })

    best_eval = max(eval_log, key=lambda e: e["chrf++"]) if eval_log else {}
    summary = {
        "approach": "scratch",
        "label": APPROACHES["scratch"].label,
        "trainable_params": trainable,
        "total_params": total,
        "hyperparameters": {
            "learning_rate": args.learning_rate,
            "weight_decay": args.weight_decay,
            "dropout": args.dropout,
            "label_smoothing": args.label_smoothing,
            "epochs": args.epochs,
            "batch_size": args.batch_size,
            "warmup_steps": warmup_steps,
            "vocab_size": config.vocab_size,
            "d_model": args.d_model,
            "layers": args.layers,
            "heads": args.heads,
            "ffn_dim": args.ffn_dim,
            "optimizer": "adamw",
            "fp16": True,
            "seed": args.seed,
        },
        "steps_completed": global_step,
        "examples_seen": global_step * args.batch_size,
        "train_step_seconds": round(step_seconds, 1),
        "seconds_per_step": round(step_seconds / max(global_step, 1), 4),
        "wall_seconds": round(wall_seconds, 1),
        "peak_vram_gb": peak_vram_gb(),
        "val_metrics": {k: v for k, v in best_eval.items() if k not in ("step", "epoch")},
        "best_epoch": best_eval.get("epoch"),
        "hardware": hardware_info(),
        "timestamp": utc_timestamp(),
    }
    if not tuning:
        approach = APPROACHES["scratch"]
        save_json(make_history("scratch", args.batch_size, train_log, eval_log), approach.history_path)
        save_json(summary, approach.summary_path)
        print(f"Best model (epoch {best_eval.get('epoch')}) saved to {FINAL_MODEL_DIR}")
    return summary


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    p = argparse.ArgumentParser(description="Approach A: Transformer trained from scratch.")
    p.add_argument("--vocab-size", type=int, default=16000)
    p.add_argument("--d-model", type=int, default=256)
    p.add_argument("--layers", type=int, default=4, help="Encoder and decoder layers each.")
    p.add_argument("--heads", type=int, default=4)
    p.add_argument("--ffn-dim", type=int, default=1024)
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--label-smoothing", type=float, default=0.1)
    p.add_argument("--learning-rate", type=float, default=5e-4)
    p.add_argument("--weight-decay", type=float, default=0.01)
    p.add_argument("--warmup-ratio", type=float, default=0.05)
    p.add_argument("--max-grad-norm", type=float, default=1.0)
    p.add_argument("--batch-size", type=int, default=128)
    p.add_argument("--epochs", type=int, default=15)
    p.add_argument("--patience", type=int, default=3, help="Early-stopping patience in epochs.")
    p.add_argument("--logging-steps", type=int, default=50)
    p.add_argument("--max-train-samples", type=int, default=None)
    p.add_argument("--max-eval-samples", type=int, default=VAL_EVAL_SIZE)
    p.add_argument("--seed", type=int, default=SEED)
    p.add_argument(
        "--resume", "--resume-from-checkpoint", "--resume_from_checkpoint",
        action="store_true", help=f"Resume from {CHECKPOINT_FILE.relative_to(CHECKPOINTS_DIR.parent)}.",
    )
    p.add_argument(
        "--tuning-output", type=Path, default=None,
        help="Run as a tuning trial (nothing saved) and write the summary JSON here. "
        "Used by src.tune.",
    )
    return p.parse_args(argv)


def main() -> None:
    """Train approach A and save the best model to ``models/scratch``."""
    args = parse_args()
    if args.tuning_output is None:
        run_scratch_experiment(args)
    else:
        save_json(run_scratch_experiment(args, tuning=True), args.tuning_output)


if __name__ == "__main__":
    main()
