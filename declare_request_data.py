from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str = Field(examples=["rohan"])
    description: str | None = Field(default=None, examples=["name is"])
    price: float = Field(examples=[12.3])
    tax: float | None = Field(default=None, examples=[2.2])

# The schema_extra with the examples key provides a sample example of how an Item object should look.
# Purpose: Provide examples for documentation.
# for pyhton 3.10+ pydantic v1
    class config:
        schema_extra = {
            "examples": [ 
                {
                    "name": "Vinayak",
                    "description": "My name",
                    "price": 20000,
                    "tax": 20.23
                }
            ]
        }

# for python 3.10+ pydantic v2
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Vinayak",
                    "description": "My name",
                    "price": 20000,
                    "tax": 20.23
                }
            ]
        }
    }

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    results = {"item ID": item_id, "Items": item}
    return results


@app.put("/bodyItems/{item_id}")
def bodyItems(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[                    # doesn't support showing multiple examples in JSON Schema in UI documentation
                {
                    "name": "Vinayak",
                    "description": "My name",
                    "price": 20000,
                    "tax": 20.23
                },
                {
                    "name": "Vinayak",
                    "price": 20000
                }
            ]
        )
    ]
):
    result = {"item ID": item_id, "items": item}
    return result


# using openapi_examples
@app.put("/openItems/{item_id}")
async def openapi_items(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "Normal": {
                    "summary": "A normal example",
                    "description": "A **normal** example works correctly",
                    "value": {
                        "name": "soap",
                        "description": "bathing/washing soaps",
                        "price": 50.00,
                        "tax": 5.50
                    }
                },
                "converted": {
                    "summary": "A converted example",
                    "description": "FastAPI can convert price strings to numbers automatically",
                    "value": {
                        "name": "oil",
                        "price": "200"
                    }
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "maggie",
                        "price": "twenty five"
                    }
                }
            }
        )
    ]
):
    result = {"item ID": item_id, "item": item}
    return result