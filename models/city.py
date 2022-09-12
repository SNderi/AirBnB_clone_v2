#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class
    Attributes:
        state_id
        name
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullabe=False)
    state_id = Column(String(60), nullabe=False, ForeignKey=('states.id'))
    places = relationship('Place', backref='cities', cascade='all, delete')
