import pinecone
import settings


class Pinecone:

    def __init__(self):
        api_key = settings.pinecone_api_key
        pinecone.init(api_key=api_key, enironment='us-west1-gcp')
        index_name = settings.pinecone_index_name
        self.index = pinecone.Index(index_name=index_name)

    def insert(self, asset_id, embedding):
        ids = [str(asset_id)]
        vectors = [
            embedding,
        ]
        self.index.upsert(vectors=zip(ids, vectors))

    def stats(self):
        return self.index.describe_index_stats()

    def query(self, embedding):
        r = self.index.query(queries=[embedding], top_k=5)

        def extract_data(m):
            return {
                    'asset_id': int(m['id']),
                    'score': m['score']
                    }
        m = map(extract_data, r['results'][0]['matches'])
        return list(m)
