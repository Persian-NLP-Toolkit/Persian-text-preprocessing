from __future__ import annotations
from typing import List
import re
from parsivar import FindStems
from hazm import word_tokenize
from .base import LemmaStep

_SPLIT = re.compile(r"[#&|/]+")


class ParsivarLemmaStep(LemmaStep):
    """Approximate lemma via Parsivar; choose present/past stems for verbs."""

    def __init__(self, *, prefer_past: bool = False):
        self._st = FindStems()
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
        lems: List[str] = []
        for t in toks:
            s = self._st.convert_to_stem(t)
            lems.append(self._pick(s))
        out = ""
        for tok in lems:
            out = (out.rstrip() + tok) if tok in self._punct else (out + " " + tok)
        return out.strip()
