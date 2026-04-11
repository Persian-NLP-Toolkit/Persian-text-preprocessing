from abc import ABC, abstractmethod


class StopwordStep(ABC):
    """Abstract interface for stopword-removal pipeline steps."""

    @abstractmethod
    def apply(self, text: str) -> str:
        """Transform input text by removing or filtering stopwords."""
        raise NotImplementedError
