from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()

@app.get("/items")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"user-agent": user_agent}

@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}