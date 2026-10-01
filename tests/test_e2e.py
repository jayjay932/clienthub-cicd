import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:5002")


def test_health_http():
    response = requests.get(f"{BASE_URL}/health", timeout=10)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_clients_http():
    response = requests.get(f"{BASE_URL}/clients", timeout=10)
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
