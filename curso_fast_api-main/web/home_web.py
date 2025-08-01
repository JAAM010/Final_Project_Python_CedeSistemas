from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "title": "StreamFlix - Tu plataforma de contenido"
    })