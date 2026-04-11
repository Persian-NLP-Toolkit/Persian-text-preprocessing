from abc import ABC, abstractmethod


class SpellStep(ABC):
    """Abstract base for all spell-checker steps."""

    @abstractmethod
    def apply(self, text: str) -> str: ...
