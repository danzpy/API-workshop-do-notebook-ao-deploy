from fastapi.testclient import TestClient
from src.main import app
from src.main import produtos


client = TestClient(app)


def test_status_code():
    response = client.get('/')
    assert response.status_code == 200

def test_response():
    response = client.get('/')
    assert response.json() == {"Seja": "Bem-vindo"}
 
def test_listar_produtos_status_code():
    response = client.get('/produtos')
    assert response.status_code == 200


def test_listar_produtos_response():
    response = client.get('/produtos')
    assert response.json() == produtos

def test_buscar_produto_inexistente():
    response = client.get('/produtos/9999')
    assert response.json() == {'Status': 404, 'Mensagem': 'Produto não encontrado'}

def test_buscar_produto_existente():
    response = client.get('/produtos/1')
    assert response.json() == {
        'id': 1,
        'nome': 'iPhone 14',
        'descricao': 'Apple iPhone 14 128GB Meia-Noite 5G Tela 6,1" Câm. Traseira 12+12MP Frontal 12MP',
        'preco': 4699.00,
    }