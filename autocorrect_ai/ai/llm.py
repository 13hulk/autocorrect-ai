from abc import ABC, abstractmethod


class Llm(ABC):
    @abstractmethod
    def generate(self, text: str) -> str:
        pass
