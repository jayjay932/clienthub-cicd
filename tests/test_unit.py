from api.app import app

def test_health():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_json() == {"status": "ok"}

def test_clients():
    with app.test_client() as client:
        response = client.get("/clients")
        assert response.status_code == 200
        assert response.get_json() == [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
        ]
