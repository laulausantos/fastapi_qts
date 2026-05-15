from fastapi import FastAPI

app  = FastAPI()

@app.get("/")
def raiz():
    return { "mensagem" : "API FatsAPI Funcionando." }

@app.get("/health")
def health():
    return{ "status": "ok" }

@app.get("soma")
def soma (a: int, b: int):
    return {"resultado": a + b}

from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str
    concluido: bool = False

@app.post("/tarefa")
def criar_tarefa(tarefa : Tarefa):
    return {
        "mensagem": "Tarefa recebida com sucesso",
        "dados" : tarefa
    }
