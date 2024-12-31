# populate.py

#Populates the SQLite database with fake logs for testing purposes.

from src.main import process_packet
from src.log_handler import initialize_database

def populate_fake_traffic():
    
  # Inserts sample logs into the database for testing the dashboard.
    
    initialize_database()

    # Insert fake data
    
    fake_packets = [
        ("FAKE_IP_1", "safe_data"),
        ("FAKE_IP_2", "malicious_payload_1"),
        ("FAKE_IP_3", "hello_world"),
        ("FAKE_IP_4", "malicious_payload_2"),
        ("FAKE_IP_5", "just_test_data"),
        ("FAKE_IP_6", "malicious_payload_1"),
        ("FAKE_IP_7", "random_info"),
        ("FAKE_IP_8", "another_string"),
        ("FAKE_IP_9", "malicious_payload_2"),
        ("FAKE_IP_10", "nothing_to_see_here"),
    ]

    
    for (fake_ip, payload) in fake_packets:
        process_packet(fake_ip, payload)

if __name__ == "__main__":
    populate_fake_traffic()
