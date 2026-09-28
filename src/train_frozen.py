"""Approach B: fine-tune NLLB for English -> Khmer with a frozen backbone.

Every parameter is frozen except the decoder cross-attention blocks
(``encoder_attn`` and their layer norms), which is about 8% of the model. These
are the layers that connect English encoder states to Khmer decoding, so
adapting them is a cheap way to specialise the model.

The output projection (``lm_head``) stays frozen because NLLB ties it to the
256k-token shared embedding matrix. Training it would also update the
embeddings used by the encoder and decoder, and would add about 262M trainable
parameters.

Run from the project root:

    python -m src.train_frozen
    python -m src.train_frozen --max-steps 50 --eval-steps 25 --save-steps 25   # smoke test
"""

from __future__ import annotations

import argparse

from transformers import PreTrainedModel

from src.config import APPROACHES, CHECKPOINTS_DIR, MODELS_DIR
from src.utils.training import add_common_args, run_from_cli

CHECKPOINT_DIR = CHECKPOINTS_DIR / "frozen"
FINAL_MODEL_DIR = MODELS_DIR / "nllb_frozen"


def freeze_backbone(model: PreTrainedModel) -> None:
    """Freeze everything except the decoder cross-attention blocks.

    Args:
        model: An ``M2M100ForConditionalGeneration`` (NLLB) model, modified in place.
    """
    for param in model.parameters():
        param.requires_grad = False
    for layer in model.model.decoder.layers:
        for module in (layer.encoder_attn, layer.encoder_attn_layer_norm):
            for param in module.parameters():
                param.requires_grad = True


# Only ~50M parameters train, so AdamW's optimizer state fits easily in 8 GB.
TRAINING_ARGS = {"optim": "adamw_torch"}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Approach B: frozen-backbone fine-tuning of NLLB.")
    add_common_args(parser, learning_rate=1e-4, max_steps=4000, eval_steps=500, save_steps=1000)
    return parser.parse_args(argv)


def main() -> None:
    """Train the frozen-backbone model and save it to ``models/nllb_frozen``."""
    args = parse_args()
    run_from_cli(
        APPROACHES["frozen"], args, freeze_backbone, TRAINING_ARGS, CHECKPOINT_DIR, FINAL_MODEL_DIR
    )


if __name__ == "__main__":
    main()
