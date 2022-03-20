import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def hello_world():
    return { "message": "hello"}


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.get("/start", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("start.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app)