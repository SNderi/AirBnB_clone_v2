#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import String, DateTime, Column, ForeignKey
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class
    Attributes:
        name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')

    else:
        @property
        def cities(self):
            """ Getter attribute in case of file storage. 
            Return:
                The list of City instances with state_id equals to self.id
            """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
