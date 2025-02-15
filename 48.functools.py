from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper








# from functools import lru_cache

# @lru_cache(maxsize=3)  # Cache up to 3 results
# def expensive_computation(x):
#     print(f"Computing {x}")
#     return x * x

# print(expensive_computation(2))  # Output: Computing 2, then 4
# print(expensive_computation(2))  # Output: 4 (from cache)






from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)  # Multiplies all numbers
print(result)  # Output: 24
