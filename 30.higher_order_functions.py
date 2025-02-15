def validate(data, *validators):
    for validator in validators:
        if not validator(data):
            return False
    return True

# Validators
is_non_empty = lambda x: bool(x)
is_alpha = lambda x: x.isalpha()

# Validate input
input_data = "Python"
is_valid = validate(input_data, is_non_empty, is_alpha)
print(is_valid)  # Output: True
