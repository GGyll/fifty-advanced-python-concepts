# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



























# numbers = [1, 2, 3, 4, 5]
# labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
# print(labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd']


























def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temperatures_c = [0, 20, 30, 40]
temperatures_f = [celsius_to_fahrenheit(t) for t in temperatures_c]
print(temperatures_f)  # Output: [32.0, 68.0, 86.0, 104.0]
