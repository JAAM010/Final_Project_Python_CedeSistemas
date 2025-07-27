from fastapi import APIRouter , Depends
from typing import List
from schemas.visualizacion import VisualizacionOut
from services.visualizaciones_servive import obtener_visualizacion
from auth.deps import get_current_user, rol_requerido

router = APIRouter()

@router.get("/visualizaciones", response_model=List[VisualizacionOut])
async def listar_visualizaciones(_ = Depends(rol_requerido("admin"))):
    return obtener_visualizacion()
