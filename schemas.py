from pydantic import BaseModel

class PacienteCreate(BaseModel):
    nome: str
    telefone: str
    email: str
    
    
        