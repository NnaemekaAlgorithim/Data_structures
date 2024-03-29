from list_operations_00 import Linked_list_00

# Define the main function or block of code
def main():
    # Create a linked list
    llist = Linked_list_00()

    # Append some elements to the linked list
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.insert_at_beginning(5)
    llist.insert_at_position(3, 0)

    # Print the linked list
    llist.print_list()

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
