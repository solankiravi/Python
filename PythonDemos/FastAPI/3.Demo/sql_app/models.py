from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String

from .database import Base

class ModelYear(Base):
    __tablename__ = 'modelyear'
    id= Column(Integer, primary_key=True, index=True)
    name=Column(String,unique=True,index=True)
    coes=relationship("Coes", uselist=False, backref="modelyear")

class Coes(Base):
    __tablename__="coes"
    id= Column(Integer, primary_key=True, index=True)
    name=Column(String,unique=True,index=True)
    modelyear_id=Column(Integer, ForeignKey("modelyear.id"))


class StreamModel(Base):
    __tablename__="streams"
    id= Column(Integer, primary_key=True, index=True)
    name=Column(String,unique=True,index=True)
    model_year=Column(Integer,ForeignKey('modelyear.id'))
    coes=relationship("Coes", back_populates=True)
    
"""

class ProjectModel(Base):
    id=UUID
    name:str
    modelyear:ModelYear
    streams:  List[StreamModel] 
"""