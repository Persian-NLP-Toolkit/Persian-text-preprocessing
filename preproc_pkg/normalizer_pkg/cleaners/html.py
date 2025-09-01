import re

_HTML_RE = re.compile(r"<[^>]+>")


def process(text: str) -> str:
    """Strip HTML/XML tags."""
    return _HTML_RE.sub("", text)
