class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # An iterator must return itself.

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Signal the end of iteration.
        value = self.current
        self.current += 1
        return value

# Using the iterator
iterator = MyIterator(1, 5)
for num in iterator:
    print(num)  # Output: 1, 2, 3, 4
