import re

_IR_MOBILE = re.compile(r"(?:\+98|0098|0)?9\d{9}")

_INTL_GENERIC = re.compile(r"\+?\d[\d\s\-]{7,}\d")


def process(text: str) -> str:
    """Mask phone numbers -> [PHONE]. Tries Iran mobile first, then a generic intl pattern."""
    out = _IR_MOBILE.sub("[PHONE]", text)
    out = _INTL_GENERIC.sub("[PHONE]", out)
    return out
