# def call_counter(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         print(f"Call {wrapper.calls} to {func.__name__}")
#         return func(*args, **kwargs)
#     wrapper.calls = 0  # Add a counter attribute to the wrapper
#     return wrapper

# @call_counter
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")  # Call 1 to greet
# greet("Bob")    # Call 2 to greet













# # So you can use decorators for caching
# def cache(func):
#     stored_results = {}
#     def wrapper(*args):
#         if args not in stored_results:
#             stored_results[args] = func(*args)
#         return stored_results[args]
#     return wrapper

# @cache
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)

# print(fib(10))  # Output: 55






# def authenticate(func):
#     def wrapper(*args, **kwargs):
#         print("Authenticating...")
#         return func(*args, **kwargs)
#     return wrapper

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Logging call to {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @authenticate
# @log
# def access_data():
#     print("Accessing sensitive data")

# access_data()
# Output:
# Authenticating...
# Logging call to access_data
# Accessing sensitive data



# def add_method(cls):
#     def new_method(self):
#         return "I am a new method!"
#     cls.new_method = new_method
#     return cls

# @add_method
# class MyClass:
#     pass

# obj = MyClass()
# print(obj.new_method())  # Output: I am a new method!




import time

def timer(unit="seconds"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            if unit == "milliseconds":
                duration *= 1000
            print(f"{func.__name__} took {duration:.2f} {unit}")
            return result
        return wrapper
    return decorator

@timer(unit="milliseconds")
def slow_function():
    time.sleep(1)

slow_function()  # Output: slow_function took 1000.00 milliseconds
