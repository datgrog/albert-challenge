from abc import ABC, abstractmethod
from typing import Any


class Encoder(ABC):
    @abstractmethod
    def encode(self, data: Any) -> str:
        pass

    @abstractmethod
    def decode(self, data: str) -> Any:
        pass
