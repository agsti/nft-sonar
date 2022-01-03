from imagededup.methods import CNN


class Hasher:
    cnn = CNN()

    def encode(self, filename):
        i_hash = self.cnn.encode_image(filename)
        return i_hash.flatten().tolist()
