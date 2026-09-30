#!/usr/bin/env python3

import socket
import logging
from ipaddress import ip_network

def scan_port(host, port, timeout=1):
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
    except socket.gaierror:
        # DNS resolution failed - this is expected behavior for invalid hosts
        logging.debug(f'DNS resolution failed for {host}')
        return False
    except Exception as e:
        logging.error(f'Unexpected error scanning port {port} on {host}: {e}')
        return False


def scan_host(host, ports, timeout=1):
    """
    Scan multiple ports on a single host.
    Returns a dictionary of port results.
    """
    results = {}
    for port in ports:
        results[port] = scan_port(host, port, timeout)
    return results


def scan_network(network, ports, timeout=1):
    """
    Scan multiple hosts and ports in a network range.
    Returns a dictionary with host keys and port result dictionaries.
    """
    results = {}
    try:
        for ip in ip_network(network).hosts():
            host = str(ip)
            results[host] = scan_host(host, ports, timeout)
    except Exception as e:
        logging.error(f'Error scanning network {network}: {e}')
    return results