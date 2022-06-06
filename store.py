class Store(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Store, cls).__new__(cls)
        return cls.instance

def store():
    return Store