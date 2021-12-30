from imagededup.methods import PHash
from os import listdir
from os.path import isfile, join
from tqdm import tqdm


phasher = PHash()
pictures_path = "./data/pictures"
pictures = listdir(pictures_path)
for f in tqdm(pictures):
    file_path = join(pictures_path, f)
    if isfile(file_path):
        h = phasher.encode_image(file_path)
