from fastapi import HTTPException, APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import models  # Go up to 'app' then import 'models'
from ..database import get_db  # Go up to 'app' then into 'database' module
from ..schemas import UserLogin, Token  # Go up to 'app' then into 'schemas' module
from ..crud import verify  # Go up to 'app' then into 'crud' module
from ..oauth2 import create_token  # Go up to 'app' then into 'oauth2' module


router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid Credentials"
        )
    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials"
        )
    access_token = create_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
