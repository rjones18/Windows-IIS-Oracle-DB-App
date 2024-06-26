from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('oracle+oracledb://<rds endpoint>:1521/<DB NAME>')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)

Base.metadata.create_all(engine) 
