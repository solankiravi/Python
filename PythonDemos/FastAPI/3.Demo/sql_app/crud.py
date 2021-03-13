from os import name
from sqlalchemy.orm import Session
from . import models, schemas

def get_models(db:Session, model_year_id:int):
    return db.query(models.ModelYear).filter(models.ModelYear.id==model_year_id).first()

def create_modelYear(db:Session, item: schemas.ModelYearCreate):
    
    db_model_year= models.ModelYear(id = item.id, name= item.name)
    db.add(db_model_year)
    db.commit()
    db.refresh(db_model_year)
    return item

def create_coe(db:Session, item: schemas.CoeCreate):
    
    db_coe= models.Coes(id = item.id, name= item.name, modelyear_id= item.modelyear_id )
    db.add(db_coe)
    db.commit()
    db.refresh(db_coe)
    return item