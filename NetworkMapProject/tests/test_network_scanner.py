import unittest
from network_scanner import scan_ip

class TestNetworkScanner(unittest.TestCase):

    def test_valid_ip_address(self):
        self.assertTrue(scan_ip("192.168.1.1"))
        self.assertTrue(scan_ip("8.8.8.8"))
        self.assertTrue(scan_ip("127.0.0.1:80"))

    def test_invalid_ip_address(self):
        self.assertFalse(scan_ip("invalid_ip"))
        self.assertFalse(scan_ip("192.168.1.1.1"))

if __name__ == '__main__':
    unittest.main()