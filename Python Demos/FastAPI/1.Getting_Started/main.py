from fastapi import FastAPI
from enum import Enum
#Create app
app = FastAPI()

class Items(str,Enum):
    item1='Item 1'
    item2="Item 2"
#Index
@app.get('/')
async def index():
    return {'message': 'Hello Fast API.'}
#Items/1
@app.get('/items/{item}')
async def get_items(item:Items):
    if(item == Items.item1):
        return {'item name': item, 'description': 'Some random text for item1'}
    if(item == Items.item2):
        return {'item name': item, 'description': 'Some random text for item2'}
    return {'item-name':'Invalid'}
