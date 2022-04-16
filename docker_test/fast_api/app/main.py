from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "universe is, was, will expanding more nad morex"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
