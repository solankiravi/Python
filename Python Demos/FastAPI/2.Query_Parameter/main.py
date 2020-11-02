from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description: Optional[str]=None
    price: float
    tax: Optional[float]=None


app=FastAPI()

fake_db=[{'task1':'Task 1'},{'task2':'Task 2'},{'task3':'Task 3'}]


@app.get('/items')
async def get_items(skip: int =0 , limit:int=3):
    return fake_db[skip: skip+limit]

@app.post('/items/')
async def create_item(item:Item):
    item_dict=item.dict()
    if(item.tax):
        price_with_tax= item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get('/items/{item_name}')
async def get_item(item_name: str, description: Optional[str] = None):
    itemname='NA'
    print(description)
    desc= description if description else 'NA'
    for task in fake_db:
        if item_name in task:
            item_name=item_name
            return item_name

    return {'itemname': itemname , 'description': desc}

