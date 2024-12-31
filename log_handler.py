# log_handler.py

#Manages logging and database operations for captured packets.

import sqlite3

def initialize_database():
    #Creates the SQLite database and the 'logs' table for storing packet information.
    conn = sqlite3.connect("../nids_logs.db")
    cursor = conn.cursor()
    cursor.execute(
        
        #CREATE TABLE IF NOT EXISTS logs (
           # id INTEGER PRIMARY KEY AUTOINCREMENT,
          #  fake_ip TEXT,
           # payload TEXT,
           # status TEXT
        #)
    #)
    conn.commit()
    conn.close()
#Logs the analyzed packet and its status into the SQLite database.

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
