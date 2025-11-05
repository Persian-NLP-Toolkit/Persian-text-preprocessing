"""Run: cleaners ➜ pinglish ➜ Parsivar ➜ Hazm ➜ final cleaners."""

from typing import Dict, Any, List, Callable, Optional
from .cleaners import (
    html,
    url,
    nonbmp,
    collapse_spaces,
    email as email_c,
    mention as mention_c,
    hashtag as hashtag_c,
    phone as phone_c,
    quotes_dashes as qd_c,
)
from .pinglish import convert as pinglish_convert
from .hazm_normalizer import HazmNormalizer
from .parsivar_normalizer import ParsivarNormalizer


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


StepFn = Callable[[str], str]


class NormalizerPipeline:
    """Configurable normalizer pipeline. Callable(text)->text."""

    def __init__(
        self,
        *,
        enable_quotes_dashes: bool = True,
        enable_url: bool = True,
        enable_email: bool = True,
        enable_mention: bool = True,
        enable_hashtag: bool = True,
        enable_phone: bool = True,
        enable_nonbmp: bool = True,
        enable_pinglish: bool = True,
        parsivar_cfg: Optional[Dict[str, Any]] = None,
        hazm_cfg: Optional[Dict[str, Any]] = None,
    ):
        self._pre: List[StepFn] = [html.process]
        if enable_quotes_dashes:
            self._pre.append(qd_c.process)
        if enable_url:
            self._pre.append(url.process)
        if enable_email:
            self._pre.append(email_c.process)
        if enable_mention:
            self._pre.append(mention_c.process)
        if enable_hashtag:
            self._pre.append(hashtag_c.process)
        if enable_phone:
            self._pre.append(phone_c.process)
        if enable_nonbmp:
            self._pre.append(nonbmp.process)

        # Engines
        self._pv = ParsivarNormalizer(**({**DEFAULT_PV_CFG, **(parsivar_cfg or {})}))
        self._hz = HazmNormalizer(**({**DEFAULT_HAZM_CFG, **(hazm_cfg or {})}))
        self._enable_pinglish = enable_pinglish

        # Post
        self._post: List[StepFn] = [nonbmp.process, collapse_spaces.process]

    def __call__(self, text: str) -> str:
        if not text:
            return ""
        # 1) pre-cleaners
        for fn in self._pre:
            text = fn(text)
        # 2) pinglish (optional)
        if self._enable_pinglish:
            text = pinglish_convert(text)
        # 3) Parsivar
        text = self._pv(text)
        # 4) Hazm
        text = self._hz(text)
        # 5) post-cleaners
        for fn in self._post:
            text = fn(text)
        return text

    def __repr__(self) -> str:
        return "NormalizerPipeline(pre={%d}, pinglish=%s, post={%d})" % (
            len(self._pre),
            self._enable_pinglish,
            len(self._post),
        )


def create_normalizer_pipeline(**kwargs) -> NormalizerPipeline:
    """
    Factory to build NormalizerPipeline.
    Keyword-args mirror the __init__ flags (enable_* toggles + *_cfg).
    """
    return NormalizerPipeline(**kwargs)


# Backward-compatible functional API
def normalize(
    text: str,
    hazm_cfg: Dict[str, Any] = None,
    parsivar_cfg: Dict[str, Any] = None,
) -> str:
    """Legacy one-shot function kept for compatibility."""
    pipe = create_normalizer_pipeline(hazm_cfg=hazm_cfg, parsivar_cfg=parsivar_cfg)
    return pipe(text)
