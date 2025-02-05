class Dog:
    pass
# python secretly does this 
# () is a tuple of base classes (e.g., if the class inherits from something).
# {} is the dictionary containing the class's methods and attributes.
Dog = type("Dog", (), {})













# from django.db import models

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

# class ModelMeta(type):
#     def __new__(cls, name, bases, dct):
#         # Extract fields (attributes that are instances of Field)
#         fields = {key: value for key, value in dct.items() if isinstance(value, Field)}
        
#         # Add the _meta attribute to store metadata about the model
#         dct["_meta"] = {"fields": fields}
        
#         # Add a custom manager
#         dct["objects"] = DatabaseManager()
        
#         return super().__new__(cls, name, bases, dct)