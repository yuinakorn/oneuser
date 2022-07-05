from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.users.users_model import UserBase, UserDisplayBase

from models.users.users_model import UserBase
from routes.users import users_controller

from utils.oauth2 import access_user_token

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserDisplayBase])
def get_all_user(db: Session = Depends(get_db)):
    return users_controller.read_users(db)


@router.get("/{username}", response_model=UserDisplayBase, dependencies=[Depends(access_user_token)])
def user_by_username(username: str, db: Session = Depends(get_db)):
    return users_controller.read_user_by_username(db, username)

# @router.post("/")
# def register_user(request: UserBase, db: Session = Depends(get_db)):
#     return users_controller.create(db, request)


# @router.put("/{id}", dependencies=[Depends(access_user_token)])
# def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
#     return users_controller.update(db, id, request)

#
# @router.delete("/{id}", dependencies=[Depends(access_user_token)])
# def delete_user(id: int, db: Session = Depends(get_db)):
#     return users_controller.delete(db, id)
