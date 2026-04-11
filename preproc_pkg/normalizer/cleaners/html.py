import re

HTML_RE = re.compile(r"<[^>]+>")
LABEL = "html"
PATTERN = HTML_RE  # exported for metrics (matches removed)


def process(text: str) -> str:
    """Strip HTML/XML tags."""
    return HTML_RE.sub("", text)
