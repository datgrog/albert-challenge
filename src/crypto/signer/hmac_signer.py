import hmac
import hashlib
import json
import base64
from typing import Any
from .signer import Signer


class HmacSigner(Signer):
    def __init__(self, b64_secret: str):
        self.secret = base64.b64decode(b64_secret)

    def sign(self, message: dict[str, Any]) -> str:
        canonical_payload = json.dumps(message, sort_keys=True, separators=(",", ":"))
        return hmac.new(
            self.secret, canonical_payload.encode(), hashlib.sha256
        ).hexdigest()

    def verify(self, message: dict[str, Any], signature: str) -> bool:
        return hmac.compare_digest(self.sign(message), signature)
