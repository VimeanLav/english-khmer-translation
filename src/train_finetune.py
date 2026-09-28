"""Approach C: full fine-tuning of NLLB for English -> Khmer (all parameters trainable).

Memory on an 8 GB GPU: with fp16 mixed precision the Trainer keeps fp32 master
weights. For 615M parameters, the weights and gradients take about 4.9 GB, and
AdamW's two moment buffers would add another 4.9 GB, which does not fit. This
script therefore uses:

* ``optim="adafactor"``: factored second moments use only a few MB of state.
* gradient checkpointing: recomputes activations in the backward pass.

Measured on an RTX 4070 Laptop GPU: about 1.17 s per optimizer step and a peak
of 6.6 GB. Pass ``--optim adamw_torch`` on a GPU with more memory.

Run from the project root:

    python -m src.train_finetune
    python -m src.train_finetune --max-steps 50 --eval-steps 25 --save-steps 25   # smoke test
"""

from __future__ import annotations

import argparse

from transformers import PreTrainedModel

from src.config import APPROACHES, CHECKPOINTS_DIR, MODELS_DIR
from src.utils.training import add_common_args, run_from_cli

CHECKPOINT_DIR = CHECKPOINTS_DIR / "full_finetune"
FINAL_MODEL_DIR = MODELS_DIR / "nllb_full"


def keep_all_trainable(model: PreTrainedModel) -> None:
    """Full fine-tuning: leave every parameter trainable (the default)."""
    for param in model.parameters():
        param.requires_grad = True


def training_args_for(optim: str, gradient_checkpointing: bool) -> dict:
    """Memory-related Trainer settings for full fine-tuning."""
    return {
        "optim": optim,
        "gradient_checkpointing": gradient_checkpointing,
        "gradient_checkpointing_kwargs": {"use_reentrant": False},
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Approach C: full fine-tuning of NLLB.")
    add_common_args(parser, learning_rate=2e-5, max_steps=2000, eval_steps=250, save_steps=500)
    parser.add_argument(
        "--optim", default="adafactor",
        help="Trainer optimizer name. 'adamw_torch' will likely run out of memory on 8 GB.",
    )
    parser.add_argument(
        "--no-gradient-checkpointing", action="store_true",
        help="Disable gradient checkpointing (faster, uses more VRAM).",
    )
    return parser.parse_args(argv)


def main() -> None:
    """Fully fine-tune NLLB and save it to ``models/nllb_full``."""
    args = parse_args()
    run_from_cli(
        APPROACHES["full"],
        args,
        keep_all_trainable,
        training_args_for(args.optim, not args.no_gradient_checkpointing),
        CHECKPOINT_DIR,
        FINAL_MODEL_DIR,
    )


if __name__ == "__main__":
    main()
