class Node:
    """A single node in a linked list."""
    def __init__(self, data):
        self.data = data  # Stores the value
        self.next = None  # Points to the next node (initially None)


class LinkedList:
    """The linked list wrapper class."""
    def __init__(self):
        self.head = None  # The first node in the list

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return      
        # Otherwise, traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        
        # Link the last node to the new node
        current.next = new_node

    def display(self):
        """Print the entire linked list so we can see it."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

class ExerciseLinkedList(LinkedList):
    def search(self, target):
        current = self.head
        # TODO: Loop through the list to find the target
        # Hint: 'while current:' will let you look at every node
        
        return False # Placeholder
    def delete(self, target):
        current = self.head
        prev = None