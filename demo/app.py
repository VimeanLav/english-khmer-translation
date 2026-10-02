"""Streamlit web demo: translate English to Khmer with the trained models.

Run from the project root:

    python -m streamlit run demo/app.py

Then open the address it prints (usually http://localhost:8501).
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

# Make the project's `src` package importable when Streamlit runs this file.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st  # noqa: E402
import torch  # noqa: E402

from src.config import APPROACHES  # noqa: E402
from src.evaluate import load_nllb, resolve_model_path, translate_nllb  # noqa: E402
from src.model_scratch import ScratchTranslator  # noqa: E402

EXAMPLES = [
    "I want to eat papaya salad.",
    "Where is the nearest hospital?",
    "The weather is very hot today.",
    "My mother is cooking dinner.",
    "Please ensure to take this antibiotic every hour.",
]


def available_approaches() -> list[str]:
    """Approaches whose model can be loaded on this machine."""
    keys = []
    for key, approach in APPROACHES.items():
        if not approach.trained or Path(resolve_model_path(approach.model_path)).is_dir():
            keys.append(key)
    return keys


def test_score(key: str) -> float | None:
    """Test-set chrF++ of an approach, from results/<approach>_results.json."""
    path = APPROACHES[key].results_path
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))["chrf++"]
    return None


@st.cache_resource(show_spinner="Loading model…")
def load_model(key: str):
    """Load a model once and keep it in memory for later requests."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_path = resolve_model_path(APPROACHES[key].model_path)
    if ScratchTranslator.is_scratch_dir(model_path):
        return ScratchTranslator.load(Path(model_path), device)
    return load_nllb(model_path, device)


def translate(key: str, sentences: list[str], num_beams: int) -> list[str]:
    """Translate sentences with one approach."""
    model = load_model(key)
    if isinstance(model, ScratchTranslator):
        return model.translate(sentences, num_beams=num_beams)
    nllb, tokenizer = model
    return translate_nllb(sentences, nllb, tokenizer, num_beams=num_beams)


st.set_page_config(page_title="English → Khmer Translator", page_icon="🇰🇭", layout="wide")
st.title("English → Khmer Translator")
st.caption("Deep Learning final project · compare the trained approaches on your own sentences")

# ---- Sidebar: model choice and decoding settings ---------------------------------
available = available_approaches()
with st.sidebar:
    st.header("Models")
    default = [k for k in ("frozen",) if k in available]
    chosen = st.multiselect(
        "Approaches to compare",
        options=available,
        default=default,
        format_func=lambda k: APPROACHES[k].label,
    )
    missing = [APPROACHES[k].label for k in APPROACHES if k not in available]
    if missing:
        st.caption("Not on this PC (download into `models/` to enable): " + ", ".join(missing))
    num_beams = st.slider("Beam size", min_value=1, max_value=8, value=4,
                          help="4 is the setting used for all test-set results.")
    st.divider()
    st.caption(f"Device: {'GPU · ' + torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")

# ---- Input -----------------------------------------------------------------------
if "text" not in st.session_state:
    st.session_state.text = EXAMPLES[0]

st.write("**Examples:**")
columns = st.columns(len(EXAMPLES))
for column, example in zip(columns, EXAMPLES):
    if column.button(example, width="stretch"):
        st.session_state.text = example

text = st.text_area("English (one sentence per line)", key="text", height=120)
sentences = [line.strip() for line in text.splitlines() if line.strip()]

# ---- Translation -----------------------------------------------------------------
if st.button("Translate", type="primary", disabled=not (sentences and chosen)):
    with st.spinner("Translating…"):
        outputs = {key: translate(key, sentences, num_beams) for key in chosen}
    for i, sentence in enumerate(sentences):
        st.subheader(sentence)
        for key in chosen:
            score = test_score(key)
            label = APPROACHES[key].label + (f" · test chrF++ {score:.2f}" if score is not None else "")
            st.markdown(f"<small>{html.escape(label)}</small>", unsafe_allow_html=True)
            st.markdown(
                f"<div style='font-size:1.6rem; line-height:2.4rem'>{html.escape(outputs[key][i])}</div>",
                unsafe_allow_html=True,
            )
        st.divider()
elif not chosen:
    st.info("Choose at least one model in the sidebar.")
