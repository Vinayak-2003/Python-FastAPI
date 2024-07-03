from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of item to get", gt=0, le=100)],
    q: Annotated[str|None, Query(alias="item-query")] = None
):
    results = {"items": item_id}
    if q:
        results.update({"q": q})
    return results