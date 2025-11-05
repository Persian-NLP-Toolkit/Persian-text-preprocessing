import re

_MENTION_RE = re.compile(r"(?<!\w)@[A-Za-z0-9_]{2,}")


def process(text: str) -> str:
    """Mask @mentions -> [MENTION]."""
    return _MENTION_RE.sub("[MENTION]", text)
