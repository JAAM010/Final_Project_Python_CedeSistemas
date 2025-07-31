from fastapi import APIRouter, Depends, Request ,Form
from typing import List
from schemas.user import UserCreate, UserResponse
from services.usuarios_service import obtener_usuarios, crear_usuario, obtener_usuario_por_id, eliminar_usuario
from auth.deps import get_current_user, rol_requerido
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates



templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/usuarios", response_model=List[UserResponse])
async def listar_usuarios(skip: int = 0, limit: int = 100, _ =Depends(rol_requerido("admin"))):
    return obtener_usuarios(skip=skip, limit=limit)

@router.post("/usuarios", response_model=UserResponse, status_code=201)
async def crear(usuario: UserCreate,_ =Depends(rol_requerido("admin")) ):
    return crear_usuario(usuario)

@router.delete("/usuarios/{id}", response_model=UserResponse, status_code=200)
async def eliminar(id:int,_ =Depends(rol_requerido("admin"))):
    return eliminar_usuario(id)

@router.get("/usuarios/{id}", response_model=UserResponse)
async def get_usuario(id:int,_ =Depends(rol_requerido("admin"))):
    return obtener_usuario_por_id(id)

@router.get("/registro", response_class=HTMLResponse)
async def mostrar_registro(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@router.post("/registro", response_class=HTMLResponse)
async def registrar_usuario(request: Request, usuario: UserCreate):
    try:
        crear_usuario(usuario)
        return JSONResponse(content={"mensaje": "Usuario creado con éxito"}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=400)
"""@router.get("/usuarios/{id}", response_model=UserResponse)
async def get_usuario(id: int, usuario_actual: UserResponse = Depends(obtener_usuario_actual)):
    return obtener_usuario_por_id(id)"""