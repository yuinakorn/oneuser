from typing import Optional

from pydantic import BaseModel, SecretStr
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from models.database import Base


class DbUser(Base):
    __tablename__ = "sys_member"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    cid = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    officename = Column(String)
    status = Column(String)


# not use
# class DbAdmin(Base):
#     __tablename__ = "sys_admin"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True)
#     password = Column(String)
#     fullname = Column(String)
#     level = Column(Integer)
#     active = Column(Integer)
#     dlevel = Column(Integer)
#     ccard = Column(String)


# class User(BaseModel):
#     class Config:
#         orm_mode = True
#
#     id: int
#     password: str
#     cid: str
#     firstname: str
#     lastname: str
#     officename: str
#     status: str
#     username: str
#
#
# class Admin(BaseModel):
#     id: int
#     password: str
#     fullname: str
#     level: int
#     active: Optional[int] = None
#     dlevel: Optional[int] = None
#     ccard: Optional[int] = None
#     username: Optional[int] = None
#
#     item: User


#     Create or Show one row
class UserBase(BaseModel):
    username: str
    password: SecretStr


class UserDisplayBase(BaseModel):
    id: int
    username: str
    cid: str
    # firstname: str
    # lastname: Optional[str] = None
    officename: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True
