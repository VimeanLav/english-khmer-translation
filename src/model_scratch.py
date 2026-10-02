"""Approach A model: a Transformer encoder-decoder trained from scratch.

Architecture (Vaswani et al., 2017, "Attention Is All You Need"), pre-norm variant:

* one SentencePiece vocabulary shared by English and Khmer, trained on the
  training split only;
* a single embedding matrix shared by the encoder, the decoder and the output
  projection (weight tying), scaled by sqrt(d_model);
* fixed sinusoidal positional encodings;
* ``nn.TransformerEncoder`` / ``nn.TransformerDecoder`` stacks with pre-layer
  normalisation (``norm_first=True``), which trains more stably from scratch.

No pretrained weights are used. Only the architecture idea is borrowed.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import sentencepiece as spm
import torch
import torch.nn.functional as F
from torch import nn

from src.config import MAX_LENGTH

# Special-token ids reserved when training the SentencePiece model.
PAD_ID, UNK_ID, BOS_ID, EOS_ID = 0, 1, 2, 3


@dataclass
class ScratchConfig:
    """Hyperparameters that define the architecture."""

    vocab_size: int = 16000
    d_model: int = 256
    nhead: int = 4
    num_encoder_layers: int = 4
    num_decoder_layers: int = 4
    dim_feedforward: int = 1024
    dropout: float = 0.1
    max_positions: int = 256


class PositionalEncoding(nn.Module):
    """Fixed sinusoidal position encodings, added to the token embeddings."""

    def __init__(self, d_model: int, max_positions: int) -> None:
        super().__init__()
        position = torch.arange(max_positions).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(max_positions, d_model)
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        # A buffer moves with .to(device) but is not a trainable parameter.
        self.register_buffer("pe", pe.unsqueeze(0), persistent=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Add position encodings to ``x`` of shape (batch, seq_len, d_model)."""
        return x + self.pe[:, : x.size(1)]


