from __future__ import annotations
from typing import List
from hazm import Stemmer, word_tokenize
from .base import StemStep


class HazmStemStep(StemStep):
    def __init__(self):
        self._hz = Stemmer()
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

    def apply(self, text: str) -> str:
        toks: List[str] = word_tokenize(text)
        stems = [self._hz.stem(t) for t in toks]
        out = ""
        for t in stems:
            if t in self._punct:
                out = out.rstrip() + t
            else:
                out += " " + t
        return out.strip()
