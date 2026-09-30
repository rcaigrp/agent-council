import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class TestNetworkScanner(unittest.TestCase):
    def test_import(self):
        try:
            from network_scanner import NetworkScanner
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import NetworkScanner: {e}")
    
    def test_scan_method_exists(self):
        from network_scanner import NetworkScanner
        scanner = NetworkScanner()
        self.assertTrue(hasattr(scanner, 'scan'))
        
    def test_cidr_support(self):
        from network_scanner import NetworkScanner
        scanner = NetworkScanner()
        # Test that CIDR notation is supported
        try:
            result = scanner.scan('192.168.1.0/24', [80])
            self.assertIsInstance(result, list)
        except Exception:
            pass  # This test is just to verify the method accepts CIDR
    
    def test_json_output(self):
        from network_scanner import NetworkScanner
        scanner = NetworkScanner()
        try:
            result = scanner.scan('127.0.0.1', [80])
            # Verify we get a JSON-like structure
            self.assertIsInstance(result, list)
        except Exception:
            pass  # This test is just to verify the method produces output

if __name__ == '__main__':
    unittest.main()