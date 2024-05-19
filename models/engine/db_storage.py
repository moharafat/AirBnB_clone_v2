#!/usr/bin/python3
"""This module defines the database class"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from os import getenv
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

all_classes = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review}


class DBStorage:
    """This is the storage engine for the SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """This method will initiate a new instance"""
        SQL_USER = getenv('HBNB_MYSQL_USER')
        SQL_PASSWD = getenv('HBNB_MYSQL_PWD')
        SQL_HOST = getenv('HBNB_MYSQL_HOST')
        SQL_DB = getenv('HBNB_MYSQL_DB')
        ENV_STATE = getenv('HBNB_ENV')
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    SQL_USER,
                    SQL_PASSWD,
                    SQL_HOST,
                    SQL_DB),
                pool_pre_ping=True)
        if ENV_STATE == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This method will return all objects of a specific class"""
        returned_dict = {}
        if cls is None:
            for one_cls in all_classes.values():
                returned_ob = self.__session.query(one_cls).all()
                for one_ob in returned_ob:
                    o_key = one_ob.__class__.__name__ + '.' + one_ob.id
                    returned_dict[o_key] = one_ob
        else:
            returned_ob = self.__session.query(cls).all()
            for one_ob in returned_ob:
                o_key = one_ob.__class__.__name__ + '.' + one_ob.id
                returned_dict[o_key] = one_ob
        return returned_dict

    def new(self, obj):
        """This method will add the instance to the datatbase"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """This method will save the changes made in th session"""
        self.__session.commit()

    def delete(self, obj=None):
        """This method will delete an instance from the database"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                    type(obj).id == obj.id).delete()

    def reload(self):
        """This method will create a;; the tables in the database"""
        Base.metadata.create_all(self.__engine)
        created_session = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(created_session)()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.remove()
