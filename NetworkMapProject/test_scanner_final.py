import sys
import os
import unittest

class TestNetworkScanner(unittest.TestCase):
    
    def test_import(self):
        # Simple test to verify the module can be imported
        try:
            import network_scanner
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import network_scanner: {e}")
    
    def test_structure(self):
        # Verify required functions exist
        import network_scanner
        self.assertTrue(hasattr(network_scanner, 'scan_port'))
        self.assertTrue(hasattr(network_scanner, 'resolve_host'))
        self.assertTrue(hasattr(network_scanner, 'scan_network'))
        
if __name__ == '__main__':
    unittest.main()