import argparse
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from network_scanner import scan_network


def main():
    parser = argparse.ArgumentParser(description='Network Scanner')
    parser.add_argument('--host', required=True, help='Host IP or CIDR range to scan')
    parser.add_argument('--port', default='22,80,443', help='Port(s) to scan (comma-separated or range)')
    parser.add_argument('--timeout', type=int, default=1, help='Timeout in seconds')
    parser.add_argument('--output', help='Output file for results')
    
    args = parser.parse_args()
    
    ports = args.port.split(',')
    ports = [p.strip() for p in ports]
    
    # Convert ranges like '1-100' to a list
    expanded_ports = []
    for port in ports:
        if '-' in port:
            start, end = map(int, port.split('-'))
            expanded_ports.extend(range(start, end + 1))
        else:
            expanded_ports.append(int(port))
    
    results = scan_network(args.host, expanded_ports, args.timeout)
    
    if args.output:
        with open(args.output, 'w') as f:
            import json
            json.dump(results, f)
    else:
        print(results)


if __name__ == '__main__':
    main()