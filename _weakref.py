import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

# Avoid circular references using weak references
a = Node("A")
b = Node("B")
a.next = weakref.ref(b)
b.next = weakref.ref(a)

# Access weak references
print(a.next().name)  # Output: "B"
print(b.next().name)  # Output: "A"
