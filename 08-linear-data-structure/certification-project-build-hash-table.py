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

 