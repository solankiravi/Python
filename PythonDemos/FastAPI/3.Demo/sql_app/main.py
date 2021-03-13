
from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from . import crud, models,schemas

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/modelyears', response_model=schemas.ModelYearModel)
def create_modelyear(item: schemas.ModelYearCreate, db: Session = Depends(get_db)):
    return crud.create_modelYear(db=db,item=item)

@app.post('/coe', response_model=schemas.CoeModel)
def create_coe(item: schemas.CoeCreate, db: Session = Depends(get_db)):
    return crud.create_coe(db=db,item=item)

