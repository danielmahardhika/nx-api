import base64
import requests
import json
import urllib3
from typing import Dict, Any

# Disable SSL warnings (not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# NX sandbox credentials
CISCO_URL = "https://sbx-nxos-mgmt.cisco.com"
USERNAME = "admin"
PASSWORD = "Admin_1234!"

# Create auth using base64
AUTH = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode('utf-8')).decode('utf-8')

# Set headers for request
HEADERS = {
    'content-type': 'application/json-rpc',
    'authorization': f"Basic {AUTH}"
}

PAYLOAD = {
    "show_run": {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show run",
            "version": 1
        },
        "id": 1
    },
    "list_interfaces": {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show interface",
            "version": 1
        },
        "id": 2
    },
    "detail_information": {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show hardware",
            "version": 1
        },
        "id": 3
    },
    "non_vlan": {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show interface brief",
            "version": 1
        },
        "id": 4
    },
}

def send_request_to_sandbox(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Send a request to the Cisco NX-API sandbox."""
    url = f"{CISCO_URL}/ins"
    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(payload), verify=False)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return {}

def show_run():
    """Show running configuration."""
    response = send_request_to_sandbox(PAYLOAD["show_run"])
    print(json.dumps(response, indent=2))

def list_interfaces():
    """List all interfaces."""
    response = send_request_to_sandbox(PAYLOAD["list_interfaces"])
    print(json.dumps(response, indent=2))

def detail_information():
    """Show hardware details."""
    response = send_request_to_sandbox(PAYLOAD["detail_information"])
    print(json.dumps(response, indent=2))

def non_vlan_details():
    """Show interface brief (non-VLAN)."""
    response = send_request_to_sandbox(PAYLOAD["non_vlan"])
    print(json.dumps(response, indent=2))

def display_menu():
    """Display the main menu."""
    print("\nCisco NX-API Menu:")
    print("1. Show Running Configuration")
    print("2. List Interfaces")
    print("3. Show Hardware Details")
    print("4. Show Interface Brief (Non-VLAN)")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            show_run()
        elif choice == '2':
            list_interfaces()
        elif choice == '3':
            detail_information()
        elif choice == '4':
            non_vlan_details()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()