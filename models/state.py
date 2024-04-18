#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import how_to_store


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if how_to_store == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
                'City',
                backref='state',
                cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """This is a property that returns a list
            of the cities objs the belongs to the state object"""
            from models import storage
            list_ofcts = []
            returned_cts = storage.all(City)
            for one_cty in returned_cts.values():
                if one_cty.state_id == self.id:
                    list_ofcts.append(one_cty)
            return list_ofcts
