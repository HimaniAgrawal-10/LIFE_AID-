import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS hospitals(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_name TEXT,
    city TEXT,
    address TEXT,
    phone TEXT
)
""")

conn.commit()
conn.close()

print("Hospitals Table Created")