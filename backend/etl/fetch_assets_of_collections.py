import datetime
from tqdm import tqdm
from model.asset import save_asset
from model.collection import update_collection_latest_fetch, get_unfetched_collections
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
    return {
        'url': asset["image_url"],
        'marketplace_url': asset["permalink"],
        'name': asset["name"],
        'contract_name': asset["asset_contract"]["name"],
        'contract_address': asset["asset_contract"]["address"],
        'erc': asset["asset_contract"]["schema_name"],
        'collection_id': collection_id,
        'kind': None
    }


def get_and_save_all_assets():
    colections = get_unfetched_collections()

    for c in tqdm(colections):
        assets = get_all_assets(c.slug)
        for a in assets:
            # HERE
            save_asset(extract_asset_data(a, c.id))
            update_collection_latest_fetch(c.id, datetime.datetime.now())


if __name__ == '__main__':
    get_and_save_all_assets()
