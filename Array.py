my_array = [1, 2, 3, 4, 5]

# Accessing elements of the array
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

# Inserting an element at a specific index
my_array.insert(2, 10)
print(my_array)  # Output: [1, 2, 10, 3, 4, 5]

# Appending an element to the end of the array
my_array.append(6)
print(my_array)  # Output: [1, 2, 10, 3, 4, 5, 6]

# Removing an element from the array
my_array.remove(3)
print(my_array)  # Output: [1, 2, 10, 4, 5, 6]

# Updating the value of an element
my_array[1] = 20
print(my_array)  # Output: [1, 20, 10, 4, 5, 6]

# Searching for an element in the array
index = my_array.index(10)
print(index)  # Output: 2

# Finding the length of the array
length = len(my_array)
print(length)  # Output: 6
