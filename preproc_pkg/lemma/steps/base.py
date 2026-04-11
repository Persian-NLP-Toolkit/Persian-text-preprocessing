from abc import ABC, abstractmethod


class LemmaStep(ABC):
    """Abstract interface for lemmatization steps."""

    @abstractmethod
    def apply(self, text: str) -> str:
        """Convert text to its lemmatized form (base forms of words)."""
        raise NotImplementedError
