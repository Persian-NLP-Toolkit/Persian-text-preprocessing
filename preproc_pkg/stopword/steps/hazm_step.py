from __future__ import annotations
from typing import Set, List, Optional
from hazm import word_tokenize, stopwords_list
from .base import StopwordStep
from ...utils.constants import PUNCT
from ...utils.textutils import detokenize


class HazmStopwordStep(StopwordStep):
    """Remove stopwords using Hazm's list (with optional extras)."""

    def __init__(self, extra: Optional[List[str]] = None):
        base: Set[str] = set(stopwords_list())
        if extra:
            base.update(extra)
        self.stopwords = base

    def apply(self, text: str) -> str:
        tokens: List[str] = word_tokenize(text)
        kept: List[str] = [t for t in tokens if t not in self.stopwords]
        return detokenize(kept, PUNCT)
