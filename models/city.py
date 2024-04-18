#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import how_to_store
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city for my sql table
    creates a new model city
    """
    __tablename__ = 'cities'
    if how_to_store == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
                'Place',
                backref='cities',
                cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
