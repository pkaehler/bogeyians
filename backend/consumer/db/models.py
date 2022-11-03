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

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.drop_all(engine)
metadata.create_all(engine)
