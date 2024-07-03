# -----------------------PATH PARAMETERS----------------------------- #
from fastapi import FastAPI

app = FastAPI()                     # fastapi instance

@app.get("/")                       # path operation decorator
async def root():
    return {"message": "Hello World..."}

@app.get("/items/me")
async def read_my_items():
    return {"Name": "Vinayak Kanchan"}

@app.get("/items/{item_name}")
async def read_name(item_name: str):
    return {"Name": item_name}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file path": file_path}


# -----------------------PREDEFINED VALUES----------------------------- #
from enum import Enum

class modelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "Lenet"

@app.get("/models/{model_name}")
async def read_model(model_name):
    if model_name == modelName.alexnet:
        return {"model": modelName.alexnet, "Message": "Hello from AlexNet"}
    
    if model_name == modelName.resnet:
        return {"model": model_name, "Message": "Hello from ResNet"}
    
    return {"model": modelName.lenet.value, "Message": 'Hello from LeNet'}


# -----------------------QUERY PARAMETERS----------------------------- #

fake_items_db = [{"item_name": "1"}, {"item_name": "2"}, {"item_name": "3"},
                 {"item_name": "4"}, {"item_name": "5"}, {"item_name": "6"},
                 {"item_name": "7"}, {"item_name": "8"}, {"item_name": "9"}
                ]

@app.get("/fakeItems/")
async def read_fake_items(skip: int, limit: int=10, q: int | None = None):
    return {"q": q, "body": fake_items_db[skip: skip+limit]}


@app.get("/users/{user_name}/newItems/{item_id}")
async def new_items(item_id: int, user_name: str, q: str | None = None, short: bool = False):
    item = {"item id": item_id, "user id": user_name}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an item"}
        )
    return item