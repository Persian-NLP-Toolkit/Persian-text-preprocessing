from typing import List
from .steps import SpellStep, ParsivarSpellStep, TransformerSpellStep


class SpellPipeline:
    def __init__(self, steps: List[SpellStep]):
        self.steps = steps

    def __call__(self, text: str) -> str:
        for s in self.steps:
            text = s.apply(text)
        return text

    def __repr__(self):
        return (
            "SpellPipeline("
            + " → ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


def create_spell_pipeline(*, use_transformer: bool = False, **kwargs) -> SpellPipeline:
    steps: List[SpellStep] = [ParsivarSpellStep()]
    if use_transformer:
        steps.append(TransformerSpellStep(**kwargs))
    return SpellPipeline(steps)
