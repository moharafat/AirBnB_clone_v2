#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, **kwargs):
        """init function for base_model
        """
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = self._parse_value(
            'created_at', kwargs.get('created_at')
            )
        self.updated_at = self._parse_value(
            'updated_at', kwargs.get('updated_at')
            )
        for key, value in kwargs.items():
            if key not in ['id', 'created_at', 'updated_at']:
                if key != '__class__':
                    setattr(self, key, value)

    def _parse_value(self, method, value):
        """parse the values of the kwargs dictionary of init
        """
        if not value:
            value = datetime.now()
        elif isinstance(value, str):
            value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        elif not isinstance(value, datetime):
            raise ValueError(f"{method} must be a datetime object")
        return value

    
    

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        """ Delethe the instance"""
        models.storage.delete(self)