import sys
data = bytearray(b"A" * 10**6)
mv = memoryview(data)


# Slicing without copying
mv_slice = mv[100:100000]  # View of the data, no copy made

# Slicing with bytes
bytes_slice = data[100:100000]  # Creates a new copy

# Compare sizes
print(f"Size of memoryview slice: {sys.getsizeof(mv_slice):,} bytes")
print(f"Size of bytes slice: {sys.getsizeof(bytes_slice):,} bytes")

