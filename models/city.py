#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class
    Attributes:
        state_id
        name
    """
    if models.storage_type == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        def __init__(self, state_id = "", name = ""):
            """ if storage type is FileStorage instantiate the values """
            self.state_id = state_id
            self.name = name
            super().__init__()
