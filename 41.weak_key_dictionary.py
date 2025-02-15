from weakref import WeakKeyDictionary

class Widget:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Widget({self.name})"

# Create a WeakKeyDictionary for storing metadata
widget_metadata = WeakKeyDictionary()

# Create some widgets
widget1 = Widget("Button1")
widget2 = Widget("Button2")

# Attach metadata
widget_metadata[widget1] = {"color": "blue", "size": "small"}
widget_metadata[widget2] = {"color": "red", "size": "large"}

print(widget_metadata)  # Output: {Widget(Button1): {...}, Widget(Button2): {...}}

# Remove a strong reference
del widget1

# The metadata for widget1 is automatically cleaned up
print([key for key in widget_metadata.keys()])  # Output: {Widget(Button2): {...}}
