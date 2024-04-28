#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
