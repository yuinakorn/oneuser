from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from models.database import get_db
from models.users.users_model import DbUser

from utils.md5 import Hash
from utils.oauth2 import create_access_token

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    elif not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    else:
        access_token = create_access_token(
            data={"sub": user.username, "hcode": user.officename})  # subject whom refer to

    return {
        "access_token": access_token,
        "token_type": "Bearer",
        "user_id": user.id,
        "username": user.username,
        "cid": user.cid,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "officename": user.officename,
        "status": user.status
    }
