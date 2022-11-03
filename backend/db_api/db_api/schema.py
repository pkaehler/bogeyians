from enum import Enum

from pydantic import BaseModel


class LeagueType(str, Enum):
    league = 'league'
    cup = 'cup'


class Team(BaseModel):
    name: str
    country: float
    founded: int
    national: bool

    class Config:
        orm_mode = True


class League(BaseModel):
    name: str
    type: LeagueType

    class Config:
        orm_mode = True


class Country(BaseModel):
    name: str
    code: str


class Season(BaseModel):
    year: int
