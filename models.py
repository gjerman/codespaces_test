
from lib2to3.pytree import Base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Plate(Base):
    __tablename__ = 'plates'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_active = Column(Boolean)
    plate_sets = relationship("PlateSet", back_populates="plate")
