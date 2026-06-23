import sqlite3
import os
def init_db():
    conn =  sqlite3.connect("../database/growthAI.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT,
            location TEXT,
            results TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
def save_search(domain, location, results):
    conn =  sqlite3.connect("../database/growthAI.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_searches (domain, location, results) VALUES (?, ?, ?)",
        (domain, location, str(results))
    )
    conn.commit()
    conn.close()