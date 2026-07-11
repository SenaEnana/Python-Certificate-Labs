# Build a Hash Table

# In this lab, you will build a hash table from scratch. A hash table is a data structure that stores key-value pairs.
#  A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.

# For the purpose of this lab, the hashing function will be simple: 
# it will sum the Unicode values of each character in the key. The hash value will then be used as the actual key to store the associated value. The same hash value would also be used to retrieve and delete the value associated with the key.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define a class named HashTable with a collection attribute 
# initialized to an empty dictionary when a new instance of HashTable is created. 
# The collection dictionary should store key-value pairs based on the hashed value of the key.

# The HashTable class should have four instance methods: hash, add, remove, and lookup.

# The hash method should:

# Take a string as a parameter.
# Return a hashed value computed as the sum of the Unicode (ASCII) values of each character in the string. You can use the ord function for this computation.
# The add method should:

# Take two arguments representing a key-value pair, and compute the hash of the key.
# Use the computed hash value as a key to store a dictionary containing the key-value pair inside the collection dictionary.
# If multiple keys produce the same hash value, their key-value pairs should be stored in the existing nested dictionary under the same hash value.
# The remove method should:

# Take a key as its argument and compute its hash.
# Confirm if the key exists in the collection.
# Remove the corresponding key-value pair from the hash table.
# If the key does not exist in the collection, it should not raise an error or remove anything.
# The lookup method should:

# Take a key as its argument.
# Compute the hash of the key, and return the corresponding value stored inside the hash table.
# If the key does not exist in the collection, it should return None.
# Tests:
# Passed:1. You should define a HashTable class.
# Passed:2. When a new instance of the HashTable class is created, its collection attribute should be initialized to an empty dictionary.
# Passed:3. The HashTable class should have a hash method.
# Passed:4. The hash method should take a string as a parameter.
# Passed:5. The hash method should take a string as its argument and return the sum of the Unicode values of each character in the string.
# Passed:6. The HashTable class should have an add method.
# Passed:7. The add method should take a key and value as parameters.
# Passed:8. The HashTable class should have a remove method.
# Passed:9. The remove method should take a key as a parameter.
# Passed:10. When you try to remove a key that does not exist in the collection, it should not raise an error or remove anything.
# Passed:11. If multiple keys hash to the same index, the remove method should only delete the specific key-value pair and not the entire dictionary at that index.
# Passed:12. The HashTable class should have a lookup method.
# Passed:13. The lookup method should take a key as the parameter.
# Passed:14. HashTable().hash('golf') should return 424.
# Passed:15. HashTable().add('golf', 'sport') should add the key-value pair to the collection at key 424.
# Passed:16. HashTable().add('dear', 'friend') and HashTable().add('read', 'book') should add both the key-value pairs to the collection at index 412 as a nested dictionary.
# Passed:17. When a key exists in the hash table, the remove() method should remove the given key and its corresponding value from the collection.
# Passed:18. When the 'golf', 'sport' key-value pair exists in the hash table, HashTable().lookup('golf') should return sport.
# Passed:19. When the 'golf', 'sport' key-value pair does not exist in the collection, HashTable().lookup('golf') should return None.
# Passed:20. When the 'fcc' key exists in the collection, HashTable().lookup('cfc') should return None.
# Passed:21. When you add ('rose', 'flower') to the hash table, its collection attribute should look like this: { 441: { 'rose': 'flower' }}.
# Passed:22. When you add a key that hashes to the same value as an existing key, like fcc and cfc, the collection should look like this: { 300: { 'fcc': 'coding', 'cfc':  'chemical' }}.