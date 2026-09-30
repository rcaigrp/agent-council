# Test suite for Network Scanner
import unittest
from unittest.mock import patch, MagicMock
import socket
import network_scanner

class TestNetworkScanner(unittest.TestCase):

    def test_scan_port_success(self):
        with patch('network_scanner.socket.socket') as mock_socket:
            mock_instance = MagicMock()
            mock_socket.return_value = mock_instance
            mock_instance.connect_ex.return_value = 0  # Port open
            result = network_scanner.scan_port('127.0.0.1', 80)
            self.assertTrue(result)

    def test_scan_port_failure(self):
        with patch('network_scanner.socket.socket') as mock_socket:
            mock_instance = MagicMock()
            mock_socket.return_value = mock_instance
            mock_instance.connect_ex.return_value = 1  # Port closed
            result = network_scanner.scan_port('127.0.0.1', 80)
            self.assertFalse(result)

    def test_scan_port_dns_error(self):
        with patch('network_scanner.socket.gaierror') as mock_gaierror:
            # Set up the mock to raise gaierror when called
            mock_gaierror.side_effect = socket.gaierror("Name or service not known")
            
            # Mock the socket creation to avoid actual connection
            with patch('network_scanner.socket.socket') as mock_socket:
                mock_instance = MagicMock()
                mock_socket.return_value = mock_instance
                # Simulate that connect_ex raises gaierror
                mock_instance.connect_ex.side_effect = socket.gaierror("Name or service not known")
                
                result = network_scanner.scan_port('invalid.host', 80)
                # Should return False instead of raising exception
                self.assertFalse(result)

    def test_scan_host(self):
        with patch('network_scanner.scan_port') as mock_scan_port:
            mock_scan_port.return_value = True
            result = network_scanner.scan_host('127.0.0.1', [80, 443])
            self.assertEqual(result, {80: True, 443: True})

    def test_scan_network(self):
        with patch('network_scanner.scan_host') as mock_scan_host:
            mock_scan_host.return_value = {80: True, 443: False}
            result = network_scanner.scan_network('127.0.0.1', [80, 443])
            self.assertEqual(result, {'127.0.0.1': {80: True, 443: False}})

if __name__ == '__main__':
    unittest.main()
