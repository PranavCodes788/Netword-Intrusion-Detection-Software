#Performs threat analysis on network packets.

known_patterns = [
    "malicious_payload_1",
    "malicious_payload_2"
]
# Analyzes a packet and determines its safety.
def analyze_data(fake_ip, payload):

    for pattern in known_patterns:
        # If malicious pattern is in the payload, flag as Intrusion
        if pattern in payload:
            return "Intrusion Detected"
    return "Safe"
