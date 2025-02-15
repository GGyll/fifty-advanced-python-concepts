import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an instance of the class
person = Person("Alice", 30)

# Serialize (pickle) the instance to a file
with open("person.pkl", "wb") as file:
    pickle.dump(person, file)

# Deserialize (unpickle) the instance from the file
with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)

print(loaded_person.greet())  # Output: Hello, my name is Alice and I am 30 years old.
