from fastapi.testclient import TestClient
from src.main import app
from pydantic import ValidationError
from src.schema import ProdutosSchema
import pytest

client = TestClient(app)


def test_status_code():
    response = client.get('/')
    assert response.status_code == 200

def test_status_code_produtos():
    response = client.get('/produtos')
    assert response.status_code == 200

@pytest.fixture
def test_client():
    """
    Cria uma instância de TestClient que pode ser usada em testes.
    O TestClient é utilizado para simular requisições à API FastAPI.
    """
    with TestClient(app) as client:
        yield client

def test_listar_produtos(test_client):
    """
    Testa se a rota GET '/produtos' retorna uma lista e um status code 200 (sucesso).
    Verifica se a resposta é uma lista, indicando uma listagem bem-sucedida dos produtos.
    """
    response = test_client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_modelo_produto_invalido():
    with pytest.raises(ValidationError):
        ProdutosSchema(titulo="", preco=-10.0)