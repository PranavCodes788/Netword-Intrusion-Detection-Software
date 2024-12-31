# main.py

from src.analyze import analyze_data
from src.log_handler import initialize_database, log_entry

def process_packet(fake_ip, payload):
    """
    Analyze the (fake_ip, payload) pair, then log the result.
    """
    status = analyze_data(fake_ip, payload)
    log_entry(fake_ip, payload, status)
    if status == "Intrusion Detected":
        print(f"🚨 ALERT: Intrusion detected. IP: {fake_ip}, Payload: {payload}")
    else:
        print(f"✅ Safe. IP: {fake_ip}, Payload: {payload}")

if __name__ == "__main__":
   
    initialize_database()
    print("main.py executed. Database ready.")
