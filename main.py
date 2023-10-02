from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Nota
from core import Core

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000"],
                   allow_credentials=True,
                   allow_methods=["POST"],
                   allow_headers=["*"],
                   )


@app.get("/")
async def root():
    return {"Response": "Service On!"}


@app.post("/items/")
async def create_item(item_: Nota):
    o_core = Core()
    o_core.parse_json(item_)
    return {"item": item_}
