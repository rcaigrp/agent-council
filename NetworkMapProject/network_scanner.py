# Network Scanner Module
import socket
import logging
from typing import List, Dict, Any

def resolve_host(host: str) -> str:
    """Resolve hostname to IP address."""
    try:
        addr_info = socket.getaddrinfo(host, None)
        return addr_info[0][4][0]
    except socket.gaierror as e:
        logging.error(f'DNS resolution failed for {host}: {e}')
        raise

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Scan a single port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        logging.error(f'Error scanning port {port} on {host}: {e}')
        return False

def scan_ports(host: str, ports: List[int], timeout: float = 1.0) -> List[Dict[str, Any]]:
    """Scan multiple ports."""
    results = []
    for port in ports:
        status = 'open' if scan_port(host, port, timeout) else 'closed'
        results.append({'port': port, 'status': status})
    return results