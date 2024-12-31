# dashboard.py

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    """
    Connect to the database and retrieve all logs,
    then pass them to the 'dashboard.html' template.
    """
    conn = sqlite3.connect("../nids_logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()  # Each row is (id, fake_ip, payload, status)
    conn.close()

    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    print("Starting Flask Dashboard at http://127.0.0.1:5000")
    app.run(debug=True)
