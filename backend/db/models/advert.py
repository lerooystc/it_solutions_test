from db import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Advert(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    viewcount = Column(Integer)
    position = Column(Integer)