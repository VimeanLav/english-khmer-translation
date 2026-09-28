"""Data pipeline for English -> Khmer translation with NLLB-200.

Downloads an English-Khmer parallel corpus from the Hugging Face Hub, cleans it,
creates deterministic 80/10/10 train/validation/test splits, tokenizes it with the
NLLB tokenizer and saves the result to ``data/processed/``.

Run from the project root:

    python -m src.data                       # full dataset
    python -m src.data --max-samples 20000   # small subset for quick experiments
"""

from __future__ import annotations

import argparse
from pathlib import Path

from datasets import Dataset, DatasetDict, load_dataset, load_from_disk
from transformers import AutoTokenizer, PreTrainedTokenizerBase

from src.config import (
    DATASET_NAME,
    LABEL_PAD_ID,
    MAX_LENGTH,
    MODEL_NAME,
    RAW_DIR,
    SEED,
    SRC_COLUMN,
    SRC_LANG,
    TGT_COLUMN,
    TGT_LANG,
    TOKENIZED_DIR,
)
from src.utils.seed import set_seed


def get_tokenizer(model_name_or_path: str | Path = MODEL_NAME) -> PreTrainedTokenizerBase:
    """Load the NLLB tokenizer configured for English -> Khmer.

    Args:
        model_name_or_path: Hub model id or local directory containing a tokenizer.

    Returns:
        A tokenizer that prefixes sources with ``eng_Latn`` and targets with ``khm_Khmr``.

    Raises:
        ValueError: If a language code is not a token in the vocabulary.
    """
    tokenizer = AutoTokenizer.from_pretrained(
        str(model_name_or_path), src_lang=SRC_LANG, tgt_lang=TGT_LANG
    )
    for code in (SRC_LANG, TGT_LANG):
        if tokenizer.convert_tokens_to_ids(code) == tokenizer.unk_token_id:
            raise ValueError(f"Language code {code!r} is not in the NLLB vocabulary.")
    return tokenizer


def clean_dataset(dataset: Dataset) -> Dataset:
    """Strip whitespace, drop empty pairs and de-duplicate English sources.

    De-duplicating on the source sentence guarantees that the same English
    sentence cannot appear in both the training and the test split.

    Args:
        dataset: Dataset with ``SRC_COLUMN`` and ``TGT_COLUMN`` text columns.

    Returns:
        The cleaned dataset.
    """
    df = dataset.to_pandas()
    for column in (SRC_COLUMN, TGT_COLUMN):
        df[column] = df[column].astype("string").str.strip()
    df = df.dropna(subset=[SRC_COLUMN, TGT_COLUMN])
    df = df[(df[SRC_COLUMN] != "") & (df[TGT_COLUMN] != "")]
    df = df.drop_duplicates(subset=[SRC_COLUMN], keep="first")
    return Dataset.from_pandas(df.astype(str), preserve_index=False)


def load_raw_dataset(
    dataset_name: str = DATASET_NAME,
    max_samples: int | None = None,
    seed: int = SEED,
) -> Dataset:
    """Download (or reuse the cached copy of) the parallel corpus and clean it.

    Args:
        dataset_name: Hugging Face dataset id with ``eng`` / ``kh`` columns.
        max_samples: Optional cap on the number of pairs, sampled randomly.
        seed: Random seed used when sub-sampling.

    Returns:
        A cleaned ``Dataset`` with only the source and target columns.
    """
    dataset = load_dataset(dataset_name, split="train", cache_dir=str(RAW_DIR))
    dataset = dataset.select_columns([SRC_COLUMN, TGT_COLUMN])
    dataset = clean_dataset(dataset)
    if max_samples is not None and max_samples < len(dataset):
        dataset = dataset.shuffle(seed=seed).select(range(max_samples))
    return dataset


def create_splits(dataset: Dataset, seed: int = SEED) -> DatasetDict:
    """Split a dataset into 80% train, 10% validation and 10% test.

    Args:
        dataset: The full cleaned dataset.
        seed: Random seed for reproducible splits.

    Returns:
        A ``DatasetDict`` with ``train``, ``validation`` and ``test`` splits.
    """
    train_rest = dataset.train_test_split(test_size=0.2, seed=seed)
    val_test = train_rest["test"].train_test_split(test_size=0.5, seed=seed)
    return DatasetDict(
        train=train_rest["train"],
        validation=val_test["train"],
        test=val_test["test"],
    )


