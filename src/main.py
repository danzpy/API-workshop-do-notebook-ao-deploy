from .data import Produtos
from fastapi import FastAPI
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
    return lista_produtos.buscar_produto(id)



@app.post('/produtos', response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    return lista_produtos.adicionar_produto(produto.model_dump())