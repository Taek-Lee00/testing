from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
<<<<<<< HEAD
    return {"msg": "Hello, World!"}
=======
    return {"Hello": "World"}
>>>>>>> 893ef666b376b683ed077ee39a01df34a6cb21df


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
