# capture.py
from scapy.all import sniff
from main import process_packet

def live_capture():
    print("Starting live capture...")
    sniff(filter="ip", prn=handle_packet, store=0)

def handle_packet(pkt):
    fake_ip = "LIVE_FAKE_IP"

    payload_str = str(pkt)

    process_packet(fake_ip, payload_str)

if __name__ == "__main__":
    live_capture()
