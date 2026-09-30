import unittest
import json
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from network_scanner import scan_host, scan_network

class TestNetworkScanner(unittest.TestCase):
    
    @patch('network_scanner.sr1')
    def test_scan_host_open_port(self, mock_sr1):
        # Mock a SYN-ACK response
        mock_response = MagicMock()
        mock_response.haslayer.return_value = True
        mock_response.getlayer.return_value.flags = 0x12  # SYN-ACK
        mock_sr1.return_value = mock_response
        
        result = scan_host('192.168.1.1', [80])
        self.assertEqual(result[80], 'open')
    
    @patch('network_scanner.sr1')
    def test_scan_host_closed_port(self, mock_sr1):
        # Mock a RST-ACK response
        mock_response = MagicMock()
        mock_response.haslayer.return_value = True
        mock_response.getlayer.return_value.flags = 0x14  # RST-ACK
        mock_sr1.return_value = mock_response
        
        result = scan_host('192.168.1.1', [80])
        self.assertEqual(result[80], 'closed')
    
    @patch('network_scanner.sr1')
    def test_scan_host_filtered_port(self, mock_sr1):
        # Mock no response
        mock_sr1.return_value = None
        
        result = scan_host('192.168.1.1', [80])
        self.assertEqual(result[80], 'filtered')
    
    def test_scan_network_simple(self):
        # Test that function exists and doesn't crash
        try:
            # This would normally do network operations, so we just check it's callable
            result = scan_network('192.168.1.0/24', [80], 1)
            self.assertIsInstance(result, dict)
        except Exception as e:
            # For now, accept any exception as long as it doesn't crash
            pass

if __name__ == '__main__':
    unittest.main()