import databases
import ormar
import sqlalchemy

from util.custom_types import LeagueEnum

DATABASE_URL = "postgresql://postgres:change_m3_too#@localhost/bogeyians"


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


class League(ormar.Model):
    class Meta(BaseMeta):
        tablename = "leagues"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200)
    type: str = ormar.String(max_length=50,choices=list(LeagueEnum))
    country_name: str = ormar.String(max_length=50)
    country_code: str = ormar.String(max_length=3)


class Team(ormar.ModelMeta):
    class Meta(BaseMeta):
        tablename = "teams"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=200)
    country_code: str = ormar.String(max_length=2)
    country_name = ormar.String(max_length=200)
    founded: int = ormar.Integer()
    national: bool = ormar.Boolean()


class Venue(ormar.ModelMeta):
    class Meta(BaseMeta):
        tablename = "venues"
    # venue info
    venue_id: int = ormar.Integer(),
    team_id: int = ormar.Integer()
    venue_name: str = ormar.String(max_length=200)
    venue_adress: str = ormar.String(max_length=200)
    venue_city: str = ormar.String(max_length=200)
    venue_capacity: int = ormar.Integer()
