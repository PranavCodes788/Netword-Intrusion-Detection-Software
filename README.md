# Network Intrusion Detection System (NIDS)

A Python-based project for monitoring network traffic, detecting intrusions, and logging results. Includes a Flask dashboard for visualizing logs.

## Features
- **Packet Monitoring**: Captures live network packets using Scapy.
- **Threat Analysis**: Flags packets as "Safe" or "Intrusion Detected" using a simple rule-based engine.
- **Logging**: Stores analyzed packets and their statuses in an SQLite database.
- **Web Dashboard**: Displays logs in a dynamic table using Flask for real-time visualization.

## Technologies Used
- **Python**: Core programming language.
- **Flask**: For building the web-based dashboard.
- **SQLite**: To store logs and threat data.
- **Scapy**: For packet sniffing and traffic analysis.

## Installation

### Prerequisites
1. Python 3.x installed on your system.
2. A virtual environment (optional but recommended).
3. Admin/root permissions (required to capture live packets).



