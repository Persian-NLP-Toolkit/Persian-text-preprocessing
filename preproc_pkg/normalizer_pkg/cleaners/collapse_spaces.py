import re


def process(text: str) -> str:
    """Collapse multiple spaces / linebreak combos to a single space."""
    return re.sub(r"\s{2,}", " ", text).strip()
