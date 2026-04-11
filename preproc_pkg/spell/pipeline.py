from typing import List
from .steps import SpellStep, ParsivarSpellStep, TransformerSpellStep
import re


class SpellPipeline:
    def __init__(self, steps: List[SpellStep]):
        self.steps = steps

    def __call__(self, text: str) -> str:
        for s in self.steps:
            text = s.apply(text)
        return _tidy(text)

    def __repr__(self):
        return (
            "SpellPipeline("
            + " -> ".join(s.__class__.__name__ for s in self.steps)
            + ")"
        )


_FIX_PUNCT = re.compile(r"\s+([،.!؟؛:»\]\)])")
_FIX_OPEN = re.compile(r"([«\[\(])\s+")


def _tidy(s: str) -> str:
    """
    Remove spaces before closing punctuation and after opening brackets/guillemets.
    """
    s = _FIX_PUNCT.sub(r"\1", s)
    s = _FIX_OPEN.sub(r"\1", s)
    return s.strip()


def create_spell_pipeline(
    *, use_parsivar: bool = True, use_transformer: bool = False, **kwargs
) -> SpellPipeline:
    """
    Build a spell-correction pipeline.

    Parameters
    ----------
    use_parsivar : bool
        If True (default), include Parsivar's dictionary-based spell checker.
    use_transformer : bool
        If True, append a Seq2Seq spell-correction model after Parsivar.
    **kwargs :
        Forwarded to TransformerSpellStep (e.g., model_name, device, generate_kwargs).

    Returns
    -------
    SpellPipeline
    """
    steps: List[SpellStep] = []
    if use_parsivar:
        steps.append(ParsivarSpellStep())
    if use_transformer:
        steps.append(TransformerSpellStep(**kwargs))
    if not steps:
        raise ValueError(
            "At least one of use_parsivar or use_transformer must be True."
        )
    return SpellPipeline(steps)
