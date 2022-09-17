from sqlalchemy.orm import Session

from . import models, schemas

def get_airbnb(db: Session, airbnb_id: str):
    return db.query(models.Airbnb).filter(models.Airbnb.id == airbnb_id).first()

def get_airbnbs(db: Session, skip: int = 0, limit = 100):
    return db.query(models.Airbnb).offset(skip).limit(limit).all()

def create_airbnb(db: Session, airbnb: schemas.AirbnbCreate):
    pass
