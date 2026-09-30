#!/usr/bin/env python3

import argparse
from scapy.all import IP, TCP, ICMP, sr1, sr
import json
import sys

def scan_host(host, ports, timeout=1):
    """
    Scan a single host for open ports
    """
    results = {}
    
    # Create IP packet
    ip_layer = IP(dst=host)
    
    # If no ports specified, scan common ones
    if not ports:
        ports = [22, 80, 443]
    
    for port in ports:
        # Create TCP packet with SYN flag
        tcp_layer = TCP(sport=12345, dport=port, flags="S")
        
        # Combine layers
        packet = ip_layer / tcp_layer
        
        try:
            # Send packet and receive response
            response = sr1(packet, timeout=timeout, verbose=False)
            
            if response and response.haslayer(TCP):
                # Check if SYN-ACK is returned (port is open)
                if response.getlayer(TCP).flags == 0x12:  # SYN-ACK
                    results[port] = "open"
                elif response.getlayer(TCP).flags == 0x14:  # RST-ACK
                    results[port] = "closed"
            else:
                results[port] = "filtered"
        except Exception as e:
            results[port] = f"error: {str(e)}"
    
    return results

def scan_network(network, ports, timeout=1):
    """
    Scan an entire network range
    """
    from scapy.all import IP, TCP, ICMP, sr1, sr
    
    # For simplicity, we'll just scan the first few hosts in a range
    # In a production implementation, this would use proper CIDR handling
    results = {}
    
    # This is a simplified approach - real implementation would parse CIDR properly
    if '/' in network:
        base_ip, cidr = network.split('/')
        cidr = int(cidr)
        # For demo purposes, just scan 5 hosts
        for i in range(1, min(6, 2**(32-cidr))):
            host = f"{base_ip.rsplit('.', 1)[0]}.{i}"
            try:
                results[host] = scan_host(host, ports, timeout)
            except Exception as e:
                results[host] = {"error": str(e)}
    else:
        # Single host scan
        results[network] = scan_host(network, ports, timeout)
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Network Scanner')
    parser.add_argument('--host', required=True, help='Host or network to scan (e.g., 192.168.1.1 or 192.168.1.0/24)')
    parser.add_argument('--port', nargs='+', type=int, help='Port(s) to scan')
    parser.add_argument('--timeout', type=int, default=1, help='Timeout in seconds')
    parser.add_argument('--output', help='Output file for results')
    
    args = parser.parse_args()
    
    try:
        if '/' in args.host:
            # Network scan
            results = scan_network(args.host, args.port, args.timeout)
        else:
            # Single host scan
            results = {args.host: scan_host(args.host, args.port, args.timeout)}
        
        # Output results
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Scan results saved to {args.output}")
        else:
            print(json.dumps(results, indent=2))
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()