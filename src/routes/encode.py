from flask import Blueprint, Response, jsonify, request
import json
import base64
from typing import Any

encode_blueprint = Blueprint("crypto_encode", __name__)


def _encrypt(raw_value: Any) -> str:
    json_str = json.dumps(raw_value)
    encoded_json_str = base64.b64encode(json_str.encode()).decode()

    return encoded_json_str


def _decrypt(encoded_value: str) -> Any:
    try:
        json_str = base64.b64decode(encoded_value, validate=True).decode()
        value = json.loads(json_str)

        return value
    except Exception:
        return encoded_value


@encode_blueprint.route("/encrypt", methods=["POST"])
def encrypt() -> Response:
    data: dict[str, Any] = request.get_json()

    encrypted = {}
    for key, value in data.items():
        encrypted[key] = _encrypt(value)

    return jsonify(encrypted)


@encode_blueprint.route("/decrypt", methods=["POST"])
def decrypt() -> Response:
    data: dict[str, Any] = request.get_json()

    decrypted = {}
    for key, value in data.items():
        decrypted[key] = _decrypt(value)

    return jsonify(decrypted)
