import inspect
import warnings
from hazm import Normalizer as _HZ

_VALID_KW = set(inspect.signature(_HZ).parameters)


class HazmNormalizer:
    """
    Wraps hazm.Normalizer with version-safe kwargs handling.
    - strict=False: unknown kwargs dropped + warning (can be turned off).
    - strict=True : If the key is unknown, throw an error.
    """

    def __init__(
        self, *, strict: bool = False, warn_on_ignored: bool = True, **hz_kwargs
    ):
        unknown = {k: v for k, v in hz_kwargs.items() if k not in _VALID_KW}
        if unknown:
            msg = f"HazmNormalizer: ignored unknown kwargs: {sorted(unknown.keys())}"
            if strict:
                raise TypeError(msg)
            if warn_on_ignored:
                warnings.warn(msg, RuntimeWarning)
        safe_kwargs = {k: v for k, v in hz_kwargs.items() if k in _VALID_KW}
        self._norm = _HZ(**safe_kwargs)

    def __call__(self, text: str) -> str:
        return self._norm.normalize(text)


# from hazm import Normalizer as _HZ


# class HazmNormalizer:
#     """Expose every Hazm switch via kwargs."""

#     def __init__(self, **hz_kwargs):
#         self._norm = _HZ(**hz_kwargs)

#     def __call__(self, text: str) -> str:
#         return self._norm.normalize(text)
