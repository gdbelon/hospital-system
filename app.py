from fastapi import FastAPI
from crud import cadastrar_cliente, procurar_cliente, alterar_dados_paciente
from schemas import PacienteCreate

app = FastAPI()

@app.get('/')
def home():
    return {"mensagem": "Bem-Vindo ao Sistema do Hospital"}

@app.post('/pacientes')
def criar_paciente(nome: str, telefone: str, email: str):
    cadastrar_cliente(nome,telefone,email)

@app.get('/pacientes/buscar')
def buscar_paciente(nome: str):
    return procurar_cliente(nome)

@app.put('/pacientes/alterar-dados')
def alterar_dados(nome: str, telefone: str, email: str, id: int):
    return alterar_dados_paciente(nome,telefone,email,id)