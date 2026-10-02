| Approach | chrF++ ↑ | chrF ↑ | BLEU ↑ | Trainable params | Train steps | Train time | s / step | Peak VRAM | GPU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Zero-shot NLLB-600M (reference) | 36.06 | 45.46 | 8.88 | 0 / – | – | – | – | – | – |
| A: Transformer from scratch | 3.81 | 5.09 | 0.17 | 11.5M / 11.5M | 30345 | 0:21:45 | 0.043 | 1.63 GB | Tesla T4 |
| **B: NLLB frozen backbone** | 34.49 | 44.24 | 21.18 | 50.4M / 615.1M | 16000 | 1:01:34 | 0.2309 | 5.18 GB | NVIDIA GeForce RTX 4070 Laptop GPU |
| C: NLLB full fine-tuning | 34.10 | 43.79 | 19.70 | 615.1M / 615.1M | 2000 | 0:27:32 | 0.8263 | 6.66 GB | Tesla T4 |

*Test set: the same 1,018 out-of-domain ALT news test sentences for every approach, beam search with 4 beams. BLEU uses sacrebleu's `flores200` SentencePiece tokenizer (spBLEU). Train time counts optimizer steps only (no evaluation or checkpointing). Params are trainable / total.*
