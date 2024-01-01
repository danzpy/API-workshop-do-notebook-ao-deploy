from fastapi.testclient import TestClient
from main import app
from main import produtos


client = TestClient(app)


def test_status_code():
    response = client.get('/')
    assert response.status_code == 200

def test_response():
    response = client.get('/')
    assert response.json() == {"Seja": "Bem-vindo"}
 
def listar_produtos_status_code():
    response = client.get('/produtos')
    assert response.status_code == 200


def listar_produtos_response():
    response = client.get('/produtos')
    assert response.json() == produtos