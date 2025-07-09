from flask import Blueprint, Response, jsonify, request
import json
import hmac
import hashlib
import os
import base64
from webargs.flaskparser import use_kwargs
from marshmallow import Schema, fields
from src.exceptions import BadRequestException
from typing import Any, Literal
from src.crypto import crypto_service

sign_blueprint = Blueprint("crypto_sign", __name__)


class SignatureSchema(Schema):
    signature = fields.Str(required=True)
    data = fields.Dict(keys=fields.Str(), values=fields.Raw(), required=True)


@sign_blueprint.route("/sign", methods=["POST"])
def sign() -> Response:
    data: dict[str, Any] = request.get_json()

    if not data:
        raise BadRequestException("Nothing to sign")

    signature = crypto_service.sign(data)

    return jsonify({"signature": signature})


@sign_blueprint.route("/verify", methods=["POST"])
@use_kwargs(SignatureSchema, location="json")
def verify(signature: str, data: dict[str, Any]) -> tuple[Response, Literal[204]]:
    if crypto_service.verify(data, signature) is False:
        raise BadRequestException("HMAC signature equality failed")

    return jsonify({}), 204
