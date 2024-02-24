class Print_list:
    def print_list(Node):
        current_node = Node.head

        while current_node:
            print(current_node.data, end= " => ")
            current_node = current_node.next
        
        print("end")
