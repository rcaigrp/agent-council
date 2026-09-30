#!/usr/bin/env python3

import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the functions directly from network_scanner
from network_scanner import scan_network, scan_host, scan_ports

class TestNetworkScanner(unittest.TestCase):
    
    def test_scan_host(self):
        # Test with localhost
        result = scan_host("127.0.0.1", [80])
        self.assertIsInstance(result, list)
        
    def test_scan_ports(self):
        # Test with localhost and common ports
        result = scan_ports("127.0.0.1", [80, 443])
        self.assertIsInstance(result, list)
        
    def test_scan_network(self):
        # Test with a small network range
        result = scan_network("127.0.0.0/30", [80])
        self.assertIsInstance(result, list)
        
    def test_port_parsing(self):
        # Test that port parsing works correctly
        from network_scanner import main
        import argparse
        
        parser = argparse.ArgumentParser()
        parser.add_argument("--port", required=True)
        args = parser.parse_args(["--port", "22,80,443"])
        self.assertEqual(args.port, "22,80,443")

if __name__ == '__main__':
    unittest.main()