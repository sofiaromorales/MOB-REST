from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from datetime import datetime
import logging
from ObjectModel import Object
import ApplicationClient

import json


app = FastAPI()

FORMAT = "%(levelname)s:%(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

#objects: List[Object] = [
#    Object(
#        name = 'Object1',
#       date_created = '01/20/2022'
#     ),
#     Object(
#         name = 'Object2',
#        date_created = '01/20/2022'
#     )
# ]

with open('data.json', 'w') as fp:
        objects= []
        json.dump(objects, fp, sort_keys=True, indent=4)        

## --OBJECT CRUD--

# GET list of objects
@app.get('/api/objects')
async def fetch_objects():
    return objects

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
    data= []
    for o in objects:
        d={
            "name": o.name,
            "date_created": o.date_created
        }
        data.append(d)
    with open('data.json', 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)
    return { 'name' : object.name }

# DELETE object by name
@app.delete('/api/objects/{object_name}')
async def fetch_object(object_name: str):
    for object in objects:
        if object.name == object_name:
            objects.remove(object)
            data= []
            for o in objects:
                d={
                    "name": o.name,
                    "date_created": o.date_created
                }
                data.append(d)
            with open('data.json', 'w') as fp:
                json.dump(data, fp,sort_keys=True, indent=4)
            return { 'name' : object_name }
    raise HTTPException(status_code=404, detail='Object Not Found')

## --COORDINATOR OPERATIONS--

# REPLICATE with vote_request
## vote_request = commit || abort || randomize
@app.post('/api/coordinator/replicate/{vote_request}')
async def request_replication(vote_request: str):
    res = ApplicationClient.getCoordinatorReplica(vote_request, objects)
    if (res) == 1:
        raise HTTPException(status_code=200, detail='Replication succeded')
    else:
        raise HTTPException(status_code=404, detail='Replication not succeded')

# RESTORE data from replication servers
@app.get('/api/coordinator/restore')
async def request_restore():
    restore = ApplicationClient.getObjectsRestore()
    for d in restore:
        o= Object(name=d["name"], date_created=d["date_created"])
        objects.append(o)
    with open('data.json', 'w') as fp:
        json.dump(restore, fp,sort_keys=True, indent=4)
    raise HTTPException(status_code=200, detail='Restore succeded')
