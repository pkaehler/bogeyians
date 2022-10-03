from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()


class Team(Base):
    __tablename__ = 'teams'
    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    founded = Column(Integer)
    national = Column(Boolean)


class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(Integer) # Enum: "league" "cup"


class Countries(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String) #  Alpha2 code of the country


class Season(Base):
    __tablename = "seasons"
    year = Column(Integer, primary_key=True)