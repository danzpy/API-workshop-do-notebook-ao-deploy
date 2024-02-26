from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schema import ProdutosSchema
from .routes import router
from typing import List


# Criando instâncias
app = FastAPI()

app.include_router(router)

