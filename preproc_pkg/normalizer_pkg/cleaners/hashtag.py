import re

_HASHTAG_RE = re.compile(r"(?<!\w)#([A-Za-z0-9_]+|[\u0600-\u06FF0-9_]+)")


def process(text: str) -> str:
    """Mask hashtags -> [HASHTAG]."""
    return _HASHTAG_RE.sub("[HASHTAG]", text)
