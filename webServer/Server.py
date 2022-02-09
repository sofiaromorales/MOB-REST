from fastapi import FastAPI
from typing import List
from uuid import UUID, uuid4

from ObjectModel import Object

app = FastAPI()

objects: List[Object] = [
    Object(
        id = uuid4(),
        name = 'Object1',
        date_created = '01/20/2022'
    ),
    Object(
        id = uuid4(),
        name = 'Object2',
        date_created = '01/20/2022'
    )
]

@app.get('/')
def root():
    return { 'Hello' : 'World' }

@app.get('/api/objects')
async def fetch_objects():
    return objects;
