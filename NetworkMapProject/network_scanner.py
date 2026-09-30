# Network Scanner Module
import socket
import sys
import logging
from typing import List, Dict, Optional

def scan_port(host: str, port: int, timeout: float) -> bool:
    """
    Scan a single port on a host.
    Returns True if the port is open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        logging.error(f"Error scanning port {port} on {host}: {e}")
        return False

def resolve_host(hostname: str) -> Optional[str]:
    """
    Resolve a hostname to an IP address.
    Returns the IP address or None if resolution fails.
    """
    try:
        result = socket.getaddrinfo(hostname, None)
        return result[0][4][0]
    except socket.gaierror as e:
        logging.error(f"DNS resolution failed for {hostname}: {e}")
        raise

def scan_host(hostname: str, ports: List[int], timeout: float) -> Dict[str, Dict[str, List[int]]]:
    """
    Scan multiple ports on a host.
    Returns a dictionary with hostname as key and IP address as key in nested dict with open ports list.
    """
    try:
        ip_address = resolve_host(hostname)
        open_ports = []
        for port in ports:
            if scan_port(ip_address, port, timeout):
                open_ports.append(port)
        return {hostname: {ip_address: open_ports}}
    except socket.gaierror:
        return {hostname: {}}
    except Exception as e:
        logging.error(f"Error scanning host {hostname}: {e}")
        return {hostname: {}}