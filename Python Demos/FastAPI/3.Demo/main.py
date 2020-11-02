
from fastapi import FastAPI

from models import ProjectModel, CoeModel,StreamModel

app = FastAPI()

@app.get('/')
async def index():
    return ProjectModel