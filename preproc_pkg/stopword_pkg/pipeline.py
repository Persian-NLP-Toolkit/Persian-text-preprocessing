from typing import List, Optional
from .steps import StopwordStep, HazmStopwordStep


class StopwordPipeline:
    def __init__(self, steps: List[StopwordStep]):
        self.steps = steps

    def __call__(self, text: str) -> str:
        for s in self.steps:
            text = s.apply(text)
        return text

    def __repr__(self):
        return (
            "StopwordPipeline("
            + " → ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


def create_stopword_pipeline(
    extra_stopwords: Optional[List[str]] = None,
) -> StopwordPipeline:
    steps: List[StopwordStep] = [HazmStopwordStep(extra=extra_stopwords)]
    return StopwordPipeline(steps)


# from typing import List, Optional
# from .steps import StopwordStep, HazmStopwordStep


# class StopwordPipeline:
#     def __init__(self, steps: List[StopwordStep]):
#         self.steps = steps

#     def __call__(self, text: str) -> str:
#         for step in self.steps:
#             text = step.apply(text)
#         return text

#     def __repr__(self):
#         return (
#             "StopwordPipeline("
#             + " → ".join(step.__class__.__name__ for step in self.steps)
#             + ")"
#         )


# def create_stopword_pipeline(
#     extra_stopwords: Optional[List[str]] = None,
# ) -> StopwordPipeline:
#     """Factory to create a stopword removal pipeline."""
#     steps: List[StopwordStep] = [HazmStopwordStep(extra=extra_stopwords)]
#     return StopwordPipeline(steps)
