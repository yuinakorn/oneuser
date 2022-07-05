from sqlalchemy.orm import Session  # to use database

from fastapi import HTTPException, status  # to response Error
from fastapi.responses import JSONResponse  # json format

from models.users.users_model import UserBase, DbUser  # import User Model
from utils.md5 import Hash  # hash function


def read_users(db: Session):
    return db.query(DbUser).all()


def read_user_by_username(db: Session, username: str):
    """
    select * from user where id = ?
    """
    return db.query(DbUser).filter(DbUser.username == username).first()


# def update(db: Session, id: int, request: UserBase):
#     user = db.query(DbUser).filter(DbUser.id == id)
#     if user.first() is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} not found"
#         )
#     else:
#         user.update(
#             {
#                 DbUser.username: request.username,
#                 DbUser.password: Hash.bcrypt(request.password),
#             }
#         )
#         db.commit()
#         return JSONResponse(
#             content={"detail": f"user id {id} updated successful"},
#             status_code=status.HTTP_200_OK,
#         )
