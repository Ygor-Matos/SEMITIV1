from pydantic import BaseModel
from typing import Optional

class Cadeira(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = "Curso tecnologico"

    def __str__(self):
        return f"Cadeira: {self.nome} ID: {self.id} Descricao: {self.descricao}"
