from typing import Optional
from pydantic import BaseModel

class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str 

from fastapi import FastAPI, HTTPException

web = FastAPI()

mensajes_db = []

@web.post("/mensajes/", response_model=Mensaje)
def crear_mensaje(mensaje : Mensaje):
    mensaje.id = len(mensajes_db) +1
    mensajes_db.append(mensaje)
    return mensaje
