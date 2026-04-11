from abc import ABC, abstractmethod


class FormalStep(ABC):
    """Abstract interface for formalization pipeline steps."""

    @abstractmethod
    def apply(self, text: str) -> str:
        """Transform input text to a (more) formal form."""
        raise NotImplementedError
