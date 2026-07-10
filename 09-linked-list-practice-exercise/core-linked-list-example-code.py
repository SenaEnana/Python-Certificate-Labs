class Node:
    """A single node in a linked list."""
    def __init__(self, data):
        self.data = data  
        self.next = None  


class LinkedList:
    """The linked list wrapper class."""
    def __init__(self):
        self.head = None  

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return      
        current = self.head
        while current.next:
            current = current.next
        
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
        # TODO: 
        
        return False 
    def delete(self, target):
        current = self.head
        prev = None

        if not current:
            return
        if current.data == target:
            self.head = current.next
            return

        # TODO: 

        if not current:
            return
            
        # TODO:

# Testing implementation 
ll = ExerciseLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print("Original List:")
ll.display() # Output should be: 10 -> 20 -> 30 -> None

# Test Search
print("\nSearching for 20:", ll.search(20)) # Should be True
print("Searching for 99:", ll.search(99)) # Should be False

# Test Delete
ll.delete(20)
print("\nList after deleting 20:")
ll.display() # Output should be: 10 -> 30 -> None