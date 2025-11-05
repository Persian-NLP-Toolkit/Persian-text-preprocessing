import re

_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def process(text: str) -> str:
    """Mask email addresses -> [EMAIL]."""
    return _EMAIL_RE.sub("[EMAIL]", text)
