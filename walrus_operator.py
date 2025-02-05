my_dict = {...}

def my_func(my_dict):
    my_var = my_dict.get("my_var", None)
    if my_var:
        return my_var

# With walrus operator
my_dict = {...}
def my_func(my_dict):
    if my_var := my_dict.get("my_var", None):
        return my_var