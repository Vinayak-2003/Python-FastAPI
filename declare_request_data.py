from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(examples=["rohan"])
    description: str | None = Field(default=None, example=["name is"])
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