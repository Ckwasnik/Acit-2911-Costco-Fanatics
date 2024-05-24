import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug(f"SQLAlchemy version: {sqlalchemy.__version__}")

if sqlalchemy.__version__.startswith('2'):
    from sqlalchemy.orm import DeclarativeBase

    class Base(DeclarativeBase):
        pass
else:
    Base = declarative_base()
