#!/usr/bin/env python3

import argparse
import json
import logging
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from ipaddress import ip_network

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def validate_port(port):
    try:
        port = int(port)
        if 0 <= port <= 65535:
            return port
        else:
            raise argparse.ArgumentTypeError(f"Port {port} is not in valid range (0-65535)")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Port {port} is not a valid integer")

def scan_port(host, port, timeout):
    """Scan a single port on a host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return port, result == 0
    except Exception as e:
        logger.error(f"Error scanning {host}:{port}: {e}")
        return port, False

def scan_host(host, ports, timeout):
    """Scan all ports on a single host."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {executor.submit(scan_port, host, port, timeout): port for port in ports}
        for future in as_completed(future_to_port):
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
    return {
        "host": host,
        "open_ports": sorted(open_ports),
        "timestamp": __import__('datetime').datetime.now().isoformat()
    }

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("--host", required=True, help="Host or CIDR notation network to scan")
    parser.add_argument("--port", nargs='+', type=validate_port, required=True, help="Port(s) to scan")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout in seconds")
    parser.add_argument("--output", help="Output file for results")
    
    args = parser.parse_args()
    
    # Validate and parse the host
    try:
        if '/' in args.host:
            # CIDR notation
            network = ip_network(args.host, strict=False)
            hosts = [str(ip) for ip in network.hosts()]
        else:
            hosts = [args.host]
    except Exception as e:
        logger.error(f"Invalid host specification: {e}")
        sys.exit(1)
    
    # Scan all hosts
    results = []
    for host in hosts:
        try:
            result = scan_host(host, args.port, args.timeout)
            results.append(result)
        except Exception as e:
            logger.error(f"Error scanning {host}: {e}")
            continue
    
    # Output results
    output_data = {
        "scan_info": {
            "target": args.host,
            "ports": args.port,
            "timeout": args.timeout,
            "timestamp": __import__('datetime').datetime.now().isoformat()
        },
        "results": results
    }
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        logger.info(f"Results saved to {args.output}")
    else:
        print(json.dumps(output_data, indent=2))

if __name__ == "__main__":
    main()