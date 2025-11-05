from __future__ import annotations
from typing import List
import re
from hazm import Lemmatizer, word_tokenize
from parsivar import FindStems
from .base import LemmaStep

_SPLIT = re.compile(r"[#&|/]+")


class CombinedLemmaStep(LemmaStep):
    """Hazm first; if unchanged, fallback Parsivar. Pick present/past for verbs."""

    def __init__(self, *, prefer_past: bool = False):
        self._hz = Lemmatizer()
        self._pv = FindStems()
        self._past = prefer_past
        self._punct = {
            "،",
            ".",
            "!",
            "؟",
            "؛",
            ":",
            "…",
            "»",
            "«",
            "(",
            ")",
            "[",
            "]",
            ",",
            "؛",
        }

    def _pick(self, s: str) -> str:
        parts = _SPLIT.split(s)
        if len(parts) > 1:
            return parts[0] if self._past else parts[1]
        return s

    def apply(self, text: str) -> str:
        toks: List[str] = word_tokenize(text)
        out_tokens: List[str] = []
        for t in toks:
            hz = self._hz.lemmatize(t)
            chosen = self._pick(hz)
            if chosen != t or _SPLIT.search(hz):
                out_tokens.append(chosen)
            else:
                pv = self._pv.convert_to_stem(t)
                out_tokens.append(self._pick(pv))
        out = ""
        for tok in out_tokens:
            out = (out.rstrip() + tok) if tok in self._punct else (out + " " + tok)
        return out.strip()
