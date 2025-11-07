from typing import List, Set


def detokenize(tokens: List[str], punct: Set[str]) -> str:
    """
    Join tokens with Persian-aware spacing rules:
    - Attach RIGHT_ATTACH punctuation to the previous token without space.
    - Attach LEFT_ATTACH punctuation to the next token without space.
    - Do not insert spaces around JOINERS (hyphen/dashes).
    """
    out = ""
    for t in tokens:
        out = (out.rstrip() + t) if t in punct else (out + " " + t)
    return out.strip()
