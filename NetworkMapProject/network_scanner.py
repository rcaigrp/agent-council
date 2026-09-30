# Network Scanner Module
import socket
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def resolve_host(host: str) -> str:
    """
    Resolve a hostname to IP address.
    
    Args:
        host (str): Hostname or IP address
        
    Returns:
        str: Resolved IP address
    """
    try:
        ip = socket.gethostbyname(host)
        logger.info(f'Resolved {host} to {ip}')
        return ip
    except Exception as e:
        logger.error(f'Failed to resolve {host}: {e}')
        raise

def scan_port(host: str, port: int, timeout: float = 1.0) -> str:
    """
    Scan a single port on a host.
    
    Args:
        host (str): Host to scan
        port (int): Port number to scan
        timeout (float): Timeout in seconds
        
    Returns:
        str: Result of the scan ('open' or 'closed')
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            return 'open'
        else:
            return 'closed'
    except Exception as e:
        logger.error(f'Error scanning port {port} on {host}: {e}')
        raise

def scan_network(host: str, ports: List[int], timeout: float = 1.0) -> Dict[str, Any]:
    """
    Scan multiple ports on a host.
    
    Args:
        host (str): Host to scan
        ports (List[int]): List of ports to scan
        timeout (float): Timeout in seconds
        
    Returns:
        Dict[str, Any]: Dictionary containing scan results
    """
    results = {}
    
    # Resolve host if needed
    try:
        resolved_host = resolve_host(host)
        results['host'] = resolved_host
    except Exception as e:
        logger.error(f'Failed to resolve host {host}: {e}')
        results['host'] = host
        
    # Scan each port
    for port in ports:
        try:
            status = scan_port(resolved_host, port, timeout)
            results[f'port_{port}'] = status
        except Exception as e:
            logger.error(f'Error scanning port {port}: {e}')
            results[f'port_{port}'] = 'error'
    
    return results

# Make the module executable for direct testing
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            print('Network scanner module test')
        else:
            print(f'Usage: python network_scanner.py test')
    else:
        print('Network scanner module loaded successfully')