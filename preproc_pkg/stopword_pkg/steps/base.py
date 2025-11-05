from abc import ABC, abstractmethod


class StopwordStep(ABC):
    @abstractmethod
    def apply(self, text: str) -> str: ...


# from abc import ABC, abstractmethod


# class StopwordStep(ABC):
#     @abstractmethod
#     def apply(self, text: str) -> str:
#         """Remove stop words from the given text."""
#         pass
