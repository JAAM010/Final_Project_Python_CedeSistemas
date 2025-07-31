# web/dashboard_web.py
from fastapi import APIRouter, Request, Cookie, HTTPException
from fastapi.templating import Jinja2Templates
from auth.jwt_handler import verificar_token
from typing import Optional
from services.contenidos_service import obtener_contenidos  # 👈 Importar el servicio

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/dashboard")
async def dashboard(request: Request, access_token: Optional[str] = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="No autorizado")

    token = access_token.replace("Bearer ", "") if access_token.startswith("Bearer ") else access_token
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")

    contenidos = obtener_contenidos()  # 👈 Obtener los contenidos desde el servicio

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "title": "Dashboard",
        "user_id": payload.get("sub"),
        "user_role": payload.get("rol"),
        "contenidos": contenidos  # 👈 Pasar los contenidos a la plantilla
    })
