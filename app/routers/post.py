from typing import List
from fastapi import FastAPI,Response,status,HTTPException,Depends ,APIRouter
import crud, models,schemas
from sqlalchemy.orm import Session
from database import engine,get_db
router=APIRouter(
     prefix="/posts",
     tags=['Posts']
)
models.Base.metadata.create_all(bind=engine)
@router.get("/", response_model=List[schemas.Post])
def get_posts(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts


@router.get("/{id}")
def get_post(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"requested {id} is not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
    return {"post_details":post}

@router.post("/",response_model=schemas.Post)
def create_post(post:schemas.PostCreate,db:Session=Depends(get_db)):
    c_p=crud.create_post(db=db,
        title=post.title,
        content=post.content,
        published=post.published)
    return c_p

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"the id {id} that your looking to delete is not there")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}")
def update_post(id :int,post:schemas.PostUpdate, db:Session=Depends(get_db)):
        update_query = db.query(models.Post).filter(models.Post.id == id)
        existing_post = update_query.first()
        if existing_post is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the id : {id} doesnot exist")
        update_query.update(post.model_dump(), synchronize_session=False)
        db.commit()
        # db.refresh(post)

        return {"data": update_query.first() }
