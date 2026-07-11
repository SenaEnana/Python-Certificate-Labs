class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key_string):
        return sum(ord(char) for char in key_string)

    def add(self, key, value):
        hash_value = self.hash(key)

        if hash_value not in self.collection:
            self.collection[hash_value] = {}

        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)

        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]

            if not self.collection[hash_value]:
                del self.collection[hash_value]

    def lookup(self, key):
        hash_value = self.hash(key)

        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        return None