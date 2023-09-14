from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base



Base = declarative_base();

class Thing(Base):
	__tablename__ = "things"

	tid = Column("tid", Integer, primary_key=True)
	description = Column("description", String)
	owner = Column(Integer, ForeignKey('people.ssn'))

	def __init__(self, tid, description, owner):
		self.tid = tid
		self.description = description
		self.owner = owner

	def __repr__(self):
		return f"{self.tid} {self.description} and owned by {self.owner}"

class Person(Base):
	__tablename__ = "people"
	ssn = Column("ssn", Integer, primary_key=True)
	firstname = Column("firstname", String)
	lastname = Column("lastname", String)
	gender = Column("gender", CHAR)
	age = Column("age", Integer)

	def __init__(self, ssn, firstname, lastname, age, gender):
		self.ssn = ssn
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.gender = gender
	
	def __str__(self):
		return f"{self.ssn} {self.firstname} {self.lastname} {self.age}"

	def __repr__(self):
		return f"{self.ssn} {self.firstname} {self.lastname} {self.age}, {self.gender}"



person = Person(1234, "Maurice", "Nicole", 24, 'M')
thing = Thing(4321, "Maurice Nicole thing", 1234)
# print(person)

engine = create_engine('postgresql://postgres:alchemy@localhost:5433/my_db', pool_pre_ping=True)
Base.metadata.create_all(bind=engine)

Sesssion = sessionmaker(bind=engine)
session = Sesssion()

# session.add(person)
# session.commit()
# session.add(thing)
# session.commit()

getAll = session.query(Person).all()
print(getAll)
getOne = session.query(Person).filter(Person.firstname == 'Nicole')
print(getAll)


getAllThings = session.query(Thing).all()
print(getAllThings)
# getOne = session.query(Person).filter(Person.firstname == 'Nicole')
# print(getAll)