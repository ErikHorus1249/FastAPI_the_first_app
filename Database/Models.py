from ast import Dict
from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
import uuid
import datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class AccelerometerModel(BaseModel):
    accX: float
    accY: float
    accZ: float

class GyroscopeModel(BaseModel):
    gyX: float
    gyY: float
    gyZ: float

class TempvsHumiModel(BaseModel):
    temp: float
    humi: float
    mois: float
    
class SensorEntryModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    accX: float
    accY: float
    accZ: float
    gyX: float
    gyY: float
    gyZ: float
    temp: float
    humi: float
    mois: float
    rain: float
    updatedAt: str
    timestamp: float
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
class SensorEntityModel(BaseModel):
    accX: float
    accY: float
    accZ: float
    gyX: float
    gyY: float
    gyZ: float
    temp: float
    humi: float
    mois: float
    rain: float
    
class SensorSavingModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    accX: float
    accY: float
    accZ: float
    gyX: float
    gyY: float
    gyZ: float
    temp: float
    humi: float
    mois: float
    rain: float
    updatedAt: str
    timestamp: float
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
# class SensorSavingModel(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     acc: AccelerometerModel
#     gy: GyroscopeModel
#     tvh: TempvsHumiModel
#     rain: float
#     updatedAt: str
#     timestamp: float
    
#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
    
# class SensorSavingModel(BaseModel):
#     email: str
#     user_ip: str
#     info: Info

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "email": "admin@gmail.com",
#                 "user_ip": "127.0.0.1",
#                 "info": {
#                     "idThucHanh": "",
#                     "attempt": 1,
#                     "timestamp": []
#                 }
#             }
#         }


class TestModel(BaseModel):
    acc: AccelerometerModel