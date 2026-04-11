from __future__ import annotations
from typing import List
from hazm import Stemmer, word_tokenize
from .base import StemStep
from ...utils.constants import PUNCT
from ...utils.textutils import detokenize


class HazmStemStep(StemStep):
    def __init__(self):
        self._hz = Stemmer()

    def apply(self, text: str) -> str:
        toks: List[str] = word_tokenize(text)
        stems = [self._hz.stem(t) for t in toks]
        return detokenize(stems, PUNCT)
