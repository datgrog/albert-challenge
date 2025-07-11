import pytest
from src.app import app


@pytest.fixture
def client():
    return app.test_client()


def test_encrypt_empty_json(client):
    response = client.post("/v0/crypto/encrypt", json={})

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {}


def test_encrypt_common_json(client):
    expected_common_json = {
        "name": "IkFsYmVydCI=",
        "age": "OTk5",
        "contact": "eyJlbWFpbCI6ICJoZWxsb0BhbGJlcnQuY29tIiwgInBob25lIjogIisxLTgwMC1BTEJFUlQtNDIifQ==",
    }
    payload = {
        "name": "Albert",
        "age": 999,
        "contact": {"email": "hello@albert.com", "phone": "+1-800-ALBERT-42"},
    }

    response = client.post("/v0/crypto/encrypt", json=payload)

    assert response.status_code == 200
    assert response.get_json() == expected_common_json


def test_encrypt_regression(client):
    expected_common_json = {
        "age": "OTk5",
        "appearance": "eyJhY2Nlc3NvcmllcyI6IHsiYmFja3BhY2siOiB7ImNvbnRlbnRzIjogWyJVU0Igc3RpY2siLCAibWluaSBkcm9uZSIsICJlbmVyZ3kgYmFyIl19LCAiaGVhZHNldCI6ICJub2lzZS1jYW5jZWxsaW5nIiwgInNtYXJ0d2F0Y2giOiAicXVhbnR1bSBlZGl0aW9uIn0sICJmZWF0dXJlcyI6IFsiYmlnIGN1cmlvdXMgZXllcyIsICJnbGFzc2VzIiwgIm1vdXN0YWNoZSJdLCAiaGVpZ2h0X2NtIjogNDJ9",
        "contact": "eyJlbWFpbCI6ICJoZWxsb0BhbGJlcnRhaS5jb20iLCAicGhvbmUiOiAiKzEtODAwLUFMQkVSVC00MiIsICJzb2NpYWwiOiB7ImdpdGh1YiI6ICJnaXRodWIuY29tL0FsYmVydEFJIiwgInR3aXR0ZXIiOiAiQEFsYmVydFRoZUJvdCJ9fQ==",
        "description": "Ik1lZXQgQWxiZXJ0LCB0aGUgY3liZXJzZWN1cml0eSBjb21wYW5pb24gdGhhdCBkcml2ZXMgYmV0dGVyIHNlY3VyaXR5IGluIHlvdXIgdGVhbS4i",
        "hobbies": "WyJyZWFkaW5nIHNjaS1maSBub3ZlbHMiLCAicGxheWluZyB2aXJ0dWFsIGNoZXNzIiwgInNvbHZpbmcgcHV6emxlcyJd",
        "name": "IkFsYmVydCI=",
        "skills": "W3sibGV2ZWwiOiAiZXhwZXJ0IiwgIm5hbWUiOiAiTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5nIiwgInllYXJzX2V4cGVyaWVuY2UiOiAyfSwgeyJsZXZlbCI6ICJhZHZhbmNlZCIsICJuYW1lIjogIkRhdGEgQW5hbHlzaXMiLCAieWVhcnNfZXhwZXJpZW5jZSI6IDEuNX0sIHsibGV2ZWwiOiAibWFzdGVyIiwgIm5hbWUiOiAiRnJpZW5kbHkgQ29udmVyc2F0aW9uIiwgInllYXJzX2V4cGVyaWVuY2UiOiAzfV0=",
    }
    payload = {
        "name": "Albert",
        "description": "Meet Albert, the cybersecurity companion that drives better security in your team.",
        "age": 999,
        "appearance": {
            "height_cm": 42,
            "features": ["big curious eyes", "glasses", "moustache"],
            "accessories": {
                "headset": "noise-cancelling",
                "smartwatch": "quantum edition",
                "backpack": {"contents": ["USB stick", "mini drone", "energy bar"]},
            },
        },
        "contact": {
            "email": "hello@albertai.com",
            "phone": "+1-800-ALBERT-42",
            "social": {"twitter": "@AlbertTheBot", "github": "github.com/AlbertAI"},
        },
        "skills": [
            {
                "name": "Natural Language Processing",
                "level": "expert",
                "years_experience": 2,
            },
            {"name": "Data Analysis", "level": "advanced", "years_experience": 1.5},
            {"name": "Friendly Conversation", "level": "master", "years_experience": 3},
        ],
        "hobbies": [
            "reading sci-fi novels",
            "playing virtual chess",
            "solving puzzles",
        ],
    }

    response = client.post("/v0/crypto/encrypt", json=payload)

    assert response.status_code == 200
    assert response.get_json() == expected_common_json
