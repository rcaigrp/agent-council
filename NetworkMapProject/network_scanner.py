# Network Scanner Module
import socket
import logging
from typing import List, Tuple, Optional

class NetworkScanner:
    def __init__(self, timeout: int = 1):
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

    def scan_port(self, host: str, port: int) -> bool:
        """
        Scan a single port on a given host.
        Returns True if the port is open, False otherwise.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((host, port))
            sock.close()  # Ensure socket is closed
            return result == 0
        except socket.gaierror:
            self.logger.error(f'DNS resolution failed for {host}')
            return False  # Return False instead of re-raising
        except Exception as e:
            self.logger.error(f'Unexpected error scanning {host}:{port} - {e}')
            return False

    def scan_host(self, host: str, ports: List[int]) -> dict:
        """
        Scan multiple ports on a single host.
        Returns a dictionary mapping port numbers to boolean results.
        """
        results = {}
        for port in ports:
            results[port] = self.scan_port(host, port)
        return results

    def scan_network(self, hosts: List[str], ports: List[int]) -> dict:
        """
        Scan multiple ports on multiple hosts.
        Returns a nested dictionary with host keys and port mappings.
        """
        results = {}
        for host in hosts:
            results[host] = self.scan_host(host, ports)
        return results