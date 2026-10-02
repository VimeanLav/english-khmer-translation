# Experiment 1 vs. experiment 2


## In-domain test (SeyhaLite, 5,000)

| Approach | chrF++ Exp. 1 | chrF++ Exp. 2 | Δ chrF++ | BLEU Exp. 1 | BLEU Exp. 2 | Δ BLEU |
|---|---:|---:|---:|---:|---:|---:|
| Zero-shot NLLB-600M (reference) | 40.53 | 40.53 | +0.00 | 13.69 | 13.69 | +0.00 |
| A: Transformer from scratch | 99.13 | 99.79 | +0.66 | 98.86 | 99.77 | +0.91 |
| B: NLLB frozen backbone | 99.31 | 98.41 | -0.90 | 99.21 | 98.25 | -0.96 |
| C: NLLB full fine-tuning | 98.42 | 96.78 | -1.64 | 98.09 | 95.76 | -2.33 |

## Out-of-domain test (ALT news, 1,018)

| Approach | chrF++ Exp. 1 | chrF++ Exp. 2 | Δ chrF++ | BLEU Exp. 1 | BLEU Exp. 2 | Δ BLEU |
|---|---:|---:|---:|---:|---:|---:|
| Zero-shot NLLB-600M (reference) | 36.06 | 36.06 | +0.00 | 8.88 | 8.88 | +0.00 |
| A: Transformer from scratch | 3.81 | 33.46 | +29.65 | 0.17 | 21.24 | +21.07 |
| B: NLLB frozen backbone | 34.49 | 42.56 | +8.07 | 21.18 | 32.38 | +11.20 |
| C: NLLB full fine-tuning | 34.10 | 41.61 | +7.51 | 19.70 | 31.13 | +11.43 |

*Experiment 1 trains on SeyhaLite only; experiment 2 adds ALT (professional news translations, repeated 3×) with the same hyperparameters and step budgets. The zero-shot reference is not trained, so it is identical in both experiments.*
