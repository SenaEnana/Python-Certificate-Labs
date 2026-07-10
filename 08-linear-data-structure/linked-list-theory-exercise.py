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

# Inserting a node at the beginning of the linked list has a constant time complexity O(1) because it only requires updating the reference to the head node and the connection between the new head node and the next node in the sequence.

# In this example, we are inserting node E at the start of the linked list. This will work correctly. But if we wanted to keep the linked list sorted in alphabetical order, node E would have to be inserted at the end of the linked list instead.

# To insert a node at the end of the linked list, first you need to reach the end and then add a connection to the new node to make it the new tail node.

# This operation has linear time complexity, O(n), where n is the number of nodes stored in the linked list, because first you need to reach the end of the linked list to make the insertion and this would require going from one node to the next and so on until the end is reached.

# Removing Nodes
# Just as you can insert nodes, you can also remove them from the start, middle, and end of the linked list.

# To remove a node from the start, you need to update the reference to the head node, which should be the next node in the sequence.

# This operation has a constant time complexity O(1), because it only requires updating the linked list's reference to the head node.

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
