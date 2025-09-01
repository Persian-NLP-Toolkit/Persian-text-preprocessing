import re

_URL_RE = re.compile(r"(https?://\S+|www\.\S+)")


def process(text: str) -> str:
    """Replace any URL with literal [URL]."""
    return _URL_RE.sub("[URL]", text)
