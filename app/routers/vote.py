from fastapi import HTTPException, APIRouter, Depends, status, Response
from sqlalchemy import false
from .. import crud  # Go up to 'app' then import 'crud'
from .. import database  # Go up to 'app' then import 'database'
from .. import schemas
from .. import models
from .. import oauth2
from sqlalchemy.orm import Session

router = APIRouter(tags=["Votes"], prefix="/votes")


@router.post("/", status_code=status.HTTP_201_CREATED)
def votes(
    vote: schemas.Vote,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_curr_user),
):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detaiL=f"Post with id:{vote.post_id} does not exist",
        )

    vote_query = db.query(models.Votes).filter(
        models.Votes.post_id == vote.post_id,
        models.Votes.user_id == current_user.id,
    )
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail=f"user{current_user.id } has already found voted in past{vote.post_id}",
            )
        new_vote = models.Votes(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"message": "successfully added voted"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist"
            )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": " successfully deleted vote"}
