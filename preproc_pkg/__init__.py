"""Package-level convenience factories."""

from importlib import import_module
from typing import Any


def _lazy(module_path: str, obj: str, *args: Any, **kwargs: Any):
    mod = import_module(module_path)
    return getattr(mod, obj)(*args, **kwargs)


def create_spell_pipeline(**kwargs):
    """Factory wrapper for spell pipeline."""
    return _lazy("preproc_pkg.spell_pkg.pipeline", "create_spell_pipeline", **kwargs)


def create_normalizer_pipeline(**kwargs):
    """Factory wrapper for normalizer pipeline."""
    return _lazy(
        "preproc_pkg.normalizer_pkg.pipeline", "create_normalizer_pipeline", **kwargs
    )


def create_formal_pipeline(**kwargs):
    """Factory wrapper for informal->formal pipeline."""
    return _lazy("preproc_pkg.formal_pkg.pipeline", "create_formal_pipeline", **kwargs)


def create_stopword_pipeline(**kwargs):
    """Factory wrapper for stopword pipeline."""
    return _lazy(
        "preproc_pkg.stopword_pkg.pipeline", "create_stopword_pipeline", **kwargs
    )


def create_lemma_pipeline(**kwargs):
    """Factory wrapper for lemmatization pipeline."""
    return _lazy("preproc_pkg.lemma_pkg.pipeline", "create_lemma_pipeline", **kwargs)


def create_stem_pipeline(**kwargs):
    """Factory wrapper for stemming pipeline."""
    return _lazy("preproc_pkg.stem_pkg.pipeline", "create_stem_pipeline", **kwargs)


__all__ = [
    "create_spell_pipeline",
    "create_formal_pipeline",
    "create_stopword_pipeline",
    "create_lemma_pipeline",
    "create_stem_pipeline",
    "create_normalizer_pipeline",
]
