from sqlalchemy import MetaData,Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

# Base = declarative_base()
from base import Base, Session, engine


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128))
    # cities = relationship('City', back_populates='state')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.id}: {self.name}'

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128))
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship('State', backref="cities")

    def __init__(self, name, state_id, state):
        self.name = name
        self.state_id = state_id
        self.state = state

    # def __repr__(self):
    #     return {self.id: self.name}

if __name__ == "__main__":
    # engine = create_engine(
    #     'mysql+mysqlconnector://root:''@localhost/mysql',
    #     echo=True
    # )
    Base.metadata.create_all(engine)

    # Session = sessionmaker(bind=engine)
    session = Session()

    # Create sample data (replace this with your actual data)
    # california = State('California')
    # arizona = State('Arizona')
    # texas = State('Texas')
    # new_york = State('New York')
    # nevada = State('Nevada')


    # cities_data = [
    #     City('San Francisco', california.id, california),
    #     City('San Jose', california.id, california),
    #     City('Los Angeles', california.id, california),
    #     City('Fremont', california.id, california),
    #     City('Livermore', california.id, california),
    #     City('Page', arizona.id, arizona),
    #     City('Phoenix', arizona.id, arizona),
    #     City('Dallas', texas.id, texas),
    #     City('Houston', texas.id, texas),
    #     City('Austin', texas.id, texas),
    #     City('New York', new_york.id, new_york),
    #     City('Las Vegas', nevada.id, new_york),
    #     City('Reno', nevada.id, nevada),
    #     City('Henderson', nevada.id, nevada),
    #     City('Carson City', nevada.id, nevada),
    # ]

    # metadata = MetaData()
    # table_name = 'cities'
    # cities = Table(table_name, metadata, autoload=True, autoload_with=engine)
    # table_name = 'states'
    # states = Table(table_name, metadata, autoload=True, autoload_with=engine)
    
    # cities.drop()
    # states.drop()

    # session.add_all([california, arizona, texas, new_york, nevada] + cities_data)
    # session.commit()

    # states = session.query(State).join(City).order_by(State.id, City.id).all()
    states = session.query(State).order_by(State.id).all()
    print('\n')
    print(states)
    print('\n')
    results_obj = {}
    for state_instance in states:
        del state_instance.__dict__['_sa_instance_state']
       
        results_obj.update({state_instance.__class__.__name__ + '.' + str(state_instance.id): state_instance})
    
    print(results_obj)
    #     for city in state.cities:
    #         print(f'    {city.id}: {city.name}')
    