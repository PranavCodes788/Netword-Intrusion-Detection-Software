# main.py


#Entry point for the Network Intrusion Detection System (NIDS).
#Initializes the database and starts packet capturing.


from src.analyze import analyze_data
from src.log_handler import initialize_database, log_entry
"Process each captured packet"
def process_packet(fake_ip, payload):
    
   # Analyze the (fake_ip, payload) pair, then log the result.
    
    status = analyze_data(fake_ip, payload)

     # Log the result in the SQLite database
    log_entry(fake_ip, payload, status)

    # Print detection results
    
    if status == "Intrusion Detected":
        print(f"🚨 ALERT: Intrusion detected. IP: {fake_ip}, Payload: {payload}")
    else:
        print(f"✅ Safe. IP: {fake_ip}, Payload: {payload}")

if __name__ == "__main__":
    # Initialize the SQLite database
    initialize_database()
    print("main.py executed. Database ready.")
# Start capturing packets and processing them
    capture_packets(process_packet)
