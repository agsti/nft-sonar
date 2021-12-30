import unittest
import random
from milvus import Milvus

class TestMilvus(unittest.TestCase):

    def test_insert(self):
        client = Milvus(collection_name="test_collection")
        e = [float(random.randrange(-20, 10)) for i in range(128)]
        client.insert(123, e)
        search_result = client.search(e, 1) 
        self.assertEqual(search_result.ids, [123])

if __name__ == '__main__':
    unittest.main()
