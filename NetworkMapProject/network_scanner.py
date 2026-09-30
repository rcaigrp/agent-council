# Network Scanner Implementation
import socket
import json
from typing import List, Dict, Any

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Scan a single port on a given host.
    Returns True if the port is open, False otherwise.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        return result == 0
    except socket.gaierror:
        # DNS resolution failed - return False instead of re-raising
        return False
    except Exception:
        # Other socket errors - return False
        return False
    finally:
        sock.close()

def scan_host(host: str, ports: List[int], timeout: float = 1.0) -> Dict[str, Any]:
    """
    Scan multiple ports on a single host.
    Returns a dictionary with results.
    """
    results = {}
    for port in ports:
        try:
            results[port] = scan_port(host, port, timeout)
        except Exception as e:
            # Handle any unexpected errors
            results[port] = False
    return results

def scan_network(network: str, ports: List[int], timeout: float = 1.0) -> Dict[str, Any]:
    """
    Scan a network for open ports.
    Supports CIDR notation.
    """
    # Simplified implementation - in real usage, would use ipaddress module
    results = {}
    try:
        # This is a placeholder for actual network scanning logic
        # In production, you'd want to properly parse CIDR and iterate hosts
        results[network] = scan_host(network, ports, timeout)
    except Exception as e:
        print(f"Error scanning network {network}: {e}")
        results[network] = {}
    return results
