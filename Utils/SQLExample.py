## Init SQLite
#
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (wird erstellt, falls sie nicht existiert)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Tabelle erstellen, falls sie noch nicht existiert
cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value INTEGER
)
""")

# Beispiel-Python-Liste
data = [
    {"name": "Alice", "value": 100},
    {"name": "Bob", "value": 200},
    {"name": "Charlie", "value": 300},
]

# Daten in die Tabelle einfügen
for entry in data:
    cursor.execute("INSERT INTO data (name, value) VALUES (?, ?)", (entry["name"], entry["value"]))

# Änderungen speichern
conn.commit()

# Daten abfragen und anzeigen
cursor.execute("SELECT * FROM data")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Verbindung schließen
conn.close()

## Timestamps
#
from datetime import datetime, timezone
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect("timestamps.db")
cursor = conn.cursor()

# Create table to store timestamps
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_time TEXT
)
""")

# Current UTC timestamp in ISO 8601 format
current_time = datetime.now(timezone.utc).isoformat()

# Insert a timestamped event
cursor.execute("INSERT INTO events (event_name, event_time) VALUES (?, ?)",
               ("Sample Event", current_time))

# Query and display stored timestamps
cursor.execute("SELECT * FROM events")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()