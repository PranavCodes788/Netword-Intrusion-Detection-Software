# dashboard.py
#Flask-based web dashboard to display packet logs from the SQLite database.
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
     #Renders the dashboard HTML template with packet logs from the database.
    conn = sqlite3.connect("../nids_logs.db")

      # Fetch all logs from the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()  # Each row is (id, fake_ip, payload, status)
    conn.close()
 # Pass logs to the template
    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    print("Starting Flask Dashboard at http://127.0.0.1:5000")
     # Run the Flask server
    app.run(debug=True)
