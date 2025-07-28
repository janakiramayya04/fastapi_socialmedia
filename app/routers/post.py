from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from .. import crud  # Go up to 'app' then import 'crud'
from .. import models  # Go up to 'app' then import 'models'
from .. import schemas  # Go up to 'app' then import 'schemas'
from ..database import engine, get_db  # Go up to 'app' then into 'database' module
from .. import oauth2  # Go up to 'app' then import 'oauth2'
from sqlalchemy.orm import Session

router = APIRouter(prefix="/posts", tags=["Posts"])


# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_curr_user),
    limit: int = 10,
    skip: int = 0,
    search: str = "",
):
    # posts = (
    #     db.query(models.Post)
    #     .filter(models.Post.title.contains(search))
    #     .limit(limit)
    #     .offset(skip)
    #     .all()
    # )
    result = (
        db.query(models.Post, func.count(models.Votes.post_id).label("votes"))
        .join(models.Votes, models.Votes.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    return result


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_curr_user),
):
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = (
        db.query(models.Post, func.count(models.Votes.post_id).label("votes"))
        .join(models.Votes, models.Votes.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.id == id)
        .first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"requested {id} is not found"
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
    return post


@router.post("/", response_model=schemas.Post)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_curr_user),
):
    c_p = crud.create_post(
        db=db,
        title=post.title,
        content=post.content,
        published=post.published,
        owner_id=current_user.id,
    )
    return c_p


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_curr_user),
):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the id {id} that your looking to delete is not there",
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="can't delete others post"
        )
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(
    id: int,
    post: schemas.PostUpdate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_curr_user),
):
    update_query = db.query(models.Post).filter(models.Post.id == id)
    existing_post = update_query.first()
    if existing_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"the id : {id} doesnot exist"
        )
    if existing_post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="can't delete others post"
        )
    update_query.update(post.model_dump(exclude_unset=True), synchronize_session=False)
    db.commit()
    db.refresh(existing_post)

    return existing_post
