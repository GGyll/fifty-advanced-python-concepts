from collections import defaultdict

# Create a defaultdict with a default value of 0
default_dict = defaultdict(int)

default_dict['a'] += 1
default_dict['b'] += 5

print(default_dict)  