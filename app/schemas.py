from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict, conint
from typing import Annotated, Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True  # Default for the incoming request body


class PostCreate(PostBase):
    pass  # If you need additional fields for creation only


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class Post(PostBase):
    id: int
    created_at: datetime
    owner: UserOut
    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post:Post
    votes:int
    model_config=ConfigDict(from_attributes=True)

class PostUpdate(BaseModel):  # This schema is for the *input* to the update endpoint
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, conint(ge=0, le=1)]
