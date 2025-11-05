from __future__ import annotations
from typing import Set, List, Optional
from hazm import word_tokenize, stopwords_list
from .base import StopwordStep


class HazmStopwordStep(StopwordStep):
    """Remove stopwords using Hazm's list (with optional extras)."""

    def __init__(self, extra: Optional[List[str]] = None):
        base: Set[str] = set(stopwords_list())
        if extra:
            base.update(extra)
        self.stopwords = base
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
        tokens: List[str] = word_tokenize(text)
        kept: List[str] = [t for t in tokens if t not in self.stopwords]
        out = ""
        for t in kept:
            if t in self._punct:
                out = out.rstrip() + t
            else:
                out += " " + t
        return out.strip()


# from __future__ import annotations
# from typing import Set, List, Optional
# from hazm import word_tokenize, stopwords_list
# from .base import StopwordStep


# class HazmStopwordStep(StopwordStep):
#     """Remove stopwords using Hazm's stopword list (with optional extra words)."""

#     def __init__(self, extra: Optional[List[str]] = None):
#         # Prepare a set of stop words for fast lookup
#         base_stopwords: Set[str] = set(stopwords_list())
#         if extra:
#             base_stopwords.update(extra)
#         self.stopwords = base_stopwords

#         # Common punctuation characters in Persian to handle spacing
#         self.punct_set = {
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
#         }

#     def apply(self, text: str) -> str:
#         # Tokenize the text into words (Hazm handles punctuation as separate tokens)
#         tokens: List[str] = word_tokenize(text)
#         filtered_tokens: List[str] = []
#         for token in tokens:
#             # If token is word and in stopwords list, skip it; always keep punctuation
#             if token in self.stopwords:
#                 continue
#             filtered_tokens.append(token)
#         # Rejoin tokens into text, ensuring no extra space before punctuation
#         output = ""
#         for token in filtered_tokens:
#             if token in self.punct_set:
#                 # Attach punctuation directly to the output (remove trailing space if any)
#                 output = output.rstrip() + token
#             else:
#                 output += " " + token
#         return output.strip()
