#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import socket

# Import the module we're testing
import network_scanner

class TestNetworkScanner(unittest.TestCase):
    
    @patch('network_scanner.socket.socket')
    def test_scan_port_success(self, mock_socket_class):
        # Setup mock socket
        mock_socket_instance = MagicMock()
        mock_socket_class.return_value = mock_socket_instance
        mock_socket_instance.connect_ex.return_value = 0  # Port is open
        
        result = network_scanner.scan_port('127.0.0.1', 80)
        self.assertTrue(result)
        
    @patch('network_scanner.socket.socket')
    def test_scan_port_failure(self, mock_socket_class):
        # Setup mock socket
        mock_socket_instance = MagicMock()
        mock_socket_class.return_value = mock_socket_instance
        mock_socket_instance.connect_ex.return_value = 1  # Port is closed
        
        result = network_scanner.scan_port('127.0.0.1', 80)
        self.assertFalse(result)
        
    @patch('network_scanner.socket.gaierror')
    def test_scan_port_dns_error(self, mock_gaierror):
        # Setup mock gaierror
        mock_gaierror.side_effect = socket.gaierror(8, 'nodename nor servname provided, or not known')
        
        with patch('network_scanner.socket.socket') as mock_socket_class:
            mock_socket_instance = MagicMock()
            mock_socket_class.return_value = mock_socket_instance
            # Mock connect_ex to raise gaierror
            mock_socket_instance.connect_ex.side_effect = socket.gaierror(8, 'nodename nor servname provided, or not known')
            
            result = network_scanner.scan_port('invalid-host', 80)
            self.assertFalse(result)
            
    def test_scan_host(self):
        # Test with a valid port
        result = network_scanner.scan_host('127.0.0.1', [80])
        self.assertIsInstance(result, dict)
        
    def test_scan_network(self):
        # Test with a small network range
        result = network_scanner.scan_network('127.0.0.1/30', [80])
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()