from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

my_posts=[{"title":"title of my post 1"
           ,"content":"cotent of post 1","id":1},
           {"title":"hyderabad"
           ,"content":"best biryani in hyderabad","id":2}]

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p

# @app.get("/posts/latest")
# def lastest_post():
#     post=my_posts [len(my_posts)-1]
#     return {"detail" :post}

@app.get("/posts/{id}")
def get_post(id:int):
    post=find_post(id)
    return {"post_details":post}

@app.post("/posts")
def create_post(payload:Post):
    post_dict=payload.model_dump()
    post_dict['id']=randrange(0,100)
    my_posts.append(post_dict)
    return {"data":post_dict}