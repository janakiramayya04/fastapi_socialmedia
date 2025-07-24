# from xmlrpc.client import boolean
from sqlalchemy.orm import Session
# import schemas
from models import Post
def create_post(db:Session,title:str,content:str,published:bool):
    c_post=Post(title=title,content=content,published=published)
    db.add(c_post)
    db.commit()
    db.refresh(c_post)
    return c_post