from typing import Optional

from pydantic import BaseModel


class CoeModel(BaseModel):
    name:str

class StreamModel(BaseModel):
    name:str
    coes: (list(CoeModel))

class ProjectModel(BaseModel):
    name:str
    modelyear:str
    streams:  (list(StreamModel))