class Seq2SeqTransformer(nn.Module):
    """Transformer encoder-decoder with tied embeddings."""

    def __init__(self, config: ScratchConfig) -> None:
        super().__init__()
        self.config = config
        d = config.d_model
        self.embedding = nn.Embedding(config.vocab_size, d, padding_idx=PAD_ID)
        self.positional = PositionalEncoding(d, config.max_positions)
        self.dropout = nn.Dropout(config.dropout)

        def encoder_layer() -> nn.TransformerEncoderLayer:
            return nn.TransformerEncoderLayer(
                d, config.nhead, config.dim_feedforward, config.dropout,
                batch_first=True, norm_first=True,
            )

        def decoder_layer() -> nn.TransformerDecoderLayer:
            return nn.TransformerDecoderLayer(
                d, config.nhead, config.dim_feedforward, config.dropout,
                batch_first=True, norm_first=True,
            )

        # Pre-norm stacks need a final LayerNorm on their output.
        self.encoder = nn.TransformerEncoder(
            encoder_layer(), config.num_encoder_layers, norm=nn.LayerNorm(d),
            enable_nested_tensor=False,
        )
        self.decoder = nn.TransformerDecoder(
            decoder_layer(), config.num_decoder_layers, norm=nn.LayerNorm(d)
        )
        self._reset_parameters()

    def _reset_parameters(self) -> None:
        """Xavier-initialise weight matrices; small normal init for embeddings."""
        for name, param in self.named_parameters():
            if param.dim() > 1 and "embedding" not in name:
                nn.init.xavier_uniform_(param)
        nn.init.normal_(self.embedding.weight, mean=0.0, std=self.config.d_model**-0.5)
        with torch.no_grad():
            self.embedding.weight[PAD_ID].zero_()

    def _embed(self, ids: torch.Tensor) -> torch.Tensor:
        x = self.embedding(ids) * math.sqrt(self.config.d_model)
        return self.dropout(self.positional(x))

    def encode(self, src: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Encode source ids (batch, src_len) into memory states and a padding mask."""
        src_padding_mask = src.eq(PAD_ID)
        memory = self.encoder(self._embed(src), src_key_padding_mask=src_padding_mask)
        return memory, src_padding_mask

    def decode_hidden(
        self, tgt_in: torch.Tensor, memory: torch.Tensor, src_padding_mask: torch.Tensor
    ) -> torch.Tensor:
        """Return decoder states (batch, tgt_len, d_model) for decoder inputs ``tgt_in``."""
        tgt_len = tgt_in.size(1)
        # True above the diagonal = position i may not attend to future positions j > i.
        causal_mask = torch.triu(
            torch.ones(tgt_len, tgt_len, dtype=torch.bool, device=tgt_in.device), diagonal=1
        )
        return self.decoder(
            self._embed(tgt_in),
            memory,
            tgt_mask=causal_mask,
            tgt_key_padding_mask=tgt_in.eq(PAD_ID),
            memory_key_padding_mask=src_padding_mask,
        )

    def project(self, hidden: torch.Tensor) -> torch.Tensor:
        """Map decoder states to vocabulary logits (weight tying: reuse the embedding matrix)."""
        return F.linear(hidden, self.embedding.weight)

    def forward(self, src: torch.Tensor, tgt_in: torch.Tensor) -> torch.Tensor:
        """Teacher-forced forward pass used for training: logits (batch, tgt_len, vocab)."""
        memory, src_padding_mask = self.encode(src)
        return self.project(self.decode_hidden(tgt_in, memory, src_padding_mask))

    @torch.no_grad()
    def generate(
        self,
        src: torch.Tensor,
        num_beams: int = 4,
        max_new_tokens: int = MAX_LENGTH,
        length_penalty: float = 1.0,
    ) -> torch.Tensor:
        """Translate a batch with beam search (``num_beams=1`` is greedy decoding).

        All ``batch x num_beams`` hypotheses are decoded in parallel. Finished
        hypotheses (those that produced EOS) are extended with PAD at no cost,
        and at the end each hypothesis score is divided by
        ``length ** length_penalty`` so longer outputs are not unfairly penalised.

        Args:
            src: Source ids of shape (batch, src_len).
            num_beams: Beam width.
            max_new_tokens: Upper bound on generated tokens. The bound actually
                used is ``min(max_new_tokens, 2 * src_len + 10)``, which stops
                runaway repetition early (Khmer needs ~1.5x the English tokens).
            length_penalty: Exponent for length normalisation.

        Returns:
            Token ids of shape (batch, out_len), starting with BOS.
        """
        batch, k = src.size(0), num_beams
        max_new_tokens = min(max_new_tokens, 2 * src.size(1) + 10)
        memory, src_padding_mask = self.encode(src)
        # Repeat every source sentence once per beam: row b*k + j is beam j of sentence b.
        memory = memory.repeat_interleave(k, dim=0)
        src_padding_mask = src_padding_mask.repeat_interleave(k, dim=0)

        seqs = torch.full((batch * k, 1), BOS_ID, dtype=torch.long, device=src.device)
        # Only the first beam is "alive" at step 0, otherwise all k beams would be identical.
        scores = torch.full((batch, k), float("-inf"), device=src.device)
        scores[:, 0] = 0.0
        scores = scores.view(-1)
        finished = torch.zeros(batch * k, dtype=torch.bool, device=src.device)
        offsets = (torch.arange(batch, device=src.device) * k).unsqueeze(1)

        for _ in range(max_new_tokens):
            # Only the last position is needed, so project just that state.
            hidden = self.decode_hidden(seqs, memory, src_padding_mask)[:, -1]
            logits = self.project(hidden).float()
            log_probs = F.log_softmax(logits, dim=-1)
            # A finished hypothesis may only be extended with PAD, at zero cost.
            log_probs[finished] = float("-inf")
            log_probs[finished, PAD_ID] = 0.0

            vocab = log_probs.size(-1)
            candidates = (scores.unsqueeze(1) + log_probs).view(batch, k * vocab)
            top_scores, top_indices = candidates.topk(k, dim=1)
            beam_origin = (offsets + top_indices // vocab).view(-1)
            next_tokens = (top_indices % vocab).view(-1, 1)

            seqs = torch.cat([seqs[beam_origin], next_tokens], dim=1)
            finished = finished[beam_origin] | next_tokens.squeeze(1).eq(EOS_ID)
            scores = top_scores.view(-1)
            if finished.all():
                break

        lengths = seqs[:, 1:].ne(PAD_ID).sum(dim=1).clamp(min=1).float()
        normalised = (scores / lengths.pow(length_penalty)).view(batch, k)
        best = normalised.argmax(dim=1)
        return seqs.view(batch, k, -1)[torch.arange(batch, device=src.device), best]


class ScratchTranslator:
    """Bundles the model with its SentencePiece tokenizer for saving and translation."""

    CONFIG_FILE = "config.json"
    WEIGHTS_FILE = "model.pt"
    SPM_FILE = "spm.model"

    def __init__(self, model: Seq2SeqTransformer, sp: spm.SentencePieceProcessor) -> None:
        self.model = model
        self.sp = sp

    @property
    def device(self) -> torch.device:
        return next(self.model.parameters()).device

    def encode_source(self, text: str) -> list[int]:
        """Source ids: pieces (truncated) followed by EOS."""
        return self.sp.encode(text)[: MAX_LENGTH - 1] + [EOS_ID]

    def encode_target(self, text: str) -> list[int]:
        """Target ids: BOS, pieces (truncated), EOS."""
        return [BOS_ID] + self.sp.encode(text)[: MAX_LENGTH - 2] + [EOS_ID]

    def decode_ids(self, ids: list[int]) -> str:
        """Turn generated ids back into text, stopping at the first EOS."""
        if EOS_ID in ids:
            ids = ids[: ids.index(EOS_ID)]
        return self.sp.decode([i for i in ids if i not in (PAD_ID, BOS_ID)]).strip()

    @torch.no_grad()
    def translate(
        self,
        texts: list[str],
        batch_size: int = 64,
        num_beams: int = 4,
        max_new_tokens: int = MAX_LENGTH,
        max_batch_tokens: int = 48_000,
    ) -> list[str]:
        """Translate English sentences, batching by length for efficiency.

        Sentences are sorted by length, longest first. Each batch holds at most
        ``batch_size`` sentences and is also capped so that
        ``num_beams x sentences x (source + output length)`` stays under
        ``max_batch_tokens``. That keeps GPU memory bounded on long inputs, such as
        news sentences, without slowing down short ones.
        """
        self.model.eval()
        encoded = [self.encode_source(text) for text in texts]
        order = sorted(range(len(texts)), key=lambda i: len(encoded[i]), reverse=True)
        outputs = [""] * len(texts)
        use_amp = self.device.type == "cuda"
        start = 0
        while start < len(order):
            longest = len(encoded[order[start]])  # sorted, so the first sentence is the longest
            tokens_per_sentence = num_beams * (longest + min(max_new_tokens, 2 * longest + 10))
            size = max(1, min(batch_size, max_batch_tokens // tokens_per_sentence))
            indices = order[start : start + size]
            src = pad_batch([encoded[i] for i in indices]).to(self.device)
            with torch.autocast("cuda", dtype=torch.float16, enabled=use_amp):
                generated = self.model.generate(src, num_beams=num_beams, max_new_tokens=max_new_tokens)
            for index, ids in zip(indices, generated[:, 1:].tolist()):
                outputs[index] = self.decode_ids(ids)
            start += size
        return outputs

    def save(self, directory: Path) -> None:
        """Save weights with ``torch.save`` plus the config and tokenizer."""
        directory.mkdir(parents=True, exist_ok=True)
        torch.save(self.model.state_dict(), directory / self.WEIGHTS_FILE)
        (directory / self.CONFIG_FILE).write_text(
            json.dumps(asdict(self.model.config), indent=2), encoding="utf-8"
        )

    @classmethod
    def load(cls, directory: Path, device: torch.device) -> ScratchTranslator:
        """Load a translator saved with :meth:`save` (weights via ``torch.load``)."""
        config = ScratchConfig(**json.loads((directory / cls.CONFIG_FILE).read_text(encoding="utf-8")))
        model = Seq2SeqTransformer(config)
        state = torch.load(directory / cls.WEIGHTS_FILE, map_location=device, weights_only=True)
        model.load_state_dict(state)
        sp = spm.SentencePieceProcessor(model_file=str(directory / cls.SPM_FILE))
        return cls(model.to(device).eval(), sp)

    @classmethod
    def is_scratch_dir(cls, path: str | Path) -> bool:
        """True if ``path`` contains a model saved by this class."""
        return (Path(path) / cls.CONFIG_FILE).is_file() and (Path(path) / cls.WEIGHTS_FILE).is_file()


def pad_batch(sequences: list[list[int]]) -> torch.Tensor:
    """Right-pad id lists with PAD into a (batch, max_len) tensor."""
    width = max(len(s) for s in sequences)
    batch = torch.full((len(sequences), width), PAD_ID, dtype=torch.long)
    for row, seq in enumerate(sequences):
        batch[row, : len(seq)] = torch.tensor(seq, dtype=torch.long)
    return batch
