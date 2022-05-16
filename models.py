"""Handling of database models"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Plate(Base):
    """Class for the Plate table"""
    __tablename__ = 'plates'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_active = Column(Boolean)
    plate_sets = relationship("PlateSet", back_populates="plate")

class PlateSet(Base):
    "Class for the PlateSet table"
    __tablename__ = 'plate_sets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_active = Column(Boolean)
    plate_id = Column(Integer, ForeignKey('plates.id'))
    plate = relationship("Plate", back_populates="plate_sets")
