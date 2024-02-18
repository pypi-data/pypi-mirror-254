

class Environment:
    def __init__(self):
        self.store = {}

    def get(self, name):
        obj = self.store.get(name)
        return obj

    def set(self, name, val):
        self.store[name] = val
        return val
