from flask import Blueprint, Response, jsonify, request
import json
import hmac
import hashlib
import os
import base64
from webargs.flaskparser import use_kwargs
from marshmallow import Schema, fields
from src.exceptions import ForbiddenException, BadRequestException
from typing import Any, Literal

sign_blueprint = Blueprint("crypto_sign", __name__)


def _get_albert_secret():
    secret = os.getenv("ALBERT_HMAC_SECRET")
    assert secret is not None

    return base64.b64decode(secret)


def _sign_payload(message):
    canonical_payload = json.dumps(message, sort_keys=True, separators=(",", ":"))
    return hmac.new(
        _get_albert_secret(), canonical_payload.encode(), hashlib.sha256
    ).hexdigest()


def _verify_signature(message, request_signature):
    canonical_payload = json.dumps(message, sort_keys=True, separators=(",", ":"))
    expected_signature = hmac.new(
        _get_albert_secret(), bytes(canonical_payload, "utf-8"), hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(expected_signature, request_signature) is False:
        raise ForbiddenException("HMAC signature equality failed")


class SignatureSchema(Schema):
    signature = fields.Str(required=True)
    data = fields.Dict(keys=fields.Str(), values=fields.Raw(), required=True)


@sign_blueprint.route("/sign", methods=["POST"])
def sign() -> Response:
    data: dict[str, Any] = request.get_json()

    if not data:
        raise BadRequestException("Nothing to sign")

    signature = _sign_payload(data)

    return jsonify({"signature": signature})


@sign_blueprint.route("/verify", methods=["POST"])
@use_kwargs(SignatureSchema, location="json")
def verify(signature: str, data: dict[str, Any]) -> tuple[Response, Literal[204]]:
    _verify_signature(data, signature)

    return jsonify({}), 204
