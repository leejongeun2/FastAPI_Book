from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent  # 현재 경로에서 parent를 하면 부모 폴더를 가리키게 됨 > app

app = FastAPI()

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)  # 응답 타입을 html
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request},
    )


@app.get("/search", response_class=HTMLResponse)  # 응답 타입을 html
async def search(request: Request, q: str):
    print(q)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "keyword": q},
    )


@app.on_event("startup")
async def on_app_start():
    pass
    """
    before app starts
    # """
    # await mongodb.connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    pass
    """
    after app shutdown
    """
    # await mongodb.close()
