import re

# Avoid matching mentions inside emails by requiring no word-char before '@'.
MENTION_RE = re.compile(r"(?<!\w)(?<!\w@)@[A-Za-z0-9_]{2,}")
LABEL = "mention"
PATTERN = MENTION_RE  # exported for metrics


def process(text: str) -> str:
    """Mask @mentions -> [MENTION]."""
    return MENTION_RE.sub("[MENTION]", text)
