from __future__ import annotations
from typing import List
import re
from parsivar import FindStems
from hazm import Stemmer, word_tokenize
from .base import StemStep

_SPLIT = re.compile(r"[#&|/]+")


class CombinedStemStep(StemStep):
    """Parsivar primary (choose present/past), Hazm fallback if no change."""

    def __init__(self, *, prefer_past: bool = False):
        self._pv = FindStems()
        self._hz = Stemmer()
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
            s = self._pv.convert_to_stem(t)
            chosen = self._pick(s)
            if chosen == t:
                chosen = self._hz.stem(t)
            out_tokens.append(chosen)
        out = ""
        for tok in out_tokens:
            out = (out.rstrip() + tok) if tok in self._punct else (out + " " + tok)
        return out.strip()


# from __future__ import annotations
# from typing import List
# from parsivar import FindStems
# from hazm import Stemmer, word_tokenize
# from .base import StemStep


# class CombinedStemStep(StemStep):
#     """Parsivar primary, Hazm fallback; verbs -> first part before '#'."""

#     def __init__(self):
#         self._pv = FindStems()
#         self._hz = Stemmer()
#         self._punct = {
#             "،",
#             ".",
#             "!",
#             "؟",
#             "؛",
#             ":",
#             "…",
#             "»",
#             "«",
#             "(",
#             ")",
#             "[",
#             "]",
#             ",",
#             "؛",
#         }

#     def apply(self, text: str) -> str:
#         toks: List[str] = word_tokenize(text)
#         out_tokens: List[str] = []
#         for t in toks:
#             if not t or t.isdigit():
#                 out_tokens.append(t)
#                 continue
#             s = self._pv.convert_to_stem(t)
#             if "#" in s:
#                 s = s.split("#")[0]
#             if s == t:  # no change by Parsivar → try Hazm
#                 s = self._hz.stem(t)
#             out_tokens.append(s)
#         out = ""
#         for t in out_tokens:
#             if t in self._punct:
#                 out = out.rstrip() + t
#             else:
#                 out += " " + t
#         return out.strip()
