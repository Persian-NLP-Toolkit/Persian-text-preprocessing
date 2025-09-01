"""Package‑level convenience factories."""

from importlib import import_module
from typing import Any


def _lazy(module_path: str, obj: str, *args: Any, **kwargs: Any):
    mod = import_module(module_path)
    return getattr(mod, obj)(*args, **kwargs)


def create_spell_pipeline(**kwargs):
    """Factory wrapper for spell pipeline."""
    return _lazy("preproc_pkg.spell_pkg.pipeline", "create_spell_pipeline", **kwargs)


def create_formal_pipeline(**kwargs):
    """Factory wrapper for informal→formal pipeline."""
    return _lazy("preproc_pkg.formal_pkg.pipeline", "create_formal_pipeline", **kwargs)


__all__ = ["create_spell_pipeline", "create_formal_pipeline"]
