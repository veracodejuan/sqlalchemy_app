from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database
engine = create_engine('sqlite:///example.db', echo=True)

# Create a base class for models
Base = declarative_base()

# Define a simple User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

# Query the user
user = session.query(User).filter_by(name='Alice').first()
print(f'User found: {user.name}, Age: {user.age}')
