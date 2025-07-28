# from operator import imod
from json import load
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
# secret_key
# algorithm
# expression time
from fastapi.security.oauth2 import OAuth2PasswordBearer
from .database import get_db
from app import models

load_dotenv(dotenv_path=".env")
import os
SECRET_KEY=os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM=os.getenv("ALGORITHM")
# from sentry_sdk import HttpTransport
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
from .schemas import TokenData, Token



def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("user_id")
        if id is None:
            raise credentials_exception
        id_str: str = str(id)
        token_data = TokenData(id=id_str)
    except JWTError:
        raise credentials_exception

    return token_data


def get_curr_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not valid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token, credentials_exception)
    try:
        user_id_int = int(token.id)
    except ValueError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.id == user_id_int).first()
    return user
