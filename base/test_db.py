import unittest
from base.db import DB


class DBTest(unittest.TestCase):

    def testGetAssetsOne(self):
        db = DB()
        assets = db.get_assets(1)
        self.assertEqual(assets.rowcount, 1)

    def testGetAssetsMulti(self):
        db = DB()
        assets = db.get_assets([1,2])
        self.assertEqual(assets.rowcount, 2)


if __name__ == '__main__':
    unittest.main()
