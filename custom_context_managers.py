import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    """Context manager for managing a database connection."""
    conn = sqlite3.connect(db_name)
    try:
        print("Database connection opened")
        yield conn
    finally:
        conn.close()
        print("Database connection closed")

# Usage
with database_connection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "Alice"))
    conn.commit()
    print("Data inserted successfully")
