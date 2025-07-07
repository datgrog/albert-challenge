# from albert_home_challenge.src.app import app

from src.app import app


# TODO: fixture
def test_ping():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"message": "pong"}
