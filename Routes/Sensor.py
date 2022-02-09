from fastapi import APIRouter
from Database.Models import *
from Database.Connect import conn
from bson.objectid import ObjectId
from Features import *
from Features.DateTime import getNow, getUpdateTime, now
from fastapi.responses import HTMLResponse

sensor = APIRouter()

@sensor.get("/", response_class=HTMLResponse)
async def get_root():
    
    return """
    <html>
        <head>
            <title>Tab Redirect</title>
            <style>    
                a {
                color: #009688;
                font-family: arial;
                font-size: 50px;
                font-style: italic;
                text-decoration: none;
                font-weight: bold;
                }
            </style>
        </head>
        <body>
            <a href="https://sensorcolln01.herokuapp.com/docs">Go to Swagger!</a> 
        </body>
    </html>
    """

# @sensor.post("/Sensors", response_description="Import new data", response_model=SensorSavingModel)
@sensor.post("/Sensors", response_description="Import new data", response_model=SensorEntryModel)
async def save_sensors_data_to_DB(senData: SensorEntryModel):
    
    del senData.timestamp
    del senData.updatedAt
    
    doc = dict((k, v) for k, v in senData.dict().items() if v is not None)
    
    doc['updatedAt'] = getUpdateTime()
    doc['timestamp'] = now()
    
    # fdoc = SensorSavingModel.parse_obj()
    if res := conn.Sensor.insert_one(doc):
        return SensorEntryModel.parse_obj(conn.Sensor.find_one({'_id':ObjectId(res.inserted_id)})) 
    else:
        return False
    
    
@sensor.post("/Tests", response_description="Test", response_model=TestModel)
async def test_request(test: TestModel):
    
    return test


@sensor.get("/Data", response_description="Test", response_model=SensorSavingModel)
def get_newest_data():
    res = conn.Sensor.find().sort("timestamp", -1)
    
    # print(type(res))
    return SensorEntryModel.parse_obj(res[0])

@sensor.delete("/Data/delete", response_description="Test",)
def delete_all_doc():
    if conn.Sensor.delete_many({}):
        return True
    else:
        return False

@sensor.get("/Data/{time}/minutes", response_description="Test")
def get_data_during(time: int):
    present = now()
    time = present - time*60
    data = []
    # res.append(doc for doc in conn.Sensor.find({}) if doc['timestamp'] >= time and doc['timestamp'] <= present)
    res = conn.Sensor.find({})
    
    for rp in res:
        if rp['timestamp'] <= present and rp['timestamp']: 
            data.append(SensorSavingModel.parse_obj(rp))    
        
    return data
    