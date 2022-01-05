import unittest
import random
from base.pinecone import Pinecone


class TestPinecone(unittest.TestCase):

    def test_insert(self):
        p = Pinecone()

        e = [float(random.randrange(-20, 10)) for i in range(1024)]
        p.insert(123, e)

        results = p.query(e)
        self.assertEqual(results[0]['asset_id'], 123)

if __name__ == '__main__':
    unittest.main()
