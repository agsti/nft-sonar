from etl.download_pictures import download_all_pictures
from etl.fetch_assets_of_collections import get_and_save_all_assets
from etl.fetch_collections import fetch_collections
from etl.hash_images import hash_images


def main():
    fetch_collections(0)
    get_and_save_all_assets()
    download_all_pictures()
    hash_images()


if __name__ == "__main__":
    main()
