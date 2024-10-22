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

@web.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
