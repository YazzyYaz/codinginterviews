class HashTable(object):
    def __init__(self):
        self.size = 11
        self.slot = [None] * self.size
        self.data = [None] * self.data

    def hash_function(self, key):
        return key % self.size

    def rehash(self, key):
        return (key + 1) % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)
        if self.slot[hash_value] is None:
            self.slot[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slot[hash_value] == key:
                self.data[hash_value] = data
            else:
                new_hash = self.rehash(key)
                while self.slot[new_hash] is not None and self.slot[new_hash] != key:
                    new_hash = self.rehash(new_hash)
                if self.slot[new_hash] is None:
                    self.slot[new_hash] = key
                    self.data[new_hash] = data
                else:
                    self.data[new_hash] = data

    def get(self, key):
        startslot = self.hash_function(key)
        found = False
        done = False
        data = None
        position = startslot
        while self.slot[position] != None and not found and not done:
            if self.slot[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    done = True
        return data
