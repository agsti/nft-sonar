from datetime import datetime
from model.collection import save_collection
from base.opensea import Opensea
from sqlalchemy.exc import DBAPIError


def new_collection(api_data):
    created_at = datetime.fromisoformat(api_data["created_date"])
    c = {
        'created_at': created_at,
        'slug': api_data["slug"],
        'name': api_data["name"],
        'twitter_username': api_data["twitter_username"],
        'telegram_url': api_data["telegram_url"]
    }
    return c


def fetch_collections(n_pages=200):
    api = Opensea()
    for p in range(n_pages):
        print("fetching page #%d" % (p))
        collection_page = api.get_collections(p)
        for c in collection_page:
            collection_data = new_collection(c)
            try:
                save_collection(collection_data)
            except DBAPIError as e:
                print("Error while saving collection", e.statement)


if __name__ == '__main__':
    fetch_collections()
