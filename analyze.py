

known_patterns = [
    "malicious_payload_1",
    "malicious_payload_2"
]

def analyze_data(fake_ip, payload):
    """
    We pretend to analyze 'fake_ip' and 'payload'.
    Returns "Intrusion Detected" if any known pattern is found.
    Otherwise returns "Safe".
    """
    for pattern in known_patterns:
        # If malicious pattern is in the payload, flag as Intrusion
        if pattern in payload:
            return "Intrusion Detected"
    return "Safe"
