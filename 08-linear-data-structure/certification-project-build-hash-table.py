class HashTable:
    def __init__(self):
        # Initialize the collection attribute to an empty dictionary
        self.collection = {}

    def hash(self, key_string):
        # Return the sum of the Unicode (ASCII) values of each character
        return sum(ord(char) for char in key_string)

    def add(self, key, value):
        # Compute the hash value of the key
        hash_value = self.hash(key)
        
        # If the hash value doesn't exist in the collection, initialize a nested dict
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
            
        # Store the key-value pair inside the nested dictionary
        self.collection[hash_value][key] = value

    def remove(self, key):
        # Compute the hash value of the key
        hash_value = self.hash(key)
        
        # Confirm if the hash index exists and the key is inside that nested dictionary
        if hash_value in self.collection and key in self.collection[hash_value]:
            # Delete only the specific key-value pair
            del self.collection[hash_value][key]
            
            # Optional cleanup: If the nested dictionary is now empty, remove the hash index entirely
            if not self.collection[hash_value]:
                del self.collection[hash_value]

    def lookup(self, key):
        # Compute the hash value of the key
        hash_value = self.hash(key)
        
        # Check if the hash index exists and if the exact key exists inside it
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        
        # Return None if the key does not exist
        return None