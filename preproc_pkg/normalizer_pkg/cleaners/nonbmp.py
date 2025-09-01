import re

_NON_BMP_RE = re.compile(r"[^\u0000-\uFFFF]")


def process(text: str) -> str:
    """Remove non-BMP code-points (emoji, fancy symbols)."""
    return _NON_BMP_RE.sub(" ", text)
