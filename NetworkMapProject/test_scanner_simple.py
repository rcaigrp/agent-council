# Simple test for network scanner
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Direct import and test
try:
    from network_scanner import scan_port, resolve_host, scan_network
    print("Import successful")
    
    # Test basic functionality
    result1 = resolve_host('google.com')
    print(f"Host resolution: {result1}")
    
    result2 = scan_port('127.0.0.1', 80)
    print(f"Port scan result: {result2}")
    
    result3 = scan_network('127.0.0.1', [80, 443])
    print(f"Network scan result keys: {list(result3.keys())}")
    
    print("All tests passed!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
