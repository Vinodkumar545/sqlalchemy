
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'person'

	id = Column('id', Integer, primary_key=True)
	username = Column('username', String, unique=True)

# engine = create_engine('sqlite:///:memory', echo=True)
engine = create_engine('sqlite:///user.db', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

# create a new user
user = User()
user.id = 2
user.username = 'Doug'

session.add(user)
session.commit()

# once the user are created query

users = session.query(User).all()

for user in users:
	print("User with username '%s' and id '%s'."%(user.username, user.id))

session.close()
