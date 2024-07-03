from typing import Union, Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def get_items(q: Union[str, None] = None):            # q is type of string but could be NONE 
    result = {"items": [{"iems_id": "Hello"}, {"item_id": "World.."}]}
    if q:
        result.update({"q": q})
    return result


@app.get("/items2/")
async def get_items2(q: Annotated[Union[str, None], Query(max_length=50)] = None):          # for adding a query or condition
    result2 = {"items": [{"iems_id": "Hello"}, {"item_id": "Query.."}]}
    if q:
        result2.update({"q": q})
    return result2


@app.get("/items3/")
async def get_items3(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):          # for adding a query or condition
    result3 = {"items": [{"iems_id": "Hello"}, {"item_id": "Query.."}]}
    if q:
        result3.update({"q": q})
    return result3


# Query parameter list/multiple values
@app.get("/items4/")
async def get_items4(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

# Declare more metadata
@app.get("/items5/")
async def get_items5(
    q: Annotated[
        str | None, 
        Query(
            title="Query string", 
            description="This is a string API description",
            min_length=3
            )
    ] = None):
    result5 = {"items5": [{"item_id": "Hello..."}, {"item_id": "World"}]}
    if q:
        result5.update({"q": q})
    return result5