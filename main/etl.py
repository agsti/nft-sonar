from etl.download_pictures import download_all_pictures
from etl.fetch_assets_of_collections import get_and_save_all_assets
from etl.fetch_collections import fetch_collections


def main():
    fetch_collections(1)
    get_and_save_all_assets()
    download_all_pictures()


if __name__ == "__main__":
    main()
