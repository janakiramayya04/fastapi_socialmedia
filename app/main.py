from fastapi import FastAPI
from app import models
from fastapi.middleware.cors import CORSMiddleware

from . import database

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)
from .routers import user, post, auth, vote

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
