# Doubly Linked Lists
# Now that you know more about singly linked lists, let's talk about doubly linked lists.

# In a doubly linked list, each node stores two references: a reference to the next node and a reference to the previous node in the sequence.

# This means that doubly linked lists can be traversed in both directions.

# Singly Linked Lists
# A singly linked list is a type of linked list in which each node is connected to the next node in the sequence.

# Each node is connected to the next one by storing a reference to it.

# This single reference per node allows you to traverse the linked list in one direction, from start to end.

# The search can only move forward, not backwards.

# Inserting Nodes
# One of the great things about linked lists is that they do not have a fixed size. They can be expanded or shrunk as needed by simply updating the connections between the nodes.

# You can insert a node at the start, middle, and end of a linked list.

# Linked lists don't necessarily need to store the nodes in a specific order. The order will be determined by the connections between the nodes.

# However, if you do need to keep the nodes in a specific order for your particular use case, you can do so by implementing that logic in your code and the criteria you implement will determine if the node is inserted at the start, middle, or end.

# To insert a node at the start of the linked list, you just need to create a connection between the new node and the node that used to be the head node and make the new node the head node instead.

# Questions

#1 What is a linked list?

# A data structure that stores elements in a contiguous block of memory.

# A data structure where nodes are connected using references.///correct

# A data structure that is always sorted.

# A data structure that has a fixed size.

#2 What is the difference between a singly linked list and a doubly linked list?

# Singly linked lists have a head and tail node, while doubly linked lists do not.

# Singly linked lists can only be traversed in one direction, while doubly linked lists can be traversed in both directions.///correct

# Singly linked lists are more efficient to insert elements at the end, while doubly linked lists are more efficient to insert elements at the beginning.

# Singly linked lists require more memory than doubly linked lists.

#3 What is the time complexity of inserting a node at the beginning of a singly linked list?

# O(1)///correct

# O(n)

# O(n^2)

# O(log n)
