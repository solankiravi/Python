
from pydantic import BaseModel

class ModelYearBase(BaseModel):
    id:int
    name:str
    is_active:bool

class ModelYearCreate(ModelYearBase):
    pass

class ModelYear(ModelYearBase):
    class Config:
        orm_mode = True
