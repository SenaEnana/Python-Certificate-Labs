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