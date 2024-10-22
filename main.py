from typing import Optional
from pydantic import BaseModel

class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str 

from fastapi import FastAPI, HTTPException

web = FastAPI()

mensajes_db = []
