# Detect Latin-only Persian sentences and convert via Parsivar.
from parsivar import Normalizer as _PV

_par_ping = _PV(pinglish_conversion_needed=True)


def is_pinglish(text: str) -> bool:
    """True iff text has Latin letters and no Persian letters."""
    return any("A" <= ch <= "z" for ch in text) and not any(
        "\u0600" <= ch <= "\u06ff" for ch in text
    )


def convert(text: str) -> str:
    """Convert Pinglish to Persian if needed, else return unchanged."""
    return _par_ping.normalize(text) if is_pinglish(text) else text
