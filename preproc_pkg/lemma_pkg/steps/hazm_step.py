from __future__ import annotations
from typing import List
from hazm import Lemmatizer, word_tokenize
from .base import LemmaStep
from ...utils.constants import SPLIT_RE, PUNCT
from ...utils.textutils import detokenize


class HazmLemmaStep(LemmaStep):
    """Lemmatize using Hazm; for verbs pick present (default) or past."""

    def __init__(self, *, prefer_past: bool = False):
        self.lemmatizer = Lemmatizer()
        self._past = prefer_past

    def _pick(self, s: str) -> str:
        parts = SPLIT_RE.split(s)
        if len(parts) > 1:
            return parts[0] if self._past else parts[1]
        return s

    def apply(self, text: str) -> str:
        toks: List[str] = word_tokenize(text)
        out_tokens: List[str] = [self._pick(self.lemmatizer.lemmatize(t)) for t in toks]
        return detokenize(out_tokens, PUNCT)
