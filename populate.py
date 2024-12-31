# populate.py

from src.main import process_packet
from src.log_handler import initialize_database

def populate_fake_traffic():
    """
    Inserts multiple 'fake' IP/payload pairs into the database.
    Some are malicious, some are safe.
    """
    # Make sure the database is set up
    initialize_database()

    # List of (fake_ip, payload) pairs
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

    # Process each "packet"
    for (fake_ip, payload) in fake_packets:
        process_packet(fake_ip, payload)

if __name__ == "__main__":
    populate_fake_traffic()
