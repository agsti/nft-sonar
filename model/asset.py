from sqlalchemy import Table, Column
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.schema import ForeignKey

from datetime import datetime
from config.db import meta, conn
from .collection import collection
from schemas.asset import Asset as AssetSchema

asset = Table("assets", meta, Column("id", Integer, primary_key=True),
              Column("url", String(512)), Column("marketplace_url",
                                                 String(512)),
              Column("name", String(512)), Column("contract_name",
                                                  String(512)),
              Column("contract_address", String(512)),
              Column("erc", String(64)), Column("filename", String(512)),
              Column("hashed_at", DateTime),
              Column("collection_id", ForeignKey(collection.c.id)),
              Column("kind", String(64)))


def find_asset(asset_ids):
    return conn.execute(asset.select()).first()


def get_assets_to_download():
    return conn.execute(
        asset.select().where(asset.c.hashed_at == None)).fetchall()


def get_assets_to_hash():
    return conn.execute(
        asset.select().where(asset.c.hashed_at == None)).fetchall()


def set_asset_hashed_at(asset_id: int, hashed_at: datetime):
    return conn.execute(asset.update().values(hashed_at=hashed_at).where(
        asset.c.id == asset_id))


def set_asset_file(asset_id: int, filename: str, kind: str):
    return conn.execute(asset.update().values(
        filename=filename, kind=kind).where(asset.c.id == asset_id))


def save_asset(asset_data: AssetSchema):
    return conn.execute(asset.insert().values(asset_data))
