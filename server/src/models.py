from sqlalchemy import Column, Integer, String
from .database import base


class User(base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
