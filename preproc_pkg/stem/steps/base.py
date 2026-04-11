from abc import ABC, abstractmethod


class StemStep(ABC):
    """Abstract interface for stemming pipeline steps."""

    @abstractmethod
    def apply(self, text: str) -> str:
        """Transform input text into stemmed representation."""
        raise NotImplementedError
