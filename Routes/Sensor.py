from fastapi import APIRouter
from Database.Models import SensorEntryModel, SensorSavingModel
from Database.Connect import conn
from bson.objectid import ObjectId
from Features import *
from Features.DateTime import getNow, getUpdateTime, now

sensor = APIRouter()

@sensor.post("/ctfs/create", response_description="Add new sensor data")
async def create_data(senData: SensorEntryModel):
    
    doc = dict((k, v) for k, v in senData.dict().items() if v is not None)
    doc['updatedAt'] = getUpdateTime()
    doc['timestamp'] = now()
    
    # fdoc = SensorSavingModel.parse_obj()
    
    if res := conn.Sensor.insert_one(doc):
        return True
    else:
        return False
    

