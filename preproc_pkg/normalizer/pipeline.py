"""Run: cleaners -> pinglish -> Parsivar? -> Hazm? -> final cleaners."""

import re
from typing import Dict, Any, List, Callable, Optional, Tuple, Union
from time import perf_counter
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

# (imports continue)
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


class _Step:
    """Internal step wrapper to carry label and optional regex pattern(s) for metrics."""

    def __init__(self, label: str, fn: StepFn, pattern=None):
        self.label = label
        self.fn = fn
        self.pattern = pattern  # can be a compiled regex or a list of them


class NormalizerPipeline:
    """
    Configurable Persian text normalizer.

    Order:
      1) light unicode cleanup (NFC, control chars, NBSP/ZWNJ fix)
      2) pre-cleaners (html, quotes/dashes, url/email/mention/hashtag/phone, nonbmp)
      3) pinglish (optional)
      4) Parsivar normalize
      5) Hazm normalize
      6) post-cleaners (nonbmp, collapse_spaces)

    Parameters
    ----------
    enable_* : bool
        Toggles for individual cleaners.
    parsivar_cfg : dict, optional
        Forwarded to Parsivar normalizer (unknown keys ignored).
    hazm_cfg : dict, optional
        Forwarded to Hazm normalizer (unknown keys dropped/warned).
    enable_metrics : bool
        If True, collect per-step timings and regex match counts.
    collapse_keep_newlines : bool
        If True, preserve paragraph breaks (two newlines).
    """

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
        # NEW: allow toggling Parsivar/Hazm engines
        enable_parsivar: bool = True,
        enable_hazm: bool = True,
        parsivar_cfg: Optional[Dict[str, Any]] = None,
        hazm_cfg: Optional[Dict[str, Any]] = None,
        enable_metrics: bool = False,
        collapse_keep_newlines: bool = False,
    ):
        # 1) Pre-cleaners with optional metrics patterns
        self._pre: List[_Step] = [
            _Step("html", html.process, getattr(html, "PATTERN", None))
        ]
        if enable_quotes_dashes:
            self._pre.append(
                _Step(
                    "quotes_dashes",
                    qd_c.process,
                    getattr(qd_c, "PATTERNS", None),
                )
            )
        if enable_url:
            self._pre.append(_Step("url", url.process, getattr(url, "PATTERN", None)))
        if enable_email:
            self._pre.append(
                _Step("email", email_c.process, getattr(email_c, "PATTERN", None))
            )
        if enable_mention:
            self._pre.append(
                _Step("mention", mention_c.process, getattr(mention_c, "PATTERN", None))
            )
        if enable_hashtag:
            self._pre.append(
                _Step("hashtag", hashtag_c.process, getattr(hashtag_c, "PATTERN", None))
            )
        if enable_phone:
            pattern = getattr(phone_c, "PATTERNS", getattr(phone_c, "PATTERN", None))
            self._pre.append(_Step("phone", phone_c.process, pattern))
        if enable_nonbmp:
            self._pre.append(
                _Step("nonbmp", nonbmp.process, getattr(nonbmp, "PATTERN", None))
            )

        # 2) Engines (conditionally enabled)
        self._enable_parsivar = enable_parsivar
        self._enable_hazm = enable_hazm
        self._pv = None
        self._hz = None
        if enable_parsivar:
            self._pv = ParsivarNormalizer(
                **({**DEFAULT_PV_CFG, **(parsivar_cfg or {})})
            )
        if enable_hazm:
            self._hz = HazmNormalizer(**({**DEFAULT_HAZM_CFG, **(hazm_cfg or {})}))
        self._enable_pinglish = enable_pinglish

        # 3) Post
        self._collapse_keep_newlines = collapse_keep_newlines
        self._post: List[_Step] = [
            _Step("nonbmp_post", nonbmp.process, getattr(nonbmp, "PATTERN", None)),
            _Step("tidy_placeholders_punct", _tidy_text, None),
            _Step(
                "collapse_spaces",
                lambda s: collapse_spaces.process(
                    s, keep_newlines=self._collapse_keep_newlines
                ),
                getattr(collapse_spaces, "PATTERN", None),
            ),
        ]
        self._enable_metrics = enable_metrics
        self.last_report: Optional[Dict[str, Any]] = None

    def __call__(
        self, text: str, *, return_report: bool = False
    ) -> Union[str, Tuple[str, Dict[str, Any]]]:
        if not text:
            self.last_report = {"empty_input": True}
            return ("", self.last_report) if return_report else ""

        report: Dict[str, Any] = {"steps": [], "counts": {}, "timings_ms": {}}
        t0 = perf_counter()

        # 1) pre-cleaners
        for st in self._pre:
            before = text
            t = perf_counter()
            text = st.fn(text)
            dt = (perf_counter() - t) * 1000.0
            if self._enable_metrics:
                c = self._count(before, st.pattern)
                report["counts"][st.label] = c
                report["timings_ms"][st.label] = round(dt, 3)
                report["steps"].append(st.label)

        # 2) pinglish (optional)
        if self._enable_pinglish:
            t = perf_counter()
            text = pinglish_convert(text)
            if self._enable_metrics:
                report["timings_ms"]["pinglish"] = round(
                    (perf_counter() - t) * 1000.0, 3
                )
                report["steps"].append("pinglish")

        # 3) Parsivar (optional)
        if self._pv:
            t = perf_counter()
            text = self._pv(text)
            if self._enable_metrics:
                report["timings_ms"]["parsivar"] = round(
                    (perf_counter() - t) * 1000.0, 3
                )
                report["steps"].append("parsivar")

        # 4) Hazm (optional)
        if self._hz:
            t = perf_counter()
            text = self._hz(text)
            if self._enable_metrics:
                report["timings_ms"]["hazm"] = round((perf_counter() - t) * 1000.0, 3)
                report["steps"].append("hazm")

        # 5) post-cleaners
        for st in self._post:
            before = text
            t = perf_counter()
            text = st.fn(text)
            dt = (perf_counter() - t) * 1000.0
            if self._enable_metrics:
                c = self._count(before, st.pattern)
                report["counts"][st.label] = c
                report["timings_ms"][st.label] = round(dt, 3)
                report["steps"].append(st.label)

        if self._enable_metrics:
            report["total_ms"] = round((perf_counter() - t0) * 1000.0, 3)
            self.last_report = report

        return (text, report) if return_report else text

    def _count(self, before: str, pattern) -> int:
        """Count matches in the 'before' text using a compiled regex or list of them."""
        if not pattern:
            return 0
        if isinstance(pattern, list):
            return sum(len(p.findall(before)) for p in pattern)
        return len(pattern.findall(before))

    def __repr__(self) -> str:
        return (
            "NormalizerPipeline(pre=%d, pinglish=%s, parsivar=%s, hazm=%s, post=%d, metrics=%s)"
            % (
                len(self._pre),
                self._enable_pinglish,
                self._enable_parsivar,
                self._enable_hazm,
                len(self._post),
                self._enable_metrics,
            )
        )


