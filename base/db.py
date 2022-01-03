import sqlite3
from dataclasses import dataclass


@dataclass
class Collection:
    created_at: str
    slug: str
    name: str
    telegram_url: str
    twitter_username: str


@dataclass
class Asset:
    url: str
    marketplace_url: str
    name: str
    contract_name: str
    contract_address: str
    erc: str
    collection_id: str


class DB:
    def __init__(self):
        db_name = open("data/LATEST_DB.txt").read()
        self.connection = sqlite3.connect(db_name)

    def save_collection(self, c):
        print("Saving collection %s" % (c.slug))
        self.connection.execute("""
                        insert into collections(
                            created_at,
                            slug,
                            name,
                            telegram_url,
                            twitter_username)
                        values (?, ?, ?, ?, ?)""", (
                            c.created_at,
                            c.slug,
                            c.name,
                            c.telegram_url,
                            c.twitter_username
                        )
                        )

    def save_asset(self, a):
        print("Saving %s" % (a.name))
        self.connection.execute("""insert into assets(
                                    asset_url,
                                    marketplace_url,
                                    name,
                                    contract_name,
                                    contract_address,
                                    erc,
                                    collection_id)
                                    values (?, ?, ?, ?, ?, ?, ?)""", (
                                        a.url,
                                        a.marketplace_url,
                                        a.name,
                                        a.contract_name,
                                        a.contract_address,
                                        a.erc,
                                        a.collection_id))

    def update_collection_latest_fetch(self, collection_id, latest_fetch):
        self.connection.execute("""UPDATE collections
                set latest_fetch = ?
                where rowid=?""", (latest_fetch, collection_id))

    def get_unfetched_collections(self):
        cur = self.connection.cursor()
        cur.execute("select rowid, slug from collections where latest_fetch is null")
        return cur

    def set_asset_filename(self, asset_id, filename):
        self.connection.execute("""UPDATE assets
                                    set filename = ?
                                    where rowid = ?""", (filename, asset_id))

    def get_asset_files(self):
        return self.connection.execute("""select
                                            rowid,
                                            filename
                                        from assets
                                        where
                                            hash is NULL""")

    def update_asset_hash(self, asset_id, hash):
        return self.connection.execute("""select
                                            rowid,
                                            filename
                                        from assets
                                        where
                                            hash is NULL""")

    def get_picture_urls(self):
        return self.connection.execute("""select
                                          rowid,
                                          asset_url
                                        from assets
                                        where
                                            filename is null""")

    def commit(self):
        self.connection.commit()
