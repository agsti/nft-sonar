from etl.download_pictures import download_all_pictures
from etl.fetch_assets_of_collections import get_and_save_all_assets
from etl.fetch_collections import fetch_collections
from etl.hash_images import hash_images


def main():
    print("=" * 20, " FETCHING COLLECTIONS ", "=" * 20)
    fetch_collections(1)
    print("=" * 23, " FETCHING ASSETS ", "=" * 20)
    get_and_save_all_assets()
    print("=" * 20, " DOWNLOADING PICTURES ", "=" * 20)
    download_all_pictures()
    print("=" * 20, " HASHING IMAGES ", "=" * 20)
    hash_images()


if __name__ == "__main__":
    main()
