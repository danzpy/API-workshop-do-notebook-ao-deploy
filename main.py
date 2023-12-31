from fastapi import FastAPI

# Criando a instância
app = FastAPI()


#Criando rotas

@app.get('/') # Request
def bem_vindo(): # Response
    return {'Seja': 'Bem-vindo'}