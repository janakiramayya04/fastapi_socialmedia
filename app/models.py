# from kivy.uix.treeview import TreeView
from database import Base
from sqlalchemy import Integer,String,Boolean,TIMESTAMP, null, text
from sqlalchemy import Column
from typing import Optional
class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,nullable=False,index=True)
    title=Column(String(200),nullable=False)
    content=Column(String(300), nullable=False)
    published=Column(Boolean, server_default='1',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False ,index=True)
    email=Column(String(100),nullable=False,unique=True)
    password=Column(String(100),nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
