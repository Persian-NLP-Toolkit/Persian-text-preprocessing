from typing import List
from .steps import FormalStep, RuleBasedFormalStep, TransformerFormalStep
import re


class FormalPipeline:
    def __init__(self, steps: List[FormalStep]):
        self.steps = steps

    def __call__(self, text: str) -> str:
        for s in self.steps:
            text = s.apply(text)
        return _orthography_tidy(text)

    def __repr__(self):
        return (
            "FormalPipeline("
            + " -> ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


_PERS_LET = r"[اآءئأإآبتثجچحخدذرزسشصضطظعغفقکگلمنوهی]"

_MI_SPACE = re.compile(rf"(?<!\S)(ن?می)\s+(?={_PERS_LET})")
_MI_JOIN = re.compile(rf"(?<!\S)(ن?می)(?={_PERS_LET})(?!\u200c)")
_MI_AFTER_OPEN = re.compile(rf"(?<=[«\(\[])(ن?می)(?={_PERS_LET})(?!\u200c)")


def _orthography_tidy(s: str) -> str:
    s = _MI_SPACE.sub("\\1\u200c", s)  # \1 + ZWNJ
    s = _MI_JOIN.sub("\\1\u200c", s)
    s = _MI_AFTER_OPEN.sub("\\1\u200c", s)
    return s


def create_formal_pipeline(*, use_rules: bool = True, **kwargs) -> FormalPipeline:
    steps: List[FormalStep] = []
    if use_rules:
        steps.append(RuleBasedFormalStep())
    steps.append(TransformerFormalStep(**kwargs))
    return FormalPipeline(steps)
