from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar la carpeta "static" para incluir archivos CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar templates con Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    """
    Endpoint para cargar el formulario HTML.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/contar-palabras", response_class=HTMLResponse)
async def contar_palabras(request: Request, texto: str = Form(...)):
    """
    Endpoint para contar palabras en un texto.
    """
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    return templates.TemplateResponse("result_template.html", {"request": request, "texto": texto, "cantidad_palabras": cantidad_palabras})
