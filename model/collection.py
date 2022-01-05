from sqlalchemy import Table, Column
from sqlalchemy.types import String, Integer, DateTime
from config.db import meta, conn
from schemas.collection import Collection as ColletionSchema

collection = Table(
    "collections",
    meta,
    Column("id", Integer, primary_key=True),
    Column("slug", String(256), unique=True),
    Column("name", String(256), nullable=True),
    Column("telegram_url", String(256), nullable=True),
    Column("twitter_username", String(256), nullable=True),
    Column("created_at", DateTime),
    Column("latest_fetch", DateTime),
)


def find_collection(id):
    return conn.execute(
        collection.select().where(collection.c.id == id)).first()


def save_collection(c_data: ColletionSchema):
    return conn.execute(collection.insert().values([c_data]))


def update_collection_latest_fetch(collection_id, latest_fetch):
    c = conn.execute(collection.update().values(
        latest_fetch=latest_fetch).where(collection.c.id == collection_id))
    return c
    # Something more


def get_unfetched_collections():
    return conn.execute(collection.select().where(
        collection.c.latest_fetch == None)).fetchall()
