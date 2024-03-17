#!/usr/bin/python3
"""Module for State class with a relationship to City class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City

class State(Base):
    """State class to represent states in the US
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

