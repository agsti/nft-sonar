
from os.path import isfile
from base.db import DB
from base.milvus import Milvus
from base.hasher import Hasher


def hash_images():
    db_con = DB()
    milvus = Milvus()
    hasher = Hasher()
    asset_urls = db_con.get_asset_files()
    for (asset_id, filename) in asset_urls:
        if isfile(filename):
            h = hasher.encode(filename)
            milvus.insert(asset_id, h)
            db_con.update_asset_hash(asset_id, h)
            db_con.commit()
            print(f"Done wih {asset_id}")


if __name__ == "__main__":
    hash_images()
