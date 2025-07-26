from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True # Default for the incoming request body

class PostCreate(PostBase):
    pass # If you need additional fields for creation only

class Post(PostBase):
    id :int
    created_at:datetime 
    class config:
        orm_mode=True

class PostUpdate(BaseModel): # This schema is for the *input* to the update endpoint
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class config:
        orm_mode=True  

class UserLogin(BaseModel):
    email:EmailStr
    password:str        