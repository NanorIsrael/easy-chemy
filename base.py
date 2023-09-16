from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = engine = create_engine(
        'mysql+mysqlconnector://root:''@localhost/mysql',
    )
Session = sessionmaker(bind=engine)

Base = declarative_base()