from ..base.db import DB

import imghdr
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

import os
import shutil


def download_picture(pic_url, id):
    tmp_fname = "/tmp/nft_search/%s" % id
    print("downloading %s" % pic_url)
    resp = requests.get(pic_url)
    with open(tmp_fname, 'wb') as my_file:
        # Read by 4KB chunks
        for byte_chunk in resp.iter_content(chunk_size=1024*10):
            if byte_chunk:
                my_file.write(byte_chunk)
                my_file.flush()
                os.fsync(my_file)
    resp.close()

    ext = imghdr.what(tmp_fname)

    print("%s is %s" % (tmp_fname, ext))
    fname = "data/pictures/%d.%s" % (id, ext)
    shutil.move(tmp_fname, fname)

    connection = DB()
    connection.set_asset_filename(id, fname)
    connection.commit()
    return (pic_url, fname)


def download_all_pictures():
    executor = ThreadPoolExecutor(max_workers=10)
    db_connection = DB()
    urls = db_connection.get_picture_urls()
    futures = []
    for (id, url) in urls:
        future = executor.submit(download_picture, url, id)
        futures += [future]

    for future in as_completed(futures):
        print("Downloaded %s into %s" % future.result())


if __name__ == '__main__':
    download_all_pictures()
