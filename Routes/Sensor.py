from fastapi import APIRouter
from Database.Models import SensorEntryModel
from Database.Connect import conn

sensor = APIRouter()

@sensor.post("/ctfs/create", response_description="Add new sensor data")
async def create_data(senData: SensorEntryModel):
    
    return senData

