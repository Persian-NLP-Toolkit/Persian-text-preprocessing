import re

# Map typographic quotes to ASCII quotes
QUOTE_MAP = str.maketrans(
    {
        "«": '"',
        "»": '"',
        "“": '"',
        "”": '"',
        "„": '"',
        "‟": '"',
        "ˮ": '"',
        "‘": "'",
        "’": "'",
        "‚": "'",
        "‹": "'",
        "›": "'",
        "′": "'",
    }
)

# Only typographic dash variants (EXCLUDES ASCII hyphen-minus '-')
_DASH_CHARS = "–—‒−﹣‐"  # intentionally no "-" to avoid breaking URLs/emails/compounds
_DASH_RE = re.compile(f"[{re.escape(_DASH_CHARS)}]")

# Export patterns for metrics collection
LABEL = "quotes_dashes"
PATTERNS = [
    re.compile(r"[«»“”„‟ˮ‘’‚‹›′]"),  # quotes that will be normalized
    re.compile(f"[{re.escape(_DASH_CHARS)}]"),  # non-ASCII dashes normalized to em dash
]


def process(text: str) -> str:
    """Normalize quotes to ASCII and dash variants to em dash, without touching ASCII '-'."""
    # Normalize quotes
    text = text.translate(QUOTE_MAP)
    # Normalize typographic dashes to em dash
    text = _DASH_RE.sub("—", text)
    # Collapse multiple em dashes to a single one
    text = re.sub(r"—{2,}", "—", text)
    return text
