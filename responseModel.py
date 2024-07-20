from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()

class mainItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tags: list[str] = []

class Item(mainItem):
    tax: float | None = None

class Item2(mainItem):
    tax: float = 10.5

class mainUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class User(mainUser):                   # as we don't want our password to be displayed to all the clients
    password: str



@app.post("/items", response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get("/items", response_model=list[Item])
async def read_item() -> Any:
    return [
        Item(name="Guns", price=50.00),
        Item(name="Bombs", price=30.50, tax=15.00)
    ]

@app.post("/user", response_model=mainUser)
async def create_user(user: User) -> Any:
    return user

@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.tatacliq.com/puma-mens-smooth-walk-black-running-shoes/p-mp000000014657201")
    return JSONResponse(content={"message": "Here is your portal"})


items = {
    "foo": {"name": "Foo", "price": 54},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
}

# default values won't be included in the response, only the values actually set
@app.get("/items/{item_id}", response_model=Item2, response_model_exclude_unset=True)
async def read_items2(item_id: str):
    return items[item_id]

# only particular values included
@app.get("/items/{item_id}", response_model=Item2, response_model_include=({"name", "description"}))
async def read_items3(item_id: str):
    return items[item_id]

# only particular value excluded
@app.get("/items/{item_id}", response_model=Item2, response_model_exclude=({"tax"}))
async def read_items4(item_id: str):
    return items[item_id]