def my_generator():
    yield 1
    yield 2
    yield 3


# This defines a generator function but doesn't execute it
gen = my_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Raises StopIteration














def generator_with_send():
    value = yield "Start"
    yield f"Received: {value}"

gen = generator_with_send()
print(next(gen))       # Output: Start
print(gen.send("Data"))  # Output: Received: Data
print(gen.throw(ValueError))