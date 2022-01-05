import unittest
from model.asset import save_asset


class TestAssetModel(unittest.TestCase):

    def testSave(self):
        asset = {
            'url': 'www.someurl.com',
            'marketplace_url': 'www.someurl.com',
            'name': 'some asset name',
            'contract_name': 'some contract name',
            'contract_address': '0x666',
            'erc': 'ERC1234',
            'collection_id': 3,
            'kind': 'jpeg'
        }
        save_asset(asset)


if __name__ == '__main__':
    unittest.main()
