class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function demonstrating polymorphism
def print_area(shape):
    print(f"The area is {shape.area()}")

# Usage
rectangle = Rectangle(5, 10)
circle = Circle(7)

print_area(rectangle)  # Output: The area is 50
print_area(circle)     # Output: The area is 153.86
