# log_handler.py

import sqlite3

def initialize_database():
    """
    Create a database (nids_logs.db) with a table named 'logs'
    if it doesn't already exist.
    """
    conn = sqlite3.connect("../nids_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fake_ip TEXT,
            payload TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_entry(fake_ip, payload, status):
    """
    Insert a new log entry into the database.
    """
    conn = sqlite3.connect("../nids_logs.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logs (fake_ip, payload, status) VALUES (?, ?, ?)",
        (fake_ip, payload, status)
    )
    conn.commit()
    conn.close()
