import unittest
from unittest.mock import patch, MagicMock
import socket

# Import the module we're testing
from network_scanner import NetworkScanner

class TestNetworkScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = NetworkScanner(timeout=1)

    @patch('network_scanner.socket')
    def test_scan_port_dns_error(self, mock_socket):
        # Mock socket.gaierror at the module level
        mock_socket.gaierror = socket.gaierror
        mock_socket.socket.return_value.connect_ex.side_effect = socket.gaierror()
        
        result = self.scanner.scan_port('invalid.host', 80)
        self.assertFalse(result)  # Should return False, not raise exception

    @patch('network_scanner.socket')
    def test_scan_port_success(self, mock_socket):
        mock_socket.socket.return_value.connect_ex.return_value = 0
        result = self.scanner.scan_port('127.0.0.1', 80)
        self.assertTrue(result)

    @patch('network_scanner.socket')
    def test_scan_port_failure(self, mock_socket):
        mock_socket.socket.return_value.connect_ex.return_value = 1
        result = self.scanner.scan_port('127.0.0.1', 80)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()