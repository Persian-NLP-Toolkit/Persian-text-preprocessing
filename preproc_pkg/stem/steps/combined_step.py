from __future__ import annotations
from typing import List
from parsivar import FindStems
from hazm import Stemmer, word_tokenize
from .base import StemStep
from ...utils.constants import SPLIT_RE, PUNCT
from ...utils.textutils import detokenize


class CombinedStemStep(StemStep):
    """Parsivar primary (choose present/past), Hazm fallback if no change."""

    def __init__(self, *, prefer_past: bool = False):
        self._pv = FindStems()
        self._hz = Stemmer()
        self._past = prefer_past

    def _pick(self, s: str) -> str:
        parts = SPLIT_RE.split(s)
        if len(parts) > 1:
            return parts[0] if self._past else parts[1]
        return s

    def apply(self, text: str) -> str:
        toks: List[str] = word_tokenize(text)
        out_tokens: List[str] = []
        for t in toks:
            s = self._pv.convert_to_stem(t)
            chosen = self._pick(s)
            if chosen == t:
                chosen = self._hz.stem(t)
            out_tokens.append(chosen)
        return detokenize(out_tokens, PUNCT)
