import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import League as LeagueSchema

from models import League as LeagueModel

import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get("/")
async def root():
    return {"message": "moin foobar"}


@app.get('/leagues/', response_model=LeagueModel)
async def leagues(league: LeagueSchema):
    leagues = db.session.query(LeagueModel).all()
    return leagues


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)