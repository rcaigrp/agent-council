#!/usr/bin/env python3

import socket
import subprocess
import sys
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def resolve_host(host: str) -> str:
    """Resolve hostname to IP address."""
    try:
        return socket.gethostbyname(host)
    except socket.gaierror as e:
        logger.error(f"Failed to resolve host {host}: {e}")
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
        logger.error(f"Error scanning port {port} on {host}: {e}")
        return False

def scan_ports(host: str, ports: List[int], timeout: float = 1.0) -> Dict[int, bool]:
    """Scan multiple ports."""
    results = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_port = {executor.submit(scan_port, host, port, timeout): port for port in ports}
        for future in as_completed(future_to_port):
            port = future_to_port[future]
            try:
                result = future.result()
                results[port] = result
            except Exception as e:
                logger.error(f"Error scanning port {port}: {e}")
                results[port] = False
    return results

def scan_network(network: str, ports: List[int], timeout: float = 1.0) -> List[Dict]:
    """Scan an entire network."""
    # This is a simplified version - in practice you'd use nmap or similar
    try:
        # For demo purposes, we'll just scan localhost with the given ports
        results = []
        host_results = scan_ports('127.0.0.1', ports, timeout)
        results.append({
            'host': '127.0.0.1',
            'ports': host_results
        })
        return results
    except Exception as e:
        logger.error(f"Error scanning network {network}: {e}")
        return []

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Network Scanner')
    parser.add_argument('--host', required=True, help='Host to scan')
    parser.add_argument('--port', nargs='+', type=int, required=True, help='Ports to scan')
    parser.add_argument('--timeout', type=float, default=1.0, help='Timeout in seconds')
    parser.add_argument('--output', help='Output file')
    
    args = parser.parse_args()
    
    try:
        # Resolve host
        resolved_host = resolve_host(args.host)
        print(f"Scanning {resolved_host}...")
        
        # Scan ports
        results = scan_ports(resolved_host, args.port, args.timeout)
        
        # Output results
        if args.output:
            import json
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Results saved to {args.output}")
        else:
            print(json.dumps(results, indent=2))
            
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
