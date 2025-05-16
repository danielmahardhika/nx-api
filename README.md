# NX-API Python Scripts

## Overview

This repository contains two Python scripts for interacting with Cisco NX-OS devices using the NX-API. The scripts allow users to manage configurations and retrieve information from the device.

### Files

1. **nxapirest.py**: A script that uses the REST API to manage SNMP, interfaces, and VLANs on a Cisco NX-OS device.
2. **nxapicli.py**: A script that uses the CLI over the NX-API to execute commands and retrieve configuration details.

## Requirements

- Python 3.x
- `requests` library
- `json` library
- `urllib3` library

You can install the required libraries using pip:

```bash
pip install requests urllib3
```

## Usage

### nxapirest.py

This script allows you to:

- Get and configure SNMP settings.
- Manage interfaces.
- Create, delete, and retrieve VLANs.

#### Running the Script

To run the script, execute the following command:

```bash
python nxapirest.py
```

Follow the on-screen menu to choose the desired operation.

### nxapicli.py

This script allows you to:

- Show the running configuration.
- List interfaces.
- Show hardware details.
- Display interface brief (non-VLAN).

#### Running the Script

To run the script, execute the following command:

```bash
python nxapicli.py
```

Choose the desired command from the menu that appears.

## Security Note

Both scripts disable SSL verification for simplicity. This is **not recommended for production**. Ensure to implement proper SSL verification in a production environment.
