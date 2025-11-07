from typing import List
from .steps import LemmaStep, HazmLemmaStep, ParsivarLemmaStep, CombinedLemmaStep


class LemmaPipeline:
    def __init__(self, steps: List[LemmaStep]):
        self.steps = steps

    def __call__(self, text: str) -> str:
        for s in self.steps:
            text = s.apply(text)
        return text

    def __repr__(self):
        return (
            "LemmaPipeline("
            + " -> ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


def create_lemma_pipeline(
    *, use_hazm: bool = True, use_parsivar: bool = True, prefer_past: bool = False
) -> LemmaPipeline:
    """
    Build a lemmatization pipeline.

    Parameters
    ----------
    use_hazm : bool
        Enable Hazm lemmatizer.
    use_parsivar : bool
        Enable Parsivar stems as a proxy for lemmas.
    prefer_past : bool
        If True, choose past form for verbs; otherwise present.

    Returns
    -------
    LemmaPipeline
    """
    steps: List[LemmaStep] = []
    if use_hazm and use_parsivar:
        steps.append(CombinedLemmaStep(prefer_past=prefer_past))
    elif use_hazm:
        steps.append(HazmLemmaStep(prefer_past=prefer_past))
    elif use_parsivar:
        steps.append(ParsivarLemmaStep(prefer_past=prefer_past))
    else:
        raise ValueError("At least one of use_hazm or use_parsivar must be True.")
    return LemmaPipeline(steps)
