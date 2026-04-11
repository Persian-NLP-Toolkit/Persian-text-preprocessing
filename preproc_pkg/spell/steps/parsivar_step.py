from parsivar import SpellCheck
from .base import SpellStep
from ..._assets import ensure_parsivar_spell_data


class ParsivarSpellStep(SpellStep):
    """Dictionary / rule-based spell correction via Parsivar."""

    def __init__(self):
        # make sure resources exist before Parsivar tries to open files
        ensure_parsivar_spell_data()
        self._sp = SpellCheck()

    def apply(self, text: str) -> str:
        return self._sp.spell_corrector(text)
