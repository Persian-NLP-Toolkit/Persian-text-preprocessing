import re

# Export pattern for metrics (counts multi-whitespace runs)
PATTERN = re.compile(r"\s{2,}")
LABEL = "collapse_spaces"

# For the keep_newlines mode
_NO_NL_MULTI_WS = re.compile(r"[ \t\f\v]{2,}")
_MULTI_NEWLINES = re.compile(r"\n{3,}")


def process(text: str, keep_newlines: bool = False) -> str:
    """
    Collapse whitespace runs to a single space.
    If keep_newlines=True: preserve line breaks, collapse only horizontal spaces,
    and reduce 3+ consecutive newlines to exactly two (paragraph boundary).
    """
    if keep_newlines:
        # Collapse horizontal whitespace (except \r and \n)
        text = _NO_NL_MULTI_WS.sub(" ", text)
        # Soften huge blank blocks (optional)
        text = _MULTI_NEWLINES.sub("\n\n", text)
        return text.strip()
    # Default: collapse all whitespace runs (space, tab, newlines) to a single space
    return PATTERN.sub(" ", text).strip()
