from fastapi import FastAPI
from crud import cadastrar_cliente, procurar_cliente, alterar_dados_paciente,deletar_paciente
from schemas import PacienteCreate,PacienteUpdate

app = FastAPI()

@app.get('/')
def home():
    return {"mensagem": "Bem-Vindo ao Sistema do Hospital"}

@app.post('/pacientes')
def criar_paciente(paciente : PacienteCreate):
    return cadastrar_cliente(paciente.nome, paciente.telefone, paciente.email)

@app.get('/pacientes/{id}')
def buscar_paciente(id : int):
    return procurar_cliente(id)

@app.put('/pacientes/{id}')
def alterar_dados(id : int, paciente : PacienteUpdate):
    return alterar_dados_paciente(paciente.nome, paciente.telefone, paciente.email,id)

@app.delete('/pacientes/{id}')
def deletar(id : int):
    return deletar_paciente(id)