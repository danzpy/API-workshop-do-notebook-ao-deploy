from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_status_code():
    response = client.get('/')
    assert response.status_code == 200

def test_response():
    response = client.get('/')
    assert response.json() == {"Seja": "Bem-vindo"}
    