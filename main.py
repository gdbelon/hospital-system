from fastapi import FastAPI
from crud import cadastrar_cliente, procurar_cliente
from schemas import PacienteCreate

app = FastAPI()

@app.get('/')
def home():
    return {"mensagem": "API do ospital funcionando"}

@app.post('/pacientes')
def criar_paciente(paciente: PacienteCreate):
    cadastrar_cliente(paciente.nome,paciente.telefone,paciente.email)

@app.get('/pacientes/buscar')
def buscar_paciente(nome: str, telefone: str):
    return procurar_cliente(nome, telefone)