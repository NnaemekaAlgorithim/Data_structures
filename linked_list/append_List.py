from node import Node
from print_list import Print_list

class append(Print_list):
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
