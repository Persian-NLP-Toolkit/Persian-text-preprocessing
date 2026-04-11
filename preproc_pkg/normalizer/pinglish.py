# Detect Latin-only Persian sentences and convert via Parsivar.
import re
from parsivar import Normalizer as _PV

_par_ping = _PV(pinglish_conversion_needed=True)
_LATIN = re.compile(r"[A-Za-z]")
_PERSIAN = re.compile(r"[\u0600-\u06FF]")


def is_pinglish(text: str) -> bool:
    """True iff text contains Latin letters and no Persian letters."""
    return bool(_LATIN.search(text)) and not bool(_PERSIAN.search(text))


def convert(text: str) -> str:
    """Convert Pinglish to Persian if needed, else return unchanged."""
    return _par_ping.normalize(text) if is_pinglish(text) else text
