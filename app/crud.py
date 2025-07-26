from passlib.context import CryptContext
from pydantic import EmailStr
from sqlalchemy.orm import Session

from models import Post, User
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def create_post(db:Session,title:str,content:str,published:bool):
    c_post=Post(title=title,content=content,published=published)
    db.add(c_post)
    db.commit()
    db.refresh(c_post)
    return c_post

def create_user(db:Session,email:EmailStr,password:str):
    hashed_password=pwd_context.hash(password)
    user_create=User(email=email,password=hashed_password)
    db.add(user_create)
    db.commit()
    db.refresh(user_create)
    return user_create

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)