import re

NON_BMP_RE = re.compile(r"[^\u0000-\uFFFF]")
LABEL = "nonbmp"
PATTERN = NON_BMP_RE  # exported for metrics (matches removed)


def process(text: str) -> str:
    """Remove non-BMP code-points (emoji, fancy symbols)."""
    return NON_BMP_RE.sub(" ", text)
