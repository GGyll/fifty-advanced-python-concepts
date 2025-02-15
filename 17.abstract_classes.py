from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def concrete(self):
        return "Subscribe"

# Cannot instantiate an abstract class
# shape = Shape()  # Raises TypeError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an instance of the subclass
rect = Rectangle(4, 5)
print(rect.area())       # Output: 20
print(rect.perimeter())  # Output: 18
print(rect.concrete())
