# Thin configurable wrapper around Hazm Normalizer.
from hazm import Normalizer as _HZ


class HazmNormalizer:
    """Expose every Hazm switch via kwargs."""

    def __init__(self, **hz_kwargs):
        self._norm = _HZ(**hz_kwargs)

    def __call__(self, text: str) -> str:
        return self._norm.normalize(text)
