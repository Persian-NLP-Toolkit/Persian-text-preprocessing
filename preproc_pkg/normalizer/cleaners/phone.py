import re

# Iran mobile (with optional +98/0098/0) with digit boundaries.
IR_MOBILE = re.compile(r"(?<!\d)(?:\+98|0098|0)?9\d{9}(?!\d)")

# Generic international: at least ~8 digits; avoid word-joins.
INTL_GENERIC = re.compile(r"(?<!\w)(?:\+|00)?\d[\d\s\-]{6,}\d(?!\w)")

LABEL = "phone"
PATTERNS = [IR_MOBILE, INTL_GENERIC]  # exported for metrics


def process(text: str) -> str:
    """Mask phone numbers -> [PHONE]. First Iran mobiles, then generic intl."""
    out = IR_MOBILE.sub("[PHONE]", text)
    out = INTL_GENERIC.sub("[PHONE]", out)
    return out
