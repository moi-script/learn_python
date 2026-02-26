
import sqlite3
import json
import sys
from pathlib import Path

# 1. Dynamically get the parent directory of this exact file
# __file__ is a special variable containing the path to the current script
parent_folder = Path(__file__).resolve().parent.parent

# 2. Add that parent folder to Python's system path
sys.path.append(str(parent_folder))

# 3. Now Python can "see" anything in that parent folder!

from cap_scrape import getInfoJson

# Let's assume these are the variables you extracted using Regex in the last step

infoList = json.loads(getInfoJson())

print(infoList)

file_name = infoList.get("file_name")
security_hash = infoList.get("security_hash")
absolute_path = infoList.get("absolute_path")



# 1. Connect to the database
# If 'scraped_files.db' doesn't exist in your folder, Python creates it instantly.
conn = sqlite3.connect('scraped_files.db')

# 2. Create a cursor
# The cursor is what actually executes your SQL commands
cursor = conn.cursor()

# 3. Create a table (if it doesn't exist yet)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS file_hashes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT NOT NULL,
        absolute_path TEXT NOT NULL UNIQUE,
        sha256_hash TEXT NOT NULL
    )
''')


# 4. Insert the data safely
# We use `?` as placeholders. NEVER use f-strings to insert variables into SQL
# because it leaves you open to SQL injection attacks.


try:
    cursor.execute('''
        INSERT INTO file_hashes (file_name, absolute_path, sha256_hash)
        VALUES (?, ?, ?)
    ''', (file_name, absolute_path, security_hash))
    
    # 5. Commit the transaction (This actually writes the data to the file)
    conn.commit()
    print("✅ Data saved to SQLite database successfully!")
    
except sqlite3.IntegrityError:
    # Because we set absolute_path as UNIQUE, SQLite automatically throws this
    # error if we try to scan and save the exact same file twice.
    print(f"⚠️ File '{file_name}' is already in the database.")

# 6. Always close the connection when your script is done
conn.close()