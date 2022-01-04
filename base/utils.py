import imghdr
import uuid


def asset_kind(filename):
    return imghdr.what(filename)

def random_uuid():
    return str(uuid.uuid4())
