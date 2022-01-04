from base.pinecone import Pinecone
from base.hasher import Hasher
from base.db import DB
import sys


def main():
    hasher = Hasher()
    db = DB()
    filename = sys.argv[1]
    print(f"Going to use {filename}")

    e = hasher.encode(filename)
    print("Encoded image")
    pinecone = Pinecone()
    print("Loaded pinecone")
    results = pinecone.query(e)
    print("Got pine results")
    db.get_assets(results[0]['id'])
    breakpoint()


if __name__ == "__main__":
    main()
