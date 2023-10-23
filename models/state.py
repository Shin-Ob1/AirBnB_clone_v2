#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """Getter attribute for cities"""
            city_list = []
            from models import storage
            for city, obj in storage.__objects.items():
                if "City" in city and (obj.state_id == State.id):
                    city_list.append(obj)

            return city_list
