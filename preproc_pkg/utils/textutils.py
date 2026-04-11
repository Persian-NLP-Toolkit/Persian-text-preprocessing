from typing import List, Set


def detokenize(tokens: List[str], punct: Set[str]) -> str:
    """
    Join tokens by inserting spaces between non-punctuation tokens.

    Any token present in `punct` is attached directly to the previous token
    (no leading whitespace).
    """
    out = ""
    for t in tokens:
        out = (out.rstrip() + t) if t in punct else (out + " " + t)
    return out.strip()
