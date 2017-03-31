
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('sqlite:///api_rest.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    username = Column(String)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User Id {}, {}>".format(self.id, self.username)


Base.metadata.create_all(engine)

'''

from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

'''
