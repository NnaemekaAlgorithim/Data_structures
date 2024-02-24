from node import Node
from print_list import Print_list

class Linked_list_00(Print_list):
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


    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_position(self, position, data):
        if position < 0:
            print("invalid position")
            return
        
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        prev = None
        count = 0

        while current and count < position:
            prev = current
            current = current.next
            count += 1

        if count < position:
            print("position out of bounds")
            return
        
        prev.next = new_node
        new_node.next = current
