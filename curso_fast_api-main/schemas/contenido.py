from datetime import date
from pydantic import BaseModel
from typing import Optional
from enum import Enum



class TipoContenido(str, Enum):
    pelicula = 'pelicula'
    serie = 'serie'

class ContenidoOut(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str]
    fecha_lanzamiento: Optional[date]
    tipo_contenido: TipoContenido

class ContenidoCreate(BaseModel):
    
    titulo: str
    descripcion: Optional[str]
    fecha_lanzamiento: Optional[str]
    tipo_contenido: TipoContenido