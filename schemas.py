from pydantic import BaseModel

class PacienteCreate(BaseModel):
    nome: str
    telefone: str
    email: str
class PacienteUpdate(BaseModel):
    nome: str
    telefone: str
    email: str

