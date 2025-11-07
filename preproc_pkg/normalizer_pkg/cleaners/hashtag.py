import re

# Avoid HTML entities like '&#123;' via negative lookbehind for '&'.
HASHTAG_RE = re.compile(r"(?<!\w)(?<!&)#([A-Za-z0-9_]+|[\u0600-\u06FF0-9_]+)")
LABEL = "hashtag"
PATTERN = HASHTAG_RE  # exported for metrics


def process(text: str) -> str:
    """Mask hashtags -> [HASHTAG]."""
    return HASHTAG_RE.sub("[HASHTAG]", text)
