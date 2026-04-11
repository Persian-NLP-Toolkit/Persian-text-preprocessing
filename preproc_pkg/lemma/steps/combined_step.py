from __future__ import annotations
from typing import List
from hazm import Lemmatizer, word_tokenize
from parsivar import FindStems
from .base import LemmaStep
from ...utils.constants import SPLIT_RE, PUNCT
from ...utils.textutils import detokenize


class CombinedLemmaStep(LemmaStep):
    """Hazm first; if unchanged, fallback Parsivar. Pick present/past for verbs."""

    def __init__(self, *, prefer_past: bool = False):
        self._hz = Lemmatizer()
        self._pv = FindStems()
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
            hz = self._hz.lemmatize(t)
            chosen = self._pick(hz)
            if chosen != t or SPLIT_RE.search(hz):
                out_tokens.append(chosen)
            else:
                pv = self._pv.convert_to_stem(t)
                out_tokens.append(self._pick(pv))
        return detokenize(out_tokens, PUNCT)
