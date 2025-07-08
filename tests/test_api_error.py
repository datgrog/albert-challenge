import pytest
from src.app import app


@pytest.fixture
def client():
    return app.test_client()


def test_decrypt_bad_json(client):
    response = client.post(
        "/v0/crypto/decrypt", data="{bad json", content_type="application/json"
    )
    assert response.status_code == 400
    assert response.get_json()["error"] == "bad_request"


def test_decrypt_weird_json_number(client):
    response = client.post(
        "/v0/crypto/decrypt", data="432678543234526", content_type="application/json"
    )
    assert response.status_code == 500
    assert response.get_json()["error"] == "internal_server_error"


def test_decrypt_weird_json_string(client):
    response = client.post(
        "/v0/crypto/decrypt", data='"just a string"', content_type="application/json"
    )
    assert response.status_code == 500
    assert response.get_json()["error"] == "internal_server_error"


def test_decrypt_weird_json_list(client):
    response = client.post(
        "/v0/crypto/decrypt", data='["a", "b", "c"]', content_type="application/json"
    )
    assert response.status_code == 500
    assert response.get_json()["error"] == "internal_server_error"
