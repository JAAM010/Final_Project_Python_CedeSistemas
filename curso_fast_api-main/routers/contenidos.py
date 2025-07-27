from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from services.contenidos_service import obtener_contenidos
from typing import List
from schemas.contenido import ContenidoOut, ContenidoCreate
from services.contenidos_service import obtener_contenidos, crear_contenido
from auth.deps import get_current_user, rol_requerido


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/contenidos")
async def ver_contenidos(request: Request):
    contenidos = obtener_contenidos()
    return templates.TemplateResponse("contenidos.html", {
        "request": request,
        "contenidos": contenidos,
        "title": "Catálogo"
    })


@router.post("/contenidos", response_model=ContenidoOut, status_code=201)
async def crear(contenido: ContenidoCreate,_ = Depends(rol_requerido("admin"))):
    return crear_contenido(contenido) 