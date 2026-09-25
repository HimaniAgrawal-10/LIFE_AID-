import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS donors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    blood_group TEXT,
    city TEXT,
    phone TEXT
)
""")

conn.commit()
conn.close()

print("Donors Table Created")