_FIX_PUNCT = re.compile(r"\s+([،.!؟؛:»\]\)])")
_FIX_OPEN = re.compile(r"([«\[\(])\s+")
_ZWNJ = "\u200c"
# [ EMAIL‌ ] / [ MENTION ] -> [EMAIL] / [MENTION]
_PH = re.compile(r"\[\s*([A-Z" + _ZWNJ + r"]+)\s*\]")


def _tidy_text(s: str) -> str:
    """Normalize spaces around punctuation/brackets and fix placeholders like [MENTION]."""

    s = (
        s.replace("\u00a0", " ")  # NBSP
        .replace("\u202f", " ")  # NNBSP
        .replace("\u2007", " ")  # figure space
        .replace("\u2009", " ")  # thin space
    )

    s = _FIX_PUNCT.sub(r"\1", s)
    s = _FIX_OPEN.sub(r"\1", s)

    def _ph(m):
        inner = m.group(1).replace(_ZWNJ, "")
        return f"[{inner}]"

    s = _PH.sub(_ph, s)

    s = re.sub(r"\u200c+(?=\s|[،.!؟؛:»\]\)\}\[\(\{])", "", s)
    s = re.sub(r"(?<=\s)\u200c+", "", s)
    s = re.sub(r"\u200c+(?=$)", "", s)
    s = re.sub(r" {2,}", " ", s)

    return s.strip()


def create_normalizer_pipeline(**kwargs) -> NormalizerPipeline:
    """
    Build a NormalizerPipeline.

    Parameters
    ----------
    enable_* : bool
        Toggles for individual cleaners (quotes_dashes/url/email/mention/hashtag/phone/nonbmp) and pinglish conversion.
    enable_parsivar : bool
        Enable Parsivar normalizer stage (default: True).
    enable_hazm : bool
        Enable Hazm normalizer stage (default: True).
    parsivar_cfg : dict, optional
        Keyword-args forwarded to Parsivar normalizer (unknown keys ignored).
    hazm_cfg : dict, optional
        Keyword-args forwarded to Hazm normalizer (unknown keys ignored).
    enable_metrics : bool
        If True, per-step timings and regex match counts are collected.
    collapse_keep_newlines : bool
        If True, collapse only horizontal spaces and keep paragraph breaks (two newlines).

    Returns
    -------
    NormalizerPipeline
        Callable object. Call with `return_report=True` to also get a metrics dict.

    Examples
    --------
    >>> pipe = create_normalizer_pipeline(enable_metrics=True, enable_parsivar=True, enable_hazm=False)
    >>> text, rep = pipe("contact me at a@b.com", return_report=True)
    """
    return NormalizerPipeline(**kwargs)


# Backward-compatible functional API
def normalize(
    text: str, hazm_cfg: Dict[str, Any] = None, parsivar_cfg: Dict[str, Any] = None
) -> str:
    """Legacy one-shot function kept for compatibility."""
    pipe = create_normalizer_pipeline(hazm_cfg=hazm_cfg, parsivar_cfg=parsivar_cfg)
    return pipe(text)
