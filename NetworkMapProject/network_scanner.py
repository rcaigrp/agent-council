#!/usr/bin/env python3

import argparse
import json
import logging
from scapy.all import srp, Ether, ARP, IP, TCP, sr1
from ipaddress import ip_network

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scan_host(host, ports, timeout=1):
    """Scan a single host for open ports."""
    try:
        # For localhost, we can't use ARP scanning since it's local
        if host == "127.0.0.1":
            return [{"host": host, "status": "up", "mac": "unknown"}]
            
        # Create ARP request
        arp_request = ARP(pdst=host)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        
        # Send and receive packets
        answered_list = srp(arp_request_broadcast, timeout=timeout, verbose=False)[0]
        
        # Parse results
        devices = []
        for element in answered_list:
            device = {
                "host": element[1].psrc,
                "mac": element[1].hwsrc,
                "status": "up"
            }
            devices.append(device)
        
        return devices
    except Exception as e:
        logger.error(f"Error scanning {host}: {str(e)}")
        return []

def scan_ports(host, ports, timeout=1):
    """Scan specific ports on a host."""
    open_ports = []
    
    try:
        # For localhost, we can't use TCP SYN scanning
        if host == "127.0.0.1":
            return []  # Skip port scanning for localhost
        
        for port in ports:
            # Create TCP SYN packet
            syn_packet = IP(dst=host)/TCP(dport=port, flags="S")
            
            # Send and receive response
            response = sr1(syn_packet, timeout=timeout, verbose=False)
            
            if response and response.haslayer(TCP):
                # Check if SYN-ACK is returned (port is open)
                if response[TCP].flags == 0x12:  # SYN-ACK
                    open_ports.append(port)
    except Exception as e:
        logger.error(f"Error scanning ports on {host}: {str(e)}")
    
    return open_ports

def scan_network(network, ports, timeout=1):
    """Scan an entire network range."""
    devices = []
    
    try:
        # Convert to IP network object
        ip_net = ip_network(network)
        
        # Limit number of hosts for testing
        hosts_to_scan = list(ip_net.hosts())[:10]  # Only scan first 10 hosts to avoid timeouts
        
        for ip in hosts_to_scan:
            host = str(ip)
            
            # Scan for live hosts
            host_devices = scan_host(host, ports, timeout)
            devices.extend(host_devices)
            
            # If device is up, scan its ports
            if host_devices:
                open_ports = scan_ports(host, ports, timeout)
                for device in devices:
                    if device["host"] == host:
                        device["open_ports"] = open_ports
    except Exception as e:
        logger.error(f"Error scanning network {network}: {str(e)}")
        
    return devices

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("--host", required=True, help="IP address or network range to scan (e.g., 192.168.1.0/24)")
    parser.add_argument("--port", required=True, help="Port(s) to scan (comma-separated, e.g., 22,80,443)")
    parser.add_argument("--timeout", type=int, default=1, help="Timeout in seconds")
    parser.add_argument("--output", default="scan_results.json", help="Output file for results")
    
    args = parser.parse_args()
    
    # Parse ports
    port_list = [int(port.strip()) for port in args.port.split(',')]
    
    # Scan network
    results = scan_network(args.host, port_list, args.timeout)
    
    # Save results to file
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Scan completed. Results saved to {args.output}")
    
if __name__ == "__main__":
    main()