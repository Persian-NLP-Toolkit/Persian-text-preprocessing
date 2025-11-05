import re

_QUOTE_MAP = str.maketrans(
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

_DASH_CHARS = "–—‒−﹣‐-"
_DASH_RE = re.compile(f"[{re.escape(_DASH_CHARS)}]")


def process(text: str) -> str:
    text = text.translate(_QUOTE_MAP)
    text = _DASH_RE.sub("—", text)
    text = re.sub(r"—{2,}", "—", text)
    return text
