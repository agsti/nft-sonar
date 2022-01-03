from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, has_collection, drop_collection, list_collections


class Milvus:
    DEFAULT_COLLECTION_NAME = "nft_search"

    def __init__(self, collection_name=DEFAULT_COLLECTION_NAME):
        self._Milvus_collection = connections.connect(host='localhost', port='19530')
        self.collection_name = collection_name
        if (has_collection(self.collection_name)):
            print("Loading existing collection")
            self.__collection = Collection(name=self.collection_name)
        else:
            print("Creating collection...", self.collection_name)
            self.__collection = self.create_schema()

    def create_schema(self):
        dim = 1024
        default_fields = [
            FieldSchema(name="asset_id", dtype=DataType.INT64, is_primary=True),
            FieldSchema(name="float_vector", dtype=DataType.FLOAT_VECTOR, dim=dim)
        ]
        default_schema = CollectionSchema(fields=default_fields, description="Collection")

        collection = Collection(name=self.collection_name, schema=default_schema)
        default_index = {"index_type": "IVF_FLAT", "params": {"nlist": 128}, "metric_type": "L2"}
        collection.create_index(field_name="float_vector", index_params=default_index)
        return collection

    def drop_collection(self):
        drop_collection(self.collection_name)

    def list_collections(self):
        list_collections()

    def search(self, search_vector, topK=5):
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        return self.__collection.search(
            [search_vector], "float_vector", search_params, topK, output_fields=["asset_id"]
        )[0]

    def insert(self, asset_id, embedding):
        self.__collection.insert([[asset_id], [embedding]])
