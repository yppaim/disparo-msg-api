from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)
HEADERS = {"X-API-Key": "portfolio-dev-key"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_send_message():
    payload = {
        "recipient": "cliente@example.com",
        "message": "Seu pedido foi confirmado.",
        "channel": "email",
    }

    response = client.post("/messages", json=payload, headers=HEADERS)

    assert response.status_code == 201
    body = response.json()

    assert body["recipient"] == payload["recipient"]
    assert body["status"] == "sent"
    assert "id" in body


def test_invalid_api_key():
    response = client.post(
        "/messages",
        json={
            "recipient": "cliente@example.com",
            "message": "Teste",
            "channel": "email",
        },
        headers={"X-API-Key": "wrong-key"},
    )

    assert response.status_code == 401


def test_invalid_message():
    response = client.post(
        "/messages",
        json={
            "recipient": "",
            "message": "Teste",
            "channel": "email",
        },
        headers=HEADERS,
    )

    assert response.status_code == 422
