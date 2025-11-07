from __future__ import annotations

import re
from typing import List, Tuple
from .base import FormalStep

COMMON = {
    r"\bمیخوام\b": "می‌خواهم",
    r"\bمی‌خوای\b": "می‌خواهی",
    r"\bمی‌خواد\b": "می‌خواهد",
    r"\bمی‌خوایم\b": "می‌خواهیم",
    r"\bمی‌خوان\b": "می‌خوانند",
    r"\bدوستام\b": "دوستانم",
    r"\bخوش‌تون\b": "خوش‌تان",
}


class RuleBasedFormalStep(FormalStep):
    """Fast regex substitution for high-frequency colloquialisms."""

    def __init__(self, extra: dict[str, str] | None = None):
        rules = COMMON.copy()
        if extra:
            rules.update(extra)
        self.patterns: List[Tuple[re.Pattern[str], str]] = [
            (re.compile(pat), repl) for pat, repl in rules.items()
        ]

    def apply(self, text: str) -> str:
        for pat, repl in self.patterns:
            text = pat.sub(repl, text)
        return text
