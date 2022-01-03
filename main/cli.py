from base.milvus import Milvus
from base.hasher import Hasher
from base.db import DB
import sys


def main():
    hasher = Hasher()
    db = DB()
    filename = sys.argv[1]
    print(f"Going to use {filename}")

    emmbeddings = hasher.encode(filename)
    print("Encoded image")
    milvus = Milvus()
    print("Loaded milvus")
    results = milvus.search(emmbeddings)
    print("Got milvus results")
    db.get_assets(results.ids)
    breakpoint()


if __name__ == "__main__":
    main()
