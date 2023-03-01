import os
import sqlite3

db = os.path.abspath("wib.sqlite3")
print(db)
db_file = os.path.basename(db)
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute('''
    SELECT file, name, ranking
    FROM ranking
    ''')
    for (file, name, ranking) in cursor.fetchall():
        print(f"{file}\n{name}\n{ranking}\n")