def tokenize_splits(
    splits: DatasetDict,
    tokenizer: PreTrainedTokenizerBase,
    max_length: int = MAX_LENGTH,
    padding: bool | str = "max_length",
) -> DatasetDict:
    """Tokenize source and target text for sequence-to-sequence training.

    The raw ``eng`` / ``kh`` columns are kept so evaluation can use the original
    text; ``Seq2SeqTrainer`` drops them automatically during training.

    Args:
        splits: Dataset splits with raw text columns.
        tokenizer: NLLB tokenizer from :func:`get_tokenizer`.
        max_length: Maximum token length for both source and target.
        padding: ``"max_length"`` pads every example to ``max_length``;
            ``False`` leaves padding to the data collator (dynamic padding).

    Returns:
        Splits with ``input_ids``, ``attention_mask`` and ``labels`` added.
    """
    pad_id = tokenizer.pad_token_id

    def _preprocess(batch: dict[str, list[str]]) -> dict[str, list[list[int]]]:
        encoded = tokenizer(
            batch[SRC_COLUMN],
            text_target=batch[TGT_COLUMN],
            max_length=max_length,
            truncation=True,
            padding=padding,
        )
        if padding == "max_length":
            # Padded label positions must be ignored by the loss.
            encoded["labels"] = [
                [tok if tok != pad_id else LABEL_PAD_ID for tok in labels]
                for labels in encoded["labels"]
            ]
        return encoded

    return splits.map(_preprocess, batched=True, desc="Tokenizing")


def save_tokenized_datasets(datasets: DatasetDict, output_dir: Path = TOKENIZED_DIR) -> Path:
    """Save tokenized splits to disk.

    Args:
        datasets: Tokenized splits.
        output_dir: Destination directory.

    Returns:
        The directory the datasets were written to.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    datasets.save_to_disk(str(output_dir))
    return output_dir


def prepare_datasets(
    dataset_name: str = DATASET_NAME,
    max_samples: int | None = None,
    output_dir: Path = TOKENIZED_DIR,
    padding: bool | str = "max_length",
    seed: int = SEED,
) -> DatasetDict:
    """Run the full pipeline: load, clean, split, tokenize and save.

    Args:
        dataset_name: Hugging Face dataset id.
        max_samples: Optional cap on the number of pairs.
        output_dir: Where to save the tokenized splits.
        padding: Padding strategy passed to :func:`tokenize_splits`.
        seed: Random seed for sub-sampling and splitting.

    Returns:
        The tokenized ``DatasetDict``.
    """
    dataset = load_raw_dataset(dataset_name, max_samples=max_samples, seed=seed)
    splits = create_splits(dataset, seed=seed)
    tokenized = tokenize_splits(splits, get_tokenizer(), padding=padding)
    save_tokenized_datasets(tokenized, output_dir)
    return tokenized


def load_tokenized_datasets(
    input_dir: Path = TOKENIZED_DIR, auto_prepare: bool = True
) -> DatasetDict:
    """Load tokenized splits from disk, building them first if necessary.

    Args:
        input_dir: Directory written by :func:`save_tokenized_datasets`.
        auto_prepare: Run :func:`prepare_datasets` with default settings when
            ``input_dir`` does not exist yet.

    Returns:
        The tokenized ``DatasetDict``.

    Raises:
        FileNotFoundError: If the data is missing and ``auto_prepare`` is False.
    """
    if not input_dir.exists():
        if not auto_prepare:
            raise FileNotFoundError(
                f"No processed data at {input_dir}. Run `python -m src.data` first."
            )
        print(f"No processed data at {input_dir}; preparing it now...")
        return prepare_datasets(output_dir=input_dir)
    return load_from_disk(str(input_dir))


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dataset", default=DATASET_NAME, help="Hugging Face dataset id.")
    parser.add_argument("--max-samples", type=int, default=None, help="Cap on sentence pairs.")
    parser.add_argument("--output-dir", type=Path, default=TOKENIZED_DIR)
    parser.add_argument(
        "--dynamic-padding",
        action="store_true",
        help="Store unpadded sequences and let the collator pad each batch "
        "(much faster for short sentences than padding to 128).",
    )
    parser.add_argument("--seed", type=int, default=SEED)
    return parser.parse_args()


def main() -> None:
    """Prepare and save the tokenized English-Khmer datasets."""
    args = parse_args()
    set_seed(args.seed)
    tokenized = prepare_datasets(
        dataset_name=args.dataset,
        max_samples=args.max_samples,
        output_dir=args.output_dir,
        padding=False if args.dynamic_padding else "max_length",
        seed=args.seed,
    )
    for split, dataset in tokenized.items():
        print(f"{split:>10}: {len(dataset):,} examples")
    print(f"Saved tokenized datasets to {args.output_dir}")


if __name__ == "__main__":
    main()
