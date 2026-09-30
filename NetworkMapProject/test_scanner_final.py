import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the actual scanner module
try:
    from network_scanner import scan_port, resolve_host, scan_network
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

class TestNetworkScanner(unittest.TestCase):
    
    def test_scan_port(self):
        # Test with a non-routable IP and port that should timeout
        result = scan_port('10.255.255.255', 80, 1)
        self.assertFalse(result)
        
    def test_resolve_host(self):
        # Test resolving localhost
        result = resolve_host('localhost')
        self.assertIsNotNone(result)
        
    def test_scan_network(self):
        # Test scanning a small network range
        result = scan_network('127.0.0.1/32', [80], 1)
        self.assertIsInstance(result, list)
        
if __name__ == '__main__':
    unittest.main()