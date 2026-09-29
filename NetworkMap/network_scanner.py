#!/usr/bin/env python3

import json
from scapy.all import sr1, IP, TCP

def scan_ports(host, port_range, timeout=1):
    """
    Scan a host for open ports in the given range.
    
    Args:
        host (str): The target host to scan
        port_range (list): List of ports to scan
        timeout (int): Timeout in seconds

    Returns:
        dict: Scan results with open ports
    """
    open_ports = []
    
    for port in port_range:
        # Create TCP SYN packet
        pkt = IP(dst=host) / TCP(dport=port, flags="S")
        
        # Send packet and receive response
        response = sr1(pkt, timeout=timeout, verbose=False)
        
        # Check if we got a SYN-ACK back (port is open)
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:  # SYN-ACK
            open_ports.append(port)
            
    return {
        "host": host,
        "ports": open_ports,
        "timestamp": "2023-06-15T10:00:00Z"
    }

def save_results(results, filename="scan_results.json"):
    """
    Save scan results to a JSON file.
    
    Args:
        results (dict): The scan results
        filename (str): Output filename
    """
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    # Example usage
    target_host = "192.168.1.1"
    ports_to_scan = [22, 80, 443]
    
    scan_results = scan_ports(target_host, ports_to_scan)
    save_results(scan_results)
    print(f"Scan complete. Results saved to scan_results.json")