from abc import ABC, abstractmethod


class StopwordStep(ABC):
    @abstractmethod
    def apply(self, text: str) -> str: ...
