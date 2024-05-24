import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase

if sqlalchemy.__version__.startswith('2'):
    class Base(DeclarativeBase):
        pass
else:
    Base = declarative_base()
