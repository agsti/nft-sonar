from base.db import Collection, DB
from base.opensea import Opensea


def new_collection(api_data):
    c = Collection(
            created_at=api_data["created_date"],
            slug=api_data["slug"],
            name=api_data["name"],
            twitter_username=api_data["twitter_username"],
            telegram_url=api_data["telegram_url"]
    )
    return c


def get_and_store_all_collections():
    db_connection = DB()
    api = Opensea()
    for p in range(200):
        print("fetching page #%d" % (p))
        collection_page = api.get_collections(p)
        for c in collection_page:
            collection_data = new_collection(c)
            db_connection.save_collection(collection_data)
        db_connection.commit()


if __name__ == '__main__':
    get_and_store_all_collections()
