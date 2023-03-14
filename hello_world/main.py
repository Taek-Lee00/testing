import os
from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"msg": f"""hello, {os.environ['FOO']} """}


@app.get("/")
def read_root():
    return {"msg": f"""hello, {"world"} """}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def main():
    uvicorn.run("hello_world.main:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
