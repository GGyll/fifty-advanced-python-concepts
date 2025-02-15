from dataclasses import dataclass, field

# @dataclass
# class Person:
#     name: str
#     age: int

#     def __post_init__(self):
#         if self.age < 0:
#             raise ValueError("Age cannot be negative")

# person = Person("Alice", 30)  # Works fine
# person = Person("Bob", -5)  # Raises ValueError




# @dataclass
# class Person:
#     name: str
#     age: int

# @dataclass
# class Employee(Person):
#     employee_id: int

# emp = Employee(name="Alice", age=30, employee_id=1234)
# print(emp)  # Output: Employee(name='Alice', age=30, employee_id=1234)



# Without field (problematic):
@dataclass
class TaskWithoutField:
    description: str
    completed: bool = False  # This becomes a parameter with default value

# This allows unwanted initialization:
task1 = TaskWithoutField("Do laundry", completed=True)  # Can override default

# With field (better design):
@dataclass
class TaskWithField:
    description: str
    completed: bool = field(init=False)  # Not in __init__
    
    def __post_init__(self):
        self.completed = False

# Now this is impossible:
# task2 = TaskWithField("Do laundry", completed=True)  # Error!
# Can only create like this:
task2 = TaskWithField("Do laundry", completed=True)  # completed is always False initially