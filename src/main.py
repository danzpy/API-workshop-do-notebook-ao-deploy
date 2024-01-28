from .data import Produtos
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schema import ProdutosSchema


# Criando instâncias
app = FastAPI()
lista_produtos = Produtos()

#Criando rotas

@app.get('/') # Request
def bem_vindo(): # Response
    return {'Seja': 'Bem-vindo'}

@app.get('/produtos', response_model=list[ProdutosSchema]) # Request
def listar_produtos():
    return lista_produtos.listar_produtos()

@app.get('/produtos/{id}', response_model=ProdutosSchema)
def seleciona_produto(id: int):
    produto = lista_produtos.buscar_produto(id)
    
    if 'Status' in produto and produto['Status'] == 404:
        content = {'Status': 404, 'Mensagem': 'Produto não encontrado'}
        return JSONResponse(content=content, status_code=404)
    
    return produto

@app.post('/produtos', response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    return lista_produtos.adicionar_produto(produto.model_dump())