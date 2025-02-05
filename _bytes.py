# Write binary data to a file
with open("example.bin", "wb") as file:
    file.write(b"Binary data")

# Read binary data from a file
with open("example.bin", "rb") as file:
    data = file.read()
    print(data)  # Output: b'Binary data'
