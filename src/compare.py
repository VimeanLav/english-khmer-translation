"""Build the single side-by-side results table for all approaches.

Combines each approach's test metrics (``results/<approach>_results.json``) with
its training summary (``results/<approach>_train_summary.json``) and writes:

* ``results/comparison.csv``: machine-readable.
* ``results/comparison.md``: the Markdown table to paste into the README.

The script refuses to compare results produced on different test subsets or
with different decoding settings, because that would make the comparison unfair.

Run from the project root:

    python -m src.compare
"""

from __future__ import annotations

import csv

from src.config import APPROACHES, RESULTS_DIR
from src.utils.reporting import load_json


def fmt_params(n: int | None) -> str:
    """Human-readable parameter count, e.g. 615.1M."""
    if n is None:
        return "–"
    if n == 0:
        return "0"
    return f"{n / 1e6:.1f}M" if n >= 1e6 else f"{n / 1e3:.0f}K"


def fmt_duration(seconds: float | None) -> str:
    """Seconds as h:mm:ss."""
    if seconds is None:
        return "–"
    s = int(round(seconds))
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"


def main() -> None:
    """Assemble and save the comparison table."""
    rows = []
    for key, approach in APPROACHES.items():
        if not approach.results_path.is_file():
            print(f"Skipping {key}: {approach.results_path.name} not found.")
            continue
        test = load_json(approach.results_path)
        train = load_json(approach.summary_path) if approach.summary_path.is_file() else {}
        hw = train.get("hardware", {})
        rows.append({
            "approach": approach.label,
            "test_chrf++": test["chrf++"],
            "test_chrf": test["chrf"],
            "test_bleu": test["bleu"],
            "trainable_params": train.get("trainable_params", 0 if not approach.trained else None),
            "total_params": train.get("total_params"),
            "train_steps": train.get("steps_completed"),
            "examples_seen": train.get("examples_seen"),
            "train_time_s": train.get("train_step_seconds"),
            "wall_time_s": train.get("wall_seconds"),
            "seconds_per_step": train.get("seconds_per_step"),
            "peak_vram_gb": train.get("peak_vram_gb"),
            "gpu": hw.get("gpu"),
            "best_val_chrf++": train.get("val_metrics", {}).get("chrf++"),
            "test_sentences": test["num_samples"],
            "num_beams": test["num_beams"],
            "inference_s": test["inference_seconds"],
        })
    if not rows:
        raise SystemExit("No results found. Run `python -m src.evaluate --approach ...` first.")

    protocols = {(r["test_sentences"], r["num_beams"]) for r in rows}
    if len(protocols) > 1:
        raise SystemExit(
            f"Unfair comparison: results use different (test sentences, beams) settings {protocols}. "
            "Re-run src.evaluate with the same settings for every approach."
        )

    csv_path = RESULTS_DIR / "comparison.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    n_test, beams = protocols.pop()
    best = max((r for r in rows if r["trainable_params"]), key=lambda r: r["test_chrf++"], default=None)
    header = (
        "| Approach | chrF++ ↑ | chrF ↑ | BLEU ↑ | Trainable params | Train steps "
        "| Train time | s / step | Peak VRAM | GPU |\n"
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|\n"
    )
    lines = []
    for r in rows:
        name = f"**{r['approach']}**" if r is best else r["approach"]
        lines.append(
            f"| {name} | {r['test_chrf++']:.2f} | {r['test_chrf']:.2f} | {r['test_bleu']:.2f} "
            f"| {fmt_params(r['trainable_params'])} / {fmt_params(r['total_params'])} "
            f"| {r['train_steps'] if r['train_steps'] is not None else '–'} "
            f"| {fmt_duration(r['train_time_s'])} "
            f"| {r['seconds_per_step'] if r['seconds_per_step'] is not None else '–'} "
            f"| {str(r['peak_vram_gb']) + ' GB' if r['peak_vram_gb'] else '–'} "
            f"| {r['gpu'] or '–'} |"
        )
    note = (
        f"\n*Test set: the same {n_test:,} held-out sentences for every approach, beam search "
        f"with {beams} beams. BLEU uses sacrebleu's `flores200` SentencePiece tokenizer (spBLEU). "
        "Train time counts optimizer steps only (no evaluation or checkpointing). "
        "Params are trainable / total.*\n"
    )
    md_path = RESULTS_DIR / "comparison.md"
    md_path.write_text(header + "\n".join(lines) + "\n" + note, encoding="utf-8")
    print(header + "\n".join(lines) + "\n" + note)
    print(f"Saved {csv_path} and {md_path}")


if __name__ == "__main__":
    main()
