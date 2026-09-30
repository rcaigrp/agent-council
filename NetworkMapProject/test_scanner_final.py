#!/usr/bin/env python3

import unittest
from network_scanner import scan_port, resolve_host, scan_ports, scan_network

class TestNetworkScanner(unittest.TestCase):
    def test_resolve_host(self):
        # Test valid hostname resolution
        result = resolve_host('google.com')
        self.assertIsInstance(result, str)

    def test_scan_port(self):
        # Test port scanning (should return False for closed ports)
        result = scan_port('127.0.0.1', 80)
        self.assertFalse(result)

    def test_scan_ports(self):
        # Test scanning multiple ports
        ports = [22, 80, 443]
        result = scan_ports('127.0.0.1', ports)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 3)

    def test_scan_network(self):
        # Test scanning a network range (simplified test)
        result = scan_network('127.0.0.1/32', [22, 80])
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
