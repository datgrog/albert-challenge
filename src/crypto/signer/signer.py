from abc import ABC, abstractmethod
from typing import Any


class Signer(ABC):
    @abstractmethod
    def sign(self, data: dict[str, Any]) -> str:
        pass

    @abstractmethod
    def verify(self, data: dict[str, Any], signature: str) -> bool:
        pass
