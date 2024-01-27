from fastapi import FastAPI
from typing import List, Dict

# Criando a instância
app = FastAPI()

#Criando rotas

@app.get('/') # Request
def bem_vindo(): # Response
    return {'Seja': 'Bem-vindo'}

produtos: List[Dict[str, any]] = [
    {
        'id': 1,
        'nome': 'iPhone 14',
        'descricao': 'Apple iPhone 14 128GB Meia-Noite 5G Tela 6,1" Câm. Traseira 12+12MP Frontal 12MP',
        'preco': 4699.00,
    },

    {
        'id': 2,
        'nome': 'ThinkPad L14',
        'descricao': 'Notebook ThinkPad L14 (14” Intel)',
        'preco': 3328.00,
    },

    {
        'id': 3,
        'nome': 'iPad 10.9',
        'descricao': 'Apple iPad 10.9" 10ª Geração, Wi-Fi, 256GB, Prateado',
        'preco': 4699.00,
    }
]

@app.get('/produtos') # Request
def listar_produtos():
    return produtos


@app.get('/produtos/{id}')

def seleciona_produto(id: int):
    for produto in produtos:
        if produto['id'] == id:
            return produto
    return {'Status': 404, 'Mensagem': 'Produto não encontrado'}
