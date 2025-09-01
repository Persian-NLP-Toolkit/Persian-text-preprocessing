from abc import ABC, abstractmethod


class FormalStep(ABC):
    @abstractmethod
    def apply(self, text: str) -> str: ...
