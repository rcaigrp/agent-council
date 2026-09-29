import unittest
from unittest.mock import patch
from network_scanner import scan_network

class TestNetworkScanner(unittest.TestCase):
    @patch('network_scanner.scan_network')
    def test_scan_network_success(self):
        # Mock the scan_network function to return True
        self.assertTrue(scan_network())

    @patch('network_scanner.scan_network')
    def test_scan_network_failure(self):
        # Mock the scan_network function to return False
        self.assertFalse(scan_network())
