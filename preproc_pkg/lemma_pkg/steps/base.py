from abc import ABC, abstractmethod


class LemmaStep(ABC):
    @abstractmethod
    def apply(self, text: str) -> str:
        """Convert text to its lemmatized form (base forms of words)."""
        pass
