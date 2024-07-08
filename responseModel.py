from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class UserIn(BaseModel):
    usename: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):                   # as we don't want our password to be displayed to all the clients
    username: str
    email: EmailStr
    full_name: str | None = None



@app.post("/items", response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get("/items", response_model=list[Item])
async def read_item() -> Any:
    return [
        Item(name="Guns", price=50.00),
        Item(name="Bombs", price=30.50, tax=15.00)
    ]

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user