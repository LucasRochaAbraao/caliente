import os
import sys
import uvicorn
from typing import Optional
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
import pegar_dados
from config import Config

app = FastAPI()

@app.get("/api")
def read_root():
    response = pegar_dados.temp_hum(Config)

    if response == 404:
        return {"Pagina": "Não encontrada"}

    return response

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}

app.mount("/static", StaticFiles(directory="web_client"), name="static")

templates = Jinja2Templates(directory="web_client")

@app.get("/")
async def web_client(request: Request):
    #temp, hum = pegar_dados.temp_hum(Config)
    response = pegar_dados.temp_hum(Config)

    if response == 404:
        return templates.TemplateResponse("notfound404.html", {"request": request})

    return templates.TemplateResponse("index.html", {
        "request": request,
        "temp": float(response.get('temp')),
        "hum":float(response.get('hum'))
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4200)

