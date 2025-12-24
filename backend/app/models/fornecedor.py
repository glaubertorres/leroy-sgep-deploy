from pydantic import BaseModel, Field
from typing import Optional

class Fornecedor(BaseModel):
    cnpj: str = Field(..., max_length=14)
    nome: str = Field(..., max_length=100)
    politica_devolucao: Optional[str] = Field(..., max_length=500, description="Descrição da política de devolução")
    contato: Optional[str] = None
    status_forn : bool = Field(default=True)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "cnpj": "12345678000190",
                    "nome": "Master Química S.A.",
                    "politica_devolucao": 60,
                    "contato": "contato@empresa.com",
                    "status_forn": True
                }
            ]
        }
    }