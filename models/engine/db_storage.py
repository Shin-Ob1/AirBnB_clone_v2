#!/usr/bin/python3

"""Database storage engine created for the AirBnb project"""
from models.base_model import Base
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """The storage class for database storage abstraction"""

    __engine = None
    __session = None

    def __init__(self):
        """This will initialize the database storage"""

        # create engine for database and ping the database connection
        # which will check if the database connection is still alive or dead
        # and carry out connection maintenance
        engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)
        self.__engine = engine
        # Delete tables if this is a testing environment instance
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """Query on the current database session"""

        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'User': User,
                    'State': State, 'City': City,
        }
        dictionary_obj = {}
        if cls is not None:
            result = self.__session.query(classes[cls]).all()
            for data in result:
                # create key for the object
                key = cls + '.' + data.id
                dictionary_obj[key] = data
            return dictionary_obj
        else:
            for key, value in classes.items():
                result = self.__session.query('State').all()
                for data in result:
                    # create new key for the objects
                    newkey = cls + '.' + data.id
                    dictionary_obj[newkey] = data
            return dictionary_obj

    def new(self, obj):
        """Adds the object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commits all session of the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()