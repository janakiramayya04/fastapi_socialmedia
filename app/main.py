from fastapi import FastAPI,Response,status,HTTPException
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

class UpdatePost(BaseModel):
    title:Optional[str]
    content:Optional[str]
    published:Optional[bool]=True
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
def get_post(id:int,response:Response):
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"requested {id} is not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
    return {"post_details":post}

@app.post("/posts")
def create_post(payload:Post):
    post_dict=payload.model_dump()
    post_dict['id']=randrange(0,100)
    my_posts.append(post_dict)
    return {"data":post_dict}

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/posts/{id}")
def update_post(id :int ,post:Post):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the id : {id} doesnot exist")
    post_dict=post.model_dump()
    post_dict['id']=id
    my_posts[index]=post_dict
    return {"data":post_dict}
