from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(100000)]  # Consumes memory
    b = [i * 2 for i in a]         # More memory consumption
    return b

if __name__ == "__main__":
    my_function()
