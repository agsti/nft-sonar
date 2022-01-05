from model.asset import set_asset_file, get_assets_to_download

from concurrent.futures import ThreadPoolExecutor, as_completed
from base.utils import asset_kind, random_uuid
import requests

import os
import shutil


def download_picture(pic_url):
    filename = random_uuid()
    tmp_fname = f"data/pictures/{filename}"
    print(f"downloading {pic_url} to {tmp_fname}")
    resp = requests.get(pic_url)
    with open(tmp_fname, 'wb') as my_file:
        # Read by 4KB chunks
        for byte_chunk in resp.iter_content(chunk_size=1024 * 10):
            if byte_chunk:
                my_file.write(byte_chunk)
                my_file.flush()
                os.fsync(my_file)
    resp.close()

    ext = asset_kind(tmp_fname)
    fname = f"data/pictures/{filename}.{ext}"

    shutil.move(tmp_fname, fname)
    return (fname, ext)


def download_and_store_asset(asset_id, asset_url):
    (filename, extension) = download_picture(asset_url)
    print(f"Downloaded {filename} {extension}")

    set_asset_file(asset_id, filename, extension)


def download_all_pictures():
    executor = ThreadPoolExecutor(max_workers=10)
    assets = get_assets_to_download()
    futures = []
    for a in assets:
        future = executor.submit(download_and_store_asset, a.id, a.url)
        futures += [future]

    for future in as_completed(futures):
        print("Downloaded %s into %s" % future.result())


if __name__ == '__main__':
    download_all_pictures()
