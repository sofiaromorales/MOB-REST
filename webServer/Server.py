from fastapi import FastAPI, HTTPException
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

# GET object by name
@app.get('/api/objects/{object_name}')
async def fetch_object(object_name: str):
    for object in objects:
        if object.name == object_name:
            return object
    raise HTTPException(status_code=404, detail='Objet Not Found')

# POST create new object
@app.post('/api/objects')
async def create_object(object: Object):
    # If name has blank space turn it into skewer-case
    object.name = object.name.replace(' ', '-')
    # Look for repeated object and if exists return code 409
    for obj in objects:
        if object.name == obj.name:
            raise HTTPException(status_code=409, detail='Object Already Exists')
    object.date_created = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    objects.append(object)
    return { 'name' : object.name }

# DELETE object by name
@app.delete('/api/objects/{object_name}')
async def fetch_object(object_name: str):
    for object in objects:
        if object.name == object_name:
            objects.remove(object)
            return { 'name' : object_name }
    raise HTTPException(status_code=404, detail='Object Not Found')
