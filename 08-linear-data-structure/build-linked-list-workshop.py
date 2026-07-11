class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
            
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

my_list = LinkedList()
print(my_list.is_empty())