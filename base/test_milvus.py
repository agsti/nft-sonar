import unittest
import random
from base.milvus import Milvus


class TestMilvus(unittest.TestCase):

    @unittest.skip("Hangs")
    def test_insert(self):
        print("Hello2")
        client = Milvus(collection_name="test_collection")
        client.drop_collection()
        client.create_schema()
        print("Hello2")
        e = [float(random.randrange(-20, 10)) for i in range(1024)]
        print("Hello2")
        client.insert(123, e)
        print("Hello2")
        search_result = client.search(e, 1) 
        print("Hello2")
        self.assertEqual(search_result.ids, [123])
        print("Hello2")

if __name__ == '__main__':
    unittest.main()
