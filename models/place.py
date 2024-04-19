#!/usr/bin/python3
""" this is the place model """

from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from models import how_to_store
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship

if how_to_store == 'db':
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60),
                ForeignKey('places.id'),
                primary_key=True,
                nullable=False),
            Column('amenity_id', String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False)
            )

class Place(BaseModel, Base):
    """ This is the place the user will chooose """
    __tablename__ = 'places'
    if how_to_store == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                'Review',
                backref='place',
                cascade='all, delete, delete-orphan')
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            ''' This propert will return a list of review ints'''
            from models import storage
            total_revs = storage.all(Review)
            ls_revs = []
            for one_rev in total_revs.values():
                if one_rev.place_id == self.id:
                    ls_revs.append(one_rev)
            return ls_revs

        @property
        def amenities(self):
            ''' This property will return a list of amenity inst'''
            from models import storage
            total_amen = storage.all(Amenity)
            ls_revs = []
            for one_amen in total_amen.values():
                if one_amen.id in self.amenity_ids:
                    ls_revs.append(one_amen)
            return ls_revs

        @amenities.setter
        def amenities(self, obj):
            ''' This propert will add the ameneity id '''
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
