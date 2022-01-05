import unittest
from model.asset import find_asset
from etl.download_pictures import download_picture, download_and_store_asset


class TestDownloadPictures(unittest.TestCase):

    def test_download_pictures(self):
        url = "https://lh3.googleusercontent.com/ePIG19KQEquWjjeOqH_n84ccdAyVW1QEEoWVc8nbksbeyorZeRpcATucThBFTaQsPZf1GnAG7VQjovrPisbgJvlMP9e0VWLDXf_PTu8"
        download_picture(url)

    def test_download_and_store_asset(self):
        url = "https://lh3.googleusercontent.com/ePIG19KQEquWjjeOqH_n84ccdAyVW1QEEoWVc8nbksbeyorZeRpcATucThBFTaQsPZf1GnAG7VQjovrPisbgJvlMP9e0VWLDXf_PTu8"
        asset = find_asset(1)
        download_and_store_asset(asset.id, url)


if __name__ == '__main__':
    unittest.main()
