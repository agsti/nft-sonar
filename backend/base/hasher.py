from imagededup.methods import CNN
from PIL import Image
from numpy import asarray


class Hasher:
    cnn = CNN()

    def encode_filename(self, filename):
        i_hash = self.cnn.encode_image(filename)
        return i_hash.flatten().tolist()

    def encode_file(self, file):
        file_image = Image.open(file).convert('RGB')
        d = asarray(file_image)
        i_hash = self.cnn.encode_image(image_array=d)
        return i_hash.flatten().tolist()
