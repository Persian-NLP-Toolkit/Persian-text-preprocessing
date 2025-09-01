from parsivar import SpellCheck
from .base import SpellStep


class ParsivarSpellStep(SpellStep):
    """Dictionary / rule-based spell correction via Parsivar."""

    def __init__(self):
        self._sp = SpellCheck()

    def apply(self, text: str) -> str:
        return self._sp.spell_corrector(text)
