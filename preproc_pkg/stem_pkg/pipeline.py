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
            "StemPipeline(" + " → ".join(s.__class__.__name__ for s in self.steps) + ")"
        )


def create_stem_pipeline(
    *, use_hazm: bool = True, use_parsivar: bool = True, prefer_past: bool = False
) -> StemPipeline:
    """
    prefer_past=False (default): return PRESENT stem.
    prefer_past=True: return PAST stem.
    """
    steps: List[StemStep] = []
    if use_hazm and use_parsivar:
        steps.append(CombinedStemStep(prefer_past=prefer_past))
    elif use_parsivar:
        steps.append(ParsivarStemStep(prefer_past=prefer_past))
    elif use_hazm:
        steps.append(HazmStemStep())  # Hazm stemmer تک‌خروجیه
    else:
        raise ValueError("At least one of use_hazm or use_parsivar must be True.")
    return StemPipeline(steps)


# from typing import List
# from .steps import StemStep, HazmStemStep, ParsivarStemStep, CombinedStemStep


# class StemPipeline:
#     def __init__(self, steps: List[StemStep]):
#         self.steps = steps

#     def __call__(self, text: str) -> str:
#         for s in self.steps:
#             text = s.apply(text)
#         return text

#     def __repr__(self):
#         return (
#             "StemPipeline(" + " → ".join(s.__class__.__name__ for s in self.steps) + ")"
#         )


# def create_stem_pipeline(
#     *, use_hazm: bool = True, use_parsivar: bool = True
# ) -> StemPipeline:
#     steps: List[StemStep] = []
#     if use_hazm and use_parsivar:
#         steps.append(CombinedStemStep())
#     elif use_parsivar:
#         steps.append(ParsivarStemStep())
#     elif use_hazm:
#         steps.append(HazmStemStep())
#     else:
#         raise ValueError("At least one of use_hazm or use_parsivar must be True.")
#     return StemPipeline(steps)
