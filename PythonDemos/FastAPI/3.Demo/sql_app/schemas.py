from typing import Any, List, Optional

from pydantic import BaseModel

#region Coe
class CoeBase(BaseModel):
    id: int
    name:str
    modelyear_id: int

class CoeCreate(CoeBase):
    pass

class CoeModel(CoeBase):
    pass

#endregion 

#region ModelYear
class ModelYearBase(BaseModel):
    id:int
    name:str

class ModelYearCreate(ModelYearBase):
    pass

class ModelYearModel(ModelYearBase):
    coes= CoeModel
    class Config:
        orm_mode=True
#endregion


   

#region streams
class StreamBase(BaseModel):
    id=int
    name:str
    modelyear_id: int
    modelyears: List[ModelYearModel]

class StreamCreate(StreamBase):
    pass

class StreamModel(StreamBase):
    pass

#endregion

class ProjectModel(BaseModel):
    id=int
    name:str
    modelyear:ModelYearModel
    streams:  List[StreamModel] 
