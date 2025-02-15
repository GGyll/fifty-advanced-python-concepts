from operator import attrgetter

# Define nested classes
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
        
class Company:
    def __init__(self, city, name):
        self.city = city
        self.name = name

class Person:
    def __init__(self, name, age, address, company):
        self.name = name
        self.age = age
        self.address = address
        self.company = company

# Sample data
people = [
    Person("Alice", 30, Address("New York", "NY"), Company("Company ABC", "Philadelphia")),
    Person("Bob", 25, Address("Chicago", "IL"), Company("Company 2", "Nashville")),
    Person("Charlie", 35, Address("Los Angeles", "CA"), Company("Company 3", "Miami"))
]

# Get sort_key from frontend
# sort_key = "address.city"
# sort_key = "company.name"
sort_key = "address.city"

# Sort based on the dynamic key
sorted_people = sorted(people, key=attrgetter(sort_key))

print([person.name for person in sorted_people])  # Example Output: ['Bob', 'Charlie', 'Alice']
