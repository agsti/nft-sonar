from fastapi import FastAPI

from base.hasher import Hasher
from config.db import conn
from model.asset import asset


def get_app():
    app = FastAPI(title="GINO FastAPI Demo")
    return app


app = get_app()


@app.get("/")
async def helloworld():
    return conn.execute(asset.select()).fetchall()
