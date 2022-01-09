from os.path import isfile
from model.asset import get_assets_to_hash, set_asset_hashed_at
from base.pinecone import Pinecone
from base.hasher import Hasher
from datetime import datetime


def hash_images():
    pinecone = Pinecone()
    hasher = Hasher()
    assets = get_assets_to_hash()
    breakpoint()
    print(f"Got {len(assets)} assets to hash")
    for asset in assets:
        if isfile(asset.filename):
            h = hasher.encode_filename(asset.filename)
            pinecone.insert(asset.id, h)
            set_asset_hashed_at(asset.id, datetime.now())
            print(f"Done wih {asset.id}")


if __name__ == "__main__":
    hash_images()
