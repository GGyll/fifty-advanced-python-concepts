from array import array

numbers = array('i', [1, 2, 3, 4, 5])
# i for integers

numbers.append(6)    # Add element to end
numbers.extend([7, 8])  # Add multiple elements
numbers.insert(0, 0)    # Insert at specific position

print(numbers)
