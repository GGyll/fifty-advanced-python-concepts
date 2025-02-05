import pickle

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")

    def write(self, data):
        self.file.write(data)

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the non-pickleable file object
        del state["file"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Restore the file object
        self.file = open(self.filename, "w")

# Create an instance
handler = FileHandler("example.txt")
handler.write("Hello, World!")

# Serialize and deserialize the instance
with open("handler.pkl", "wb") as file:
    pickle.dump(handler, file)

with open("handler.pkl", "rb") as file:
    loaded_handler = pickle.load(file)

loaded_handler.write("Another line!")
