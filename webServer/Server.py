from fastapi import FastAPI
from typing import List
from uuid import UUID, uuid4
from datetime import datetime

from ObjectModel import Object

app = FastAPI()

objects: List[Object] = [
    Object(
        name = 'Object1',
        date_created = '01/20/2022'
    ),
    Object(
        name = 'Object2',
        date_created = '01/20/2022'
    )
]


# GET list of objects
@app.get('/api/objects')
async def fetch_objects():
    return objects;

# POST create new object
@app.post('/api/objects')
async def create_object(object: Object):
    #TODO: Look for repeated object and if exists return code 409
    #TODO: if name has blank space turn it into skewer-case
    object.date_created = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    objects.append(object)
    return { 'name' : object.name }
