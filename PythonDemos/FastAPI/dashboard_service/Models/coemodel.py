from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer, String
from Common.database import Base


class ModelYearModel(Base):
    __tablename__="model_year"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String,unique=True,index=True)
    is_active=Column(Boolean, default=True)


class CoeModel(Base):
    __tablename__="coes"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String,unique=True,index=True)
    is_active=Column(Boolean, default=True)

class Stream(Base):
    __tablename__="projects"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String,unique=True,index=True)
    is_active=Column(Boolean, default=True)
    # modelyear_id = Column(Integer, ForeignKey("model_year.id"))
    
    # coes = relationship("ModelYearModel", back_populates="name")

