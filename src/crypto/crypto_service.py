from typing import Any
from src.crypto import Encoder, Signer


class CryptoService:
    def __init__(self, encoder: Encoder, signer: Signer):
        self.encoder = encoder
        self.signer = signer

    def encrypt(self, data: Any) -> str:
        return self.encoder.encode(data)

    def decrypt(self, data: str) -> Any:
        return self.encoder.decode(data)

    def sign(self, data: dict[str, Any]) -> str:
        return self.signer.sign(data)

    def verify(self, data: dict[str, Any], signature: str) -> bool:
        return self.signer.verify(data, signature)
