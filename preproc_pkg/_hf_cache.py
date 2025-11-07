"""Tiny, process-local caches for HuggingFace models/pipelines."""

from functools import lru_cache
from typing import Tuple, Any
from transformers import AutoTokenizer, T5ForConditionalGeneration, pipeline


@lru_cache(maxsize=8)
def load_t5(
    model_name: str, device: str = "cpu"
) -> Tuple[Any, T5ForConditionalGeneration]:
    """Load a T5 tokenizer+model once per process for a specific device; returns (tokenizer, model)."""
    tok = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    if device:
        model.to(device)
    model.eval()
    return tok, model


@lru_cache(maxsize=8)
def get_text2text_pipeline(model_name: str, device: int = -1):
    """Cache a text2text-generation pipeline (Seq2Seq only) by (model, device)."""
    return pipeline("text2text-generation", model=model_name, device=device)
