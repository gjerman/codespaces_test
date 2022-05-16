"""Main app"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Plate, PlateSet

engine = create_engine('sqlite:///plates.db')
Session = sessionmaker(bind=engine)
session = Session()


print("Hello World!")
print("Hello World again!")

a = Plate()
b = PlateSet()
