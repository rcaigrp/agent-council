import unittest
from unittest.mock import patch, MagicMock
import socket  # Added missing import
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from network_scanner import scan_port, scan_ports, scan_host_range

class TestNetworkScanner(unittest.TestCase):
    
    def test_scan_port_success(self):
        # Mock successful connection
        with patch('socket.socket') as mock_socket:
            mock_instance = MagicMock()
            mock_socket.return_value.__enter__.return_value = mock_instance
            mock_instance.connect_ex.return_value = 0
            result = scan_port("127.0.0.1", 80)
            self.assertTrue(result)
            
    def test_scan_port_failure(self):
        # Mock failed connection
        with patch('socket.socket') as mock_socket:
            mock_instance = MagicMock()
            mock_socket.return_value.__enter__.return_value = mock_instance
            mock_instance.connect_ex.return_value = 1
            result = scan_port("127.0.0.1", 80)
            self.assertFalse(result)
            
    def test_scan_port_dns_error(self):
        # Mock DNS resolution error by patching socket.gaierror directly in network_scanner module context
        with patch('network_scanner.socket.gaierror') as mock_gaierror:
            mock_gaierror.side_effect = socket.gaierror("Name or service not known")
            with patch('socket.socket') as mock_socket:
                mock_socket.side_effect = socket.gaierror("Name or service not known")
                result = scan_port("invalid.host", 80)
                self.assertFalse(result)
                
    def test_scan_ports_multiple(self):
        # Test scanning multiple ports
        with patch('network_scanner.scan_port') as mock_scan:
            mock_scan.side_effect = [True, False]
            result = scan_ports("127.0.0.1", [80, 443])
            self.assertEqual(result, {80: True, 443: False})
            
    def test_scan_host_range(self):
        # Test host range scanning (mock implementation)
        result = scan_host_range("192.168.1.0/24", [80, 443])
        self.assertIsInstance(result, dict)
        
    def test_invalid_input_handling(self):
        # Test with invalid input
        with patch('socket.socket') as mock_socket:
            mock_socket.side_effect = Exception("Test error")
            result = scan_port("127.0.0.1", 80)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()