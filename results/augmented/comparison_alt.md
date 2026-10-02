| Approach | chrF++ ↑ | chrF ↑ | BLEU ↑ | Trainable params | Train steps | Train time | s / step | Peak VRAM | GPU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Zero-shot NLLB-600M (reference) | 36.06 | 45.46 | 8.88 | 0 / – | – | – | – | – | – |
| A: Transformer from scratch | 33.46 | 42.02 | 21.24 | 11.5M / 11.5M | 36615 | 1:11:33 | 0.1172 | 4.53 GB | Tesla T4 |
| **B: NLLB frozen backbone** | 42.56 | 52.67 | 32.38 | 50.4M / 615.1M | 16000 | 1:09:50 | 0.2619 | 7.13 GB | Tesla T4 |
| C: NLLB full fine-tuning | 41.61 | 51.46 | 31.13 | 615.1M / 615.1M | 2000 | 0:30:19 | 0.9096 | 8.15 GB | Tesla T4 |

*Test set: the same 1,018 out-of-domain ALT news test sentences for every approach, beam search with 4 beams. BLEU uses sacrebleu's `flores200` SentencePiece tokenizer (spBLEU). Train time counts optimizer steps only (no evaluation or checkpointing). Params are trainable / total.*
