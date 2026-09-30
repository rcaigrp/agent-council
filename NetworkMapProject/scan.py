#!/usr/bin/env python3

import argparse
import json
from scapy.all import IP, TCP, sr1
import sys

# Simplified scanner implementation for testing purposes
def scan_port(ip, port, timeout=1):
    """Scan a single port on an IP address."""
    try:
        # Create SYN packet
        pkt = IP(dst=ip)/TCP(dport=port, flags="S")
        response = sr1(pkt, timeout=timeout, verbose=0)
        
        if response and response.haslayer(TCP):
            # Check if port is open (SYN-ACK)
            if response[TCP].flags == 0x12:  # SYN-ACK
                return True
        return False
    except Exception as e:
        print(f"Error scanning {ip}:{port} - {e}", file=sys.stderr)
        return False

def scan_host(host, ports, timeout=1):
    """Scan multiple ports on a single host."""
    results = {}
    for port in ports:
        open_port = scan_port(host, port, timeout)
        results[port] = open_port
    return results

def main():
    parser = argparse.ArgumentParser(description='Network Scanner')
    parser.add_argument('--host', required=True, help='IP address or network range to scan')
    parser.add_argument('--port', required=True, help='Port(s) to scan (comma-separated)')
    parser.add_argument('--timeout', type=int, default=1, help='Timeout in seconds')
    parser.add_argument('--output', default='results.json', help='Output file for results')
    
    args = parser.parse_args()
    
    # Parse ports
    ports = [int(p.strip()) for p in args.port.split(',')]
    
    # Scan host (simplified)
    scan_results = scan_host(args.host, ports, args.timeout)
    
    # Save results
    with open(args.output, 'w') as f:
        json.dump(scan_results, f, indent=2)
    
    print(f"Scan results saved to {args.output}")

if __name__ == '__main__':
    main()