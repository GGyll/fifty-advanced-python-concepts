"""
In this example, the Multiplier class has a __call__ method. When you create an instance of Multiplier with a certain factor, that instance becomes callable. 
So when you use parentheses with that object, it triggers the __call__ method and applies the factor to the given value. """
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Example usage:
doubler = Multiplier(2)
print(doubler(5))  # Output: 10

tripler = Multiplier(3)
print(tripler(5))  # Output: 15
