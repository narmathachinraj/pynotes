---
title: Prog
date: 2026-04-18
author: Your Name
cell_count: 2
score: 0
---

```python

```


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample in-memory "database"
items = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Phone", "price": 500}
]

# -----------------------
# GET endpoint
# -----------------------
@app.get("/items")
def get_items():
    return {"items": items}


# -----------------------
# POST endpoint
# -----------------------

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "price": item.price
    }
    items.append(new_item)
    return {
        "message": "Item created",
        "item": new_item
    }
```


---
**Score: 0**