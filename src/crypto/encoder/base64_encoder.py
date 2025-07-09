import base64
import json
from typing import Any
from .encoder import Encoder


class Base64Encoder(Encoder):
    def encode(self, data: Any) -> str:
        return base64.b64encode(json.dumps(data).encode()).decode()

    def decode(self, data: str) -> Any:
        try:
            return json.loads(base64.b64decode(data).decode())
        except Exception:
            return data
