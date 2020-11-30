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

app = FastAPI()

temp, hum = pegar_dados.temp_hum()

@app.get("/api")
def read_root():
    return {
        "temp": temp,
        "hum" : hum
    }

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}

app.mount("/static", StaticFiles(directory="web_client"), name="static")

templates = Jinja2Templates(directory="web_client")

@app.get("/")
async def web_client(request: Request):
    print(temp, hum)
    return templates.TemplateResponse("placeholder.html", {
        "request": request,
        "temp": float(temp),
        "hum":float(hum)
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4200)
