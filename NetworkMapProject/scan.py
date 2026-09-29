#!/usr/bin/env python3
import argparse
from network_scanner import ping_sweep, port_scan

def main():
    parser = argparse.ArgumentParser(description='Network Scanner')
    parser.add_argument('--host', required=True, help='Host to scan')
    parser.add_argument('--port', nargs='+', type=int, help='Port(s) to scan')
    parser.add_argument('--timeout', type=int, default=1, help='Timeout in seconds')
    parser.add_argument('--output', default='results.json', help='Output file')
    
    args = parser.parse_args()
    
    # Perform ping sweep
    hosts = ping_sweep(args.host)
    
    # Perform port scan on each host
    scan_results = {}
    for host in hosts:
        if args.port:
            open_ports = port_scan(host, args.port)
            scan_results[host] = {'open_ports': open_ports}
        else:
            scan_results[host] = {'reachable': True}
    
    # Save results to file
    import json
    with open(args.output, 'w') as f:
        json.dump(scan_results, f)
    
    print(f'Scan completed. Results saved to {args.output}')

if __name__ == '__main__':
    main()
