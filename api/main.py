from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import sessionLocal1, engine

app = FastAPI()
# models.Base.metadata.create_all(bind=engine)


# Dependency
async def get_db():
    db = sessionLocal1()
    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()

@app.get("/airbnbs/", response_model=list[schemas.Airbnb])
def read_airbnbs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    airbnbs = crud.get_airbnbs(db, skip=skip, limit=limit)
    return airbnbs