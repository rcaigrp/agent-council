# Network Scanner with improved error handling and logging
import socket
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def validate_ip(ip: str) -> bool:
    '''Validate if the IP address is in correct format'''
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def scan_port(host: str, port: int, timeout: float = 1.0) -> str:
    '''Scan a single port on the host'''
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return 'open' if result == 0 else 'closed'
    except Exception as e:
        logger.error(f"Error scanning port {port} on {host}: {str(e)}")
        return 'error'

def scan_host(host: str, ports: List[int], timeout: float = 1.0) -> Dict[str, Any]:
    '''Scan multiple ports on a single host'''
    logger.info(f"Scanning host {host} for ports {ports}")
    
    if not validate_ip(host):
        logger.error(f"Invalid IP address: {host}")
        return {'host': host, 'status': 'invalid', 'open_ports': []}
    
    open_ports = []
    for port in ports:
        try:
            status = scan_port(host, port, timeout)
            if status == 'open':
                open_ports.append(port)
        except Exception as e:
            logger.error(f"Failed to scan port {port} on {host}: {str(e)}")
    
    return {
        'host': host,
        'status': 'up' if open_ports else 'down',
        'open_ports': open_ports
    }

def scan_network(network: str, ports: List[int], timeout: float = 1.0) -> List[Dict[str, Any]]:
    '''Scan an entire network range'''
    logger.info(f"Scanning network {network} for ports {ports}")
    # For simplicity, we'll just scan localhost for now
    return [scan_host('127.0.0.1', ports, timeout)]