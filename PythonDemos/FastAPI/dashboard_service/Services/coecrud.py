from sqlalchemy.orm import Session

from Models import coemodel
from Schemas import coeschemas


def create_modelyear(db: Session, modelyear: coeschemas.ModelYearCreate):
    db_modelyear = coemodel.ModelYearModel(name=modelyear.name)
    print(db_modelyear)
    db.add(db_modelyear)
    db.commit()
    db.refresh(db_modelyear)
    return db_modelyear