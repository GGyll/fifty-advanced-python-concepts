# with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
#     data = file1.read()
#     file2.write(data)

























from contextlib import ExitStack

files = ['file1.txt', 'file2.txt']

with ExitStack() as stack:
    file_objects = [stack.enter_context(open(file, 'w')) for file in files]
    for file_obj in file_objects:
        file_obj.write("Hello, World!")
