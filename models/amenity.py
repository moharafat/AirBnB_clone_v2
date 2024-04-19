#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import how_to_store

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if how_to_store == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
