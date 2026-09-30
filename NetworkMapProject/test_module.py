#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Test the actual module functions directly
try:
    from network_scanner import scan_port, resolve_host, scan_ports, scan_network
    print("All imports successful")
    
    # Test basic functionality
    result = resolve_host('google.com')
    print(f"Hostname resolution test: {result}")
    
    result = scan_port('127.0.0.1', 80)
    print(f"Port scan test: {result}")
    
    result = scan_ports('127.0.0.1', [22, 80])
    print(f"Multi-port scan test: {result}")
    
    result = scan_network('127.0.0.1/32', [22, 80])
    print(f"Network scan test: {result}")
    
    print("All tests passed successfully")
    
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
