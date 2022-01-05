from datetime import datetime
import unittest
from model.collection import save_collection, find_collection


class TestCollectionModel(unittest.TestCase):

    def testSave(self):
        collection = {
            'id': 3,
            'slug': 'a slug',
            'name': 'some collection name',
            'telegram_url': 'telegar.cm',
            'twitter_username': 'agsti',
            'created_at': datetime.now(),
        }
        save_collection(collection)
        saved_col = find_collection(3)
        self.assertEqual(collection, saved_col)
        self.assertEqual(saved_col.slug, "a slug")


if __name__ == '__main__':
    unittest.main()
