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


_MI = re.compile(r"(?<!\S)(ن?می)\s+(?=[اآءئأإآبتثجچحخدذرزسشصضطظعغفقکگلمنوهی])")


def _orthography_tidy(s: str) -> str:
    return _MI.sub(r"\1‌", s)


def create_formal_pipeline(*, use_rules: bool = True, **kwargs) -> FormalPipeline:
    """
    Build an informal->formal pipeline.

    Parameters
    ----------
    use_rules : bool
        If True, apply a fast rule-based pass before the transformer (recommended).
    **kwargs :
        Forwarded to TransformerFormalStep (e.g., model_name, device, generate_kwargs).

    Returns
    -------
    FormalPipeline
    """
    steps: List[FormalStep] = []
    if use_rules:
        steps.append(RuleBasedFormalStep())
    steps.append(TransformerFormalStep(**kwargs))
    return FormalPipeline(steps)
