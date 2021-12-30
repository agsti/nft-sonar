import datetime
from tqdm import tqdm
from base.db import Asset, DB
from base.opensea import Opensea


def get_all_assets(collection):
    all_assets = []
    api = Opensea()
    for p in range(200):
        new_assets = api.get_assets(collection, p)
        if len(new_assets) == 0:
            break
        all_assets += new_assets
        if len(new_assets) < 0:
            break
    return all_assets


def extract_asset_data(asset, collection_id):
    return Asset(
            contract_name=asset["asset_contract"]["name"],
            erc=asset["asset_contract"]["schema_name"],
            contract_address=asset["asset_contract"]["address"],
            url=asset["image_url"],
            name=asset["name"],
            marketplace_url=asset["permalink"],
            collection_id=collection_id
            )


def get_and_save_all_assets():
    db_connection = DB()
    cur = db_connection.get_unfetched_collections()

    for (rowid, slug) in tqdm(cur):
        assets = get_all_assets(slug)
        for a in assets:
            db_connection.save_asset(extract_asset_data(a, rowid))
        db_connection.update_collection_latest_fetch(rowid, datetime.datetime.now())
        db_connection.commit()

    cur.close()


if __name__ == '__main__':
    get_and_save_all_assets()
