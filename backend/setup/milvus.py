from base.milvus import Milvus
from base.db import DB

if __name__ == "__main__":
    m = Milvus()
    m.drop_collection()
    m.create_schema()


