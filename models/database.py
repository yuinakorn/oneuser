from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

from decouple import config

DATABASE_URL = config('DATABASE_URL')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')

engine = create_engine(DATABASE_URL % quote(MYSQL_PASSWORD))
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()
