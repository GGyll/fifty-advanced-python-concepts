import sys

class MyClass:
    my_var = "foo"

my_list = [MyClass()] * 10000000
print(len(my_list))
print(sys.getsizeof(my_list))