| Approach | chrF++ ↑ | chrF ↑ | BLEU ↑ | Trainable params | Train steps | Train time | s / step | Peak VRAM | GPU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Zero-shot NLLB-600M (reference) | 40.53 | 50.31 | 13.69 | 0 / – | – | – | – | – | – |
| A: Transformer from scratch | 99.13 | 99.16 | 98.86 | 11.5M / 11.5M | 30345 | 0:21:45 | 0.043 | 1.63 GB | Tesla T4 |
| **B: NLLB frozen backbone** | 99.31 | 99.45 | 99.21 | 50.4M / 615.1M | 16000 | 1:01:34 | 0.2309 | 5.18 GB | NVIDIA GeForce RTX 4070 Laptop GPU |
| C: NLLB full fine-tuning | 98.42 | 98.71 | 98.09 | 615.1M / 615.1M | 2000 | 0:27:32 | 0.8263 | 6.66 GB | Tesla T4 |

*Test set: the same 5,000 held-out sentences for every approach, beam search with 4 beams. BLEU uses sacrebleu's `flores200` SentencePiece tokenizer (spBLEU). Train time counts optimizer steps only (no evaluation or checkpointing). Params are trainable / total.*
