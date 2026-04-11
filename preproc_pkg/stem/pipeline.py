from typing import List
from .steps import StemStep, HazmStemStep, ParsivarStemStep, CombinedStemStep


class StemPipeline:
    def __init__(self, steps: List[StemStep]):
        self.steps = steps

    def __call__(self, text: str) -> str:
        for s in self.steps:
            text = s.apply(text)
        return text

    def __repr__(self):
        return (
            "StemPipeline("
            + " -> ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


def create_stem_pipeline(
    *, use_hazm: bool = True, use_parsivar: bool = True, prefer_past: bool = False
) -> StemPipeline:
    """
    Build a stemming pipeline.

    Parameters
    ----------
    use_hazm : bool
        If True, enable Hazm stemmer.
    use_parsivar : bool
        If True, enable Parsivar stems (present/past split aware).
    prefer_past : bool
        If True, pick the past stem for verbs, else present.

    Returns
    -------
    StemPipeline
    """
    steps: List[StemStep] = []
    if use_hazm and use_parsivar:
        steps.append(CombinedStemStep(prefer_past=prefer_past))
    elif use_parsivar:
        steps.append(ParsivarStemStep(prefer_past=prefer_past))
    elif use_hazm:
        steps.append(HazmStemStep())
    else:
        raise ValueError("At least one of use_hazm or use_parsivar must be True.")
    return StemPipeline(steps)
