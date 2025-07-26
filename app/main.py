from typing import List
from fastapi import FastAPI,Response,status,HTTPException,Depends
# from app.routers import auth
import crud
import models
from sqlalchemy.orm import Session
from database import engine,get_db

app=FastAPI()
models.Base.metadata.create_all(bind=engine)
import routers.user
# import schemas
import routers.post
import routers.auth
app.include_router(routers.post.router)
app.include_router(routers.user.router)
app.include_router(routers.auth.router)