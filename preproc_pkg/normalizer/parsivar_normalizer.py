from parsivar import Normalizer as _PV
import inspect

# build a set of valid keyword names from the current Parsivar signature
_VALID_KW = set(inspect.signature(_PV).parameters)


class ParsivarNormalizer:
    """Wrapper that silently drops unknown kwargs (version-proof)."""

    def __init__(self, **pv_kwargs):
        safe_kwargs = {k: v for k, v in pv_kwargs.items() if k in _VALID_KW}
        self._norm = _PV(**safe_kwargs)

    def __call__(self, text: str) -> str:
        return self._norm.normalize(text)
