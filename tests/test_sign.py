import pytest
from src.app import app


@pytest.fixture
def client():
    return app.test_client()


def test_sign_nothing(client):
    response = client.post("/v0/crypto/sign", json={})

    assert response.status_code == 400
    assert response.get_json()["error"] == "bad_request"


def test_sign_something(client):
    payload = {
        "name": "Albert",
        "contact": {"email": "hello@albert.com", "phone": "+1-800-ALBERT-42"},
        "age": 999,
    }
    response = client.post("/v0/crypto/sign", json=payload)

    assert response.status_code == 200
    assert (
        response.get_json()["signature"]
        == "9344b6a38aae164f66752747d997add35f0691f6e2207326afd99be74f8c0ae2"
    )
