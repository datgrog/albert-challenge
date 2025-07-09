from flask import Blueprint, Response, jsonify, request
from typing import Any
from src.crypto import crypto_service

encode_blueprint = Blueprint("crypto_encode", __name__)


@encode_blueprint.route("/encrypt", methods=["POST"])
def encrypt() -> Response:
    data: dict[str, Any] = request.get_json()

    encrypted = {}
    for key, value in data.items():
        encrypted[key] = crypto_service.encrypt(value)

    return jsonify(encrypted)


@encode_blueprint.route("/decrypt", methods=["POST"])
def decrypt() -> Response:
    data: dict[str, Any] = request.get_json()

    decrypted = {}
    for key, value in data.items():
        decrypted[key] = crypto_service.decrypt(value)

    return jsonify(decrypted)
