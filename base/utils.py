import imghdr


def asset_kind(filename):
    return imghdr.what(filename)
