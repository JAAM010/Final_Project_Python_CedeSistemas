from pydantic import BaseModel
from typing import Optional
from enum import Enum

class VisualizacionOut(BaseModel):
    nombre: str
    titulo:str
    fecha_visualizacion: Optional[str]