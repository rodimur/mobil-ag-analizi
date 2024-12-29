from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_analyze_url():
    response = client.get("/threats?url=https://example.com")
    assert response.status_code == 200
    assert response.json() == {"url": "https://example.com", "status": "Safe"}
