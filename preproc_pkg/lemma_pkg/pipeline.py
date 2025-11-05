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
            + " → ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


def create_lemma_pipeline(
    *, use_hazm: bool = True, use_parsivar: bool = True, prefer_past: bool = False
) -> LemmaPipeline:
    """
    prefer_past=False (default): return PRESENT stem for verbs.
    prefer_past=True: return PAST stem for verbs.
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


# from typing import List
# from .steps import LemmaStep, HazmLemmaStep, ParsivarLemmaStep, CombinedLemmaStep


# class LemmaPipeline:
#     def __init__(self, steps: List[LemmaStep]):
#         self.steps = steps

#     def __call__(self, text: str) -> str:
#         for s in self.steps:
#             text = s.apply(text)
#         return text

#     def __repr__(self):
#         return (
#             "LemmaPipeline("
#             + " → ".join(s.__class__.__name__ for s in self.steps)
#             + ")"
#         )


# def create_lemma_pipeline(
#     *, use_hazm: bool = True, use_parsivar: bool = True
# ) -> LemmaPipeline:
#     steps: List[LemmaStep] = []
#     if use_hazm and use_parsivar:
#         steps.append(CombinedLemmaStep())
#     elif use_hazm:
#         steps.append(HazmLemmaStep())
#     elif use_parsivar:
#         steps.append(ParsivarLemmaStep())
#     else:
#         raise ValueError("At least one of use_hazm or use_parsivar must be True.")
#     return LemmaPipeline(steps)
