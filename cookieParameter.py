from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()

@app.get("/items")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    if ads_id:
        return {"message": f"Welcome back user {ads_id}"}
    else:
        return {"message": f"No user found with user {ads_id}"}