# capture.py

#Handles live packet capturing using Scapy.
    
from scapy.all import sniff
from main import process_packet

# Captures live network packets and processes them with a callback function.

def live_capture():
    print("Starting live capture...")

     # Sniff packets and call the callback for each one
    
    sniff(filter="ip", prn=handle_packet, store=0)

def handle_packet(pkt):
    fake_ip = "LIVE_FAKE_IP"

    payload_str = str(pkt)

    process_packet(fake_ip, payload_str)

if __name__ == "__main__":
    live_capture()
