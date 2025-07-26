from fastapi import HTTPException,APIRouter,Depends,status,Response
from sqlalchemy.orm import Session

import models
from database import get_db
from schemas import UserLogin
from crud import verify
router=APIRouter(
    tags=['Authentication']
)
@router.post('/login')
def login(user_credentials:UserLogin,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid Credentials")
    if not verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"requested {id} is not found")
    
    return {"token":"example token"}