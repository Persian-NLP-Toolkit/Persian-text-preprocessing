import re

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
LABEL = "email"
PATTERN = EMAIL_RE  # exported for metrics


def process(text: str) -> str:
    """Mask email addresses -> [EMAIL]."""
    return EMAIL_RE.sub("[EMAIL]", text)
