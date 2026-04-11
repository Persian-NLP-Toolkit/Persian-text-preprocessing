"""Public factory API for Persian text preprocessing pipelines.

The module exposes lightweight factory functions and keeps imports lazy to
reduce startup overhead and optional dependency pressure.
"""

from importlib import import_module
from typing import Any

__version__ = "0.1.5"


def _lazy(module_path: str, obj: str, *args: Any, **kwargs: Any):
    mod = import_module(module_path)
    return getattr(mod, obj)(*args, **kwargs)


def create_spell_pipeline(**kwargs):
    """Factory wrapper for spell pipeline."""
    return _lazy("preproc_pkg.spell.pipeline", "create_spell_pipeline", **kwargs)


def create_normalizer_pipeline(**kwargs):
    """Factory wrapper for normalizer pipeline."""
    return _lazy(
        "preproc_pkg.normalizer.pipeline", "create_normalizer_pipeline", **kwargs
    )


def create_formal_pipeline(**kwargs):
    """Factory wrapper for informal->formal pipeline."""
    return _lazy("preproc_pkg.formal.pipeline", "create_formal_pipeline", **kwargs)


def create_stopword_pipeline(**kwargs):
    """Factory wrapper for stopword pipeline."""
    return _lazy(
        "preproc_pkg.stopword.pipeline", "create_stopword_pipeline", **kwargs
    )


def create_lemma_pipeline(**kwargs):
    """Factory wrapper for lemmatization pipeline."""
    return _lazy("preproc_pkg.lemma.pipeline", "create_lemma_pipeline", **kwargs)


def create_stem_pipeline(**kwargs):
    """Factory wrapper for stemming pipeline."""
    return _lazy("preproc_pkg.stem.pipeline", "create_stem_pipeline", **kwargs)


__all__ = [
    "create_spell_pipeline",
    "create_formal_pipeline",
    "create_stopword_pipeline",
    "create_lemma_pipeline",
    "create_stem_pipeline",
    "create_normalizer_pipeline",
]
