from abc import ABC, abstractmethod


class StemStep(ABC):
    @abstractmethod
    def apply(self, text: str) -> str: ...
