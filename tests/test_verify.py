import pytest
from src.app import app
import base64

# TODO: UPDATE WITH ENCODING PROVIDER


@pytest.fixture
def client():
    return app.test_client()


def test_verify_incorrect_payload(client):
    response = client.post("/v0/crypto/verify", json={})

    assert response.status_code == 422
    assert response.get_json()["error"] == "bad_request"


def test_verify_invalid_signature(client):
    payload = {
        "signature": "a_real_one",
        "data": {"message": "Hello World", "timestamp": 1616161616},
    }
    response = client.post("/v0/crypto/verify", json=payload)

    assert response.status_code == 403
    assert response.get_json()["error"] == "forbidden"


def test_verify_valid_signature(client):
    payload = {
        "signature": "9344b6a38aae164f66752747d997add35f0691f6e2207326afd99be74f8c0ae2",
        "data": {
            "name": "Albert",
            "contact": {"email": "hello@albert.com", "phone": "+1-800-ALBERT-42"},
            "age": 999,
        },
    }
    response = client.post("/v0/crypto/verify", json=payload)

    assert response.status_code == 204


def test_verify_valid_signature_change_order(client):
    payload = {
        "signature": "9344b6a38aae164f66752747d997add35f0691f6e2207326afd99be74f8c0ae2",
        "data": {
            "contact": {"phone": "+1-800-ALBERT-42", "email": "hello@albert.com"},
            "age": 999,
            "name": "Albert",
        },
    }
    response = client.post("/v0/crypto/verify", json=payload)

    assert response.status_code == 204
