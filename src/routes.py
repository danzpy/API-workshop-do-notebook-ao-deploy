from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schema import ProdutosSchema
from .database import SessionLocal, get_db
from .model import Produto

router = APIRouter()

#Criando rotas

@router.get('/') # Request
def bem_vindo(): # Response
    return {'Seja': 'Bem-vindo'}

@router.get('/produtos', response_model=List[ProdutosSchema]) # Request
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all() # Equivale a "SELECT * FROM produtos"


@router.get('/produtos/{id}', response_model=ProdutosSchema)
def seleciona_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.post('/produtos', response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.delete(f'produtos/{id}', response_model=ProdutosSchema)
def remover_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        db.delete(produto)
        db.refresh()
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrados")
    
@router.put(f"produtos/{id}", response_model=ProdutosSchema)
def atualizar_produto(id: int, produto_data: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = db.query(Produto).filter(Produto.id == id).first()
    if db_produto:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh()
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")