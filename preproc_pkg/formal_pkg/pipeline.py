from typing import List
from .steps import FormalStep, RuleBasedFormalStep, TransformerFormalStep


class FormalPipeline:
    def __init__(self, steps: List[FormalStep]):
        self.steps = steps

    def __call__(self, text: str) -> str:
        for s in self.steps:
            text = s.apply(text)
        return text

    def __repr__(self):
        return (
            "FormalPipeline("
            + " → ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


def create_formal_pipeline(*, use_rules: bool = True, **kwargs) -> FormalPipeline:
    steps: List[FormalStep] = []
    if use_rules:
        steps.append(RuleBasedFormalStep())
    steps.append(TransformerFormalStep(**kwargs))
    return FormalPipeline(steps)
