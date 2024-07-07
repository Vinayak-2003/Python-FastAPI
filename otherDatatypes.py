from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel

from datetime import datetime, time, timedelta
import uuid

app = FastAPI()

@app.put("/items/{item_id}")
async def update_time(
    item_id: int,
    start_datetime: Annotated[datetime, Body()],            # Annotated needs atleast 2 arguments
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()]
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_datetime

    return{
        "item ID": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after, 
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration
    }