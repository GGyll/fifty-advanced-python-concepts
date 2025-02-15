from dataclasses import dataclass

# @dataclass
# class Point:
#     x: int
#     y: int

# point = Point(1, 2)
# print(point)        # Output: Point(x=1, y=2)
# print(point.x)      # Output: 1
# print(point.y)      # Output: 2














# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"
    
#     def __eq__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented
#         return (self.x, self.y) == (other.x, other.y)
    
#     def __hash__(self):
#         return hash((self.x, self.y))

# point = Point(1, 2)
# print(point)        # Output: Point(x=1, y=2)
# print(point.x)      # Output: 1
# print(point.y)      # Output: 2

# # The dataclass also generates these behaviors:
# point1 = Point(1, 2)
# point2 = Point(1, 2)
# print(point1 == point2)  # True - equality comparison works
# print(hash(point1))      # Hash value based on x and y

# @dataclass
# class Person:
#     name: str
#     age: int = 30
#     city: str = "Unknown"

# person = Person(name="Alice")
# print(person)  # Output: Person(name='Alice', age=30, city='Unknown')





@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(1, 2)
point.x = 3  # Raises FrozenInstanceError
