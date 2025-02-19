from fastapi import FastAPI, Path, Body
from typing import Annotated
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(title="Body parameters")

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, max_length=300
    )
    price: float = Field(gt=0, title="This is price")
    tax: float | None = None
    tags: list[str]         # to define string list
    tags2: set[str] = set()
    image: Image | None = None
    images: list[Image] | None = None

class User(BaseModel):
    user: str
    contact: int
    email: str | None = None



@app.post("/items/{item_id}")
async def add_items(
    item_id: Annotated[int, Path(title="This is item ID path", ge=0, le=100)],
    p: Annotated[str, Body()],          # body parameter
    item: Item | None = None,
    q: str | None = None,               # query parameter
    user: User | None = None
):
    result = {"Items": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item})
    if user:
        result.update({"user": user})
    return result


@app.put("/updateItems/{item_id}")
async def update_items(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item ID": item_id, "Items": item}
    return results

@app.put("/imageItem/{item_id}")
async def upload_image(item_id: int, image: Image):
    return {"Item": item_id, "Image": image}

@app.post("/indexWeights/")
async def upload_index_weights(weights: dict[int, float]):
    return weights