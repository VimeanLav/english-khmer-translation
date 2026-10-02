| Approach | chrF++ ↑ | chrF ↑ | BLEU ↑ | Trainable params | Train steps | Train time | s / step | Peak VRAM | GPU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Zero-shot NLLB-600M (reference) | 40.53 | 50.31 | 13.69 | 0 / – | – | – | – | – | – |
| **A: Transformer from scratch** | 99.79 | 99.83 | 99.77 | 11.5M / 11.5M | 36615 | 1:11:33 | 0.1172 | 4.53 GB | Tesla T4 |
| B: NLLB frozen backbone | 98.41 | 98.72 | 98.25 | 50.4M / 615.1M | 16000 | 1:09:50 | 0.2619 | 7.13 GB | Tesla T4 |
| C: NLLB full fine-tuning | 96.78 | 97.32 | 95.76 | 615.1M / 615.1M | 2000 | 0:30:19 | 0.9096 | 8.15 GB | Tesla T4 |

*Test set: the same 5,000 in-domain SeyhaLite test sentences for every approach, beam search with 4 beams. BLEU uses sacrebleu's `flores200` SentencePiece tokenizer (spBLEU). Train time counts optimizer steps only (no evaluation or checkpointing). Params are trainable / total.*
