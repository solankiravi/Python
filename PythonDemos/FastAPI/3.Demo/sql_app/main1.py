
from typing import List
from fastapi import FastAPI

from models import ProjectModel, CoeModel,StreamModel

app = FastAPI()

project_fake_db: List[ProjectModel] =  []
stream_fake_db: List[StreamModel]=[]
coe_fake_db: List[CoeModel]=[]

#region Project
@app.get('/')
async def getAllProjects():
    return project_fake_db

@app.post('/create_project')
def createProject(obj: ProjectModel):
    project_fake_db.append(obj)
    return obj
#endregion

#region Streams
@app.get('/getstreams')
async def getAllProjects():
    return stream_fake_db

@app.post('/create_streams')
def createProject(obj: StreamModel):
    stream_fake_db.append(obj)
    return obj
#endregion

#region Coes
@app.get('/getcoes')
async def getAllProjects():
    return coe_fake_db

@app.post('/create_coe')
def createProject(obj: CoeModel):
    coe_fake_db.append(obj)
    return obj
#endregion