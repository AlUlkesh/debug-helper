import os
import sqlite3

db = os.path.abspath("wib.sqlite3")
print(db)
db_file = os.path.basename(db)
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute('''
    SELECT path, depth, path_display
    FROM path_recorder
    ''')
    for (path, depth, path_display) in cursor.fetchall():
        print(f"{path}\n{depth}\n{path_display}\n{os.path.realpath(path)}\n")
