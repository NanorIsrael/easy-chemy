#!/usr/bin/python3
"""Start link class to table in database 
"""
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR

Base = declarative_base()
class State(Base):
	"""Defines the state class"""
	__tablename__ = "states"
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column('name', String(128))

	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return f'{self.id} {self.name}'
