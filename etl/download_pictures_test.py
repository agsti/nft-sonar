import unittest
from etl.download_pictures import download_picture


class TestDownloadPictures(unittest.TestCase):

    def test_download_all_pictures(self):
        url = "https://lh3.googleusercontent.com/ePIG19KQEquWjjeOqH_n84ccdAyVW1QEEoWVc8nbksbeyorZeRpcATucThBFTaQsPZf1GnAG7VQjovrPisbgJvlMP9e0VWLDXf_PTu8"
        download_picture(url)

if __name__ == '__main__':
    unittest.main()
