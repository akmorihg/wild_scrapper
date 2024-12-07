import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from data import read_excel, append_to_df
from models import ItemCollection, Item

DATA_PATH = "data.xlsx"

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://www.wildberries.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/items/")
async def create_item(item_collection: ItemCollection):
    df: pd.DataFrame = read_excel(DATA_PATH)
    append_to_df(df, item_collection)
    return item_collection

@app.get("/excels/")
async def get_excel():
    read_excel(DATA_PATH)
    return FileResponse(path=DATA_PATH, filename="Сбор данных.xlsx", media_type='multipart/form-data')
