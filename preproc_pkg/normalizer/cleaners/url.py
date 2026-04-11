import re

# Loose-but-practical URL pattern; avoids trailing punctuation.
URL_RE = re.compile(r"""(?xi)
    \b(
        (?:https?://|ftp://|www\.)
        [^\s<>'"{}|\\^`]+
    )
""")

LABEL = "url"
PATTERN = URL_RE  # exported for metrics


def process(text: str) -> str:
    """Mask URLs -> [URL]."""
    return URL_RE.sub("[URL]", text)
