"""Run: cleaners ➜ pinglish ➜ Parsivar ➜ Hazm ➜ final cleaners."""

from typing import Dict, Any, List, Callable
from .cleaners import html, url, nonbmp, collapse_spaces
from .pinglish import convert as pinglish_convert
from .hazm_normalizer import HazmNormalizer
from .parsivar_normalizer import ParsivarNormalizer

# default configs – flip any key True/False per need
DEFAULT_HAZM_CFG: Dict[str, Any] = dict(
    correct_spacing=True,
    remove_diacritics=True,
    remove_specials_chars=True,
    decrease_repeated_chars=True,
    persian_style=True,
    persian_numbers=True,
    unicodes_replacement=True,
    seperate_mi=True,
)
DEFAULT_PV_CFG: Dict[str, Any] = dict(
    statistical_space_correction=True,
    pinglish_conversion_needed=False,  # dynamic
    normalize_numbers=True,
    token_punctuation_augmentation=True,
)


# build engine instances once
def _get_hazm(cfg):
    return HazmNormalizer(**cfg)


def _get_pv(cfg):
    return ParsivarNormalizer(**cfg)


# ordered steps (functions must take & return str)
_CLEAN_PRE: List[Callable[[str], str]] = [html.process, url.process, nonbmp.process]
_CLEAN_POST: List[Callable[[str], str]] = [nonbmp.process, collapse_spaces.process]


def normalize(
    text: str,
    hazm_cfg: Dict[str, Any] = None,
    parsivar_cfg: Dict[str, Any] = None,
) -> str:
    """Full text normalisation pipeline."""
    if not text:
        return ""

    # 1) pre-clean
    for fn in _CLEAN_PRE:
        text = fn(text)

    # 2) optional Pinglish conversion (before other Persian ops)
    text = pinglish_convert(text)

    # 3) Parsivar stage
    pv_cfg = {**DEFAULT_PV_CFG, **(parsivar_cfg or {})}
    text = _get_pv(pv_cfg)(text)

    # 4) Hazm stage
    hz_cfg = {**DEFAULT_HAZM_CFG, **(hazm_cfg or {})}
    text = _get_hazm(hz_cfg)(text)

    # 5) post-clean
    for fn in _CLEAN_POST:
        text = fn(text)

    return text
