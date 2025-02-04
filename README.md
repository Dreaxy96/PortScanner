# PortScanner
A simple and efficient Python-based tool to scan open ports on target systems.





#  Usage Guide

## Required Libraries (Pip Installations)

This project requires no additional libraries other than the ones included in Python by default. However, if you want to install any extra dependencies, you can use the `requirements.txt` file. To install the libraries listed in `requirements.txt`, run:

```bash
pip install -r requirements.txt
```
Usage Instructions
1. Ensure Python is Installed:
If you don’t have Python installed, you can download it from here.

2. Clone or Download the Project:
Using Git:
```bash
git clone https://github.com/Dreaxy96/PortScanner.git
cd PortScanner
```
Alternatively, you can download the ZIP file from GitHub and extract it.
3. Run the Script:
Open your terminal or command prompt and run the following command to execute the port scanner:
```bash
python portscanner.py <TARGET_IP_OR_DOMAIN> --start-port <START_PORT> --end-port <END_PORT>
```
<TARGET_IP_OR_DOMAIN>: Enter the IP address or domain you want to scan.
<START_PORT> and <END_PORT>: Specify the range of ports you want to scan.
Example Usage:
```bash
python portscanner.py 192.168.1.1 --start-port 20 --end-port 80
```
This command will resolve the domain example.com to its IP address and scan ports 80 to 100.

4. Domain or IP Validation:
If you provide a domain, the script will automatically resolve it to an IP address.
If you provide an IP address, the script will directly start the scan.
The program checks whether the provided IP is valid. If not, it will display an error message.
5. Port Scanning:
The program will list open ports within the specified range. For example:
```bash
Port 22: OPEN
Port 80: OPEN
```
6. Error Handling:
If an error occurs (e.g., the IP cannot be resolved or the connection fails), the script will display appropriate error messages.
The IP 127.0.0.1 is restricted from scanning, as it refers to the local machine.


