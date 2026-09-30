import unittest
from unittest.mock import patch, MagicMock
import socket
import json

class TestNetworkScanner(unittest.TestCase):
    
    @patch('socket.socket')
    def test_scan_port_open(self, mock_socket):
        # Mock a successful connection
        mock_conn = MagicMock()
        mock_socket.return_value = mock_conn
        mock_conn.connect_ex.return_value = 0  # Connection successful
        
        # Test scan function logic
        from scanner import scan_port
        result = scan_port('127.0.0.1', 80)
        self.assertEqual(result, 'open')
        
    @patch('socket.socket')
    def test_scan_port_closed(self, mock_socket):
        # Mock a failed connection
        mock_conn = MagicMock()
        mock_socket.return_value = mock_conn
        mock_conn.connect_ex.return_value = 1  # Connection failed
        
        from scanner import scan_port
        result = scan_port('127.0.0.1', 80)
        self.assertEqual(result, 'closed')
        
    def test_validate_ip_valid(self):
        from scanner import validate_ip
        self.assertTrue(validate_ip('192.168.1.1'))
        
    def test_validate_ip_invalid(self):
        from scanner import validate_ip
        self.assertFalse(validate_ip('999.999.999.999'))
        
    def test_scan_host_no_ports(self):
        from scanner import scan_host
        # Test with empty ports list
        result = scan_host('127.0.0.1', [])
        self.assertEqual(result['host'], '127.0.0.1')
        self.assertEqual(result['open_ports'], [])
        
    def test_scan_host_with_ports(self):
        from scanner import scan_host
        # Mock socket behavior for multiple ports
        with patch('socket.socket') as mock_socket:
            mock_conn = MagicMock()
            mock_socket.return_value = mock_conn
            mock_conn.connect_ex.side_effect = [0, 1]  # First port open, second closed
            
            result = scan_host('127.0.0.1', [80, 443])
            self.assertEqual(result['host'], '127.0.0.1')
            self.assertIn(80, result['open_ports'])
            self.assertNotIn(443, result['open_ports'])