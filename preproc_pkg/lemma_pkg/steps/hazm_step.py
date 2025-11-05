from __future__ import annotations
from typing import List
import re
from hazm import Lemmatizer, word_tokenize
from .base import LemmaStep

_SPLIT = re.compile(r"[#&|/]+")


class HazmLemmaStep(LemmaStep):
    """Lemmatize using Hazm; for verbs pick present (default) or past."""

    def __init__(self, *, prefer_past: bool = False):
        self.lemmatizer = Lemmatizer()
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
            # parts[0]=past, parts[1]=present
            return parts[0] if self._past else parts[1]
        return s

    def apply(self, text: str) -> str:
        toks: List[str] = word_tokenize(text)
        out_tokens: List[str] = []
        for t in toks:
            l = self.lemmatizer.lemmatize(t)
            out_tokens.append(self._pick(l))
        out = ""
        for tok in out_tokens:
            out = (out.rstrip() + tok) if tok in self._punct else (out + " " + tok)
        return out.strip()
