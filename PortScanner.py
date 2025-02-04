import socket
from datetime import datetime
import re
import argparse

def validate_ip(ip):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if ip_pattern.match(ip):
        octets = ip.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            return True
    return False

def validate_domain(domain):
    domain_pattern = re.compile(r"^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$")
    return domain_pattern.match(domain) is not None

def get_ip_from_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print("Could not resolve the domain to an IP address.")
        return None

def port_scanner(target, start_port, end_port):
    print(f"\nScanning Target: {target}")
    print(f"Scanning started at: {datetime.now()}\n")

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Program.")
        return
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return
    except socket.error:
        print("Couldn't connect to server.")
        return

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", type=str, help="Target IP or domain to scan")
    parser.add_argument("--start-port", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="End port (default: 1024)")

    args = parser.parse_args()

    target = args.target
    start_port = args.start_port
    end_port = args.end_port

    # Remove protocol (http/https) if present
    if target.startswith("http://") or target.startswith("https://"):
        target = target.split("//")[1].split('/')[0]

    # Check if target is a valid domain or IP
    if validate_domain(target):
        target_ip = get_ip_from_domain(target)
        if target_ip:
            print(f"Domain resolved to IP: {target_ip}")
            target = target_ip
        else:
            return
    elif not validate_ip(target):
        print("Invalid IP address or domain. Exiting.")
        return

    if target == "127.0.0.1":  # Example forbidden target
        print("This IP is restricted. Please enter a different target.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Ports must be between 1 and 65535, and start-port <= end-port.")
        return

    port_scanner(target, start_port, end_port)

if __name__ == "__main__":
    main()
