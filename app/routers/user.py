from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import crud  # Go up to 'app' then import 'crud'
from .. import database  # Go up to 'app' then import 'database'
from .. import schemas
from .. import models
# from database import engine, get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])
crud.models.Base.metadata.create_all(bind=database.engine)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut
)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    creation = crud.create_user(db, user.email, user.password)
    return creation


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"requested {id} is not found"
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
    return user
