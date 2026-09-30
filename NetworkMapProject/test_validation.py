#!/usr/bin/env python3
import subprocess
import sys

def test_import():
    try:
        import network_scanner
        print("SUCCESS: network_scanner imported successfully")
        return True
    except ImportError as e:
        print(f"FAILED: Could not import network_scanner: {e}")
        return False

def test_help():
    try:
        result = subprocess.run([sys.executable, 'network_scanner.py', '--help'], 
                               capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("SUCCESS: Help command works")
            return True
        else:
            print(f"FAILED: Help command failed with code {result.returncode}")
            return False
    except Exception as e:
        print(f"FAILED: Help command error: {e}")
        return False

def test_functionality():
    # Test basic argument parsing and validation
    try:
        import network_scanner
        import argparse
        
        # Test that the module has expected functions
        if hasattr(network_scanner, 'validate_port'):
            print("SUCCESS: validate_port function exists")
        else:
            print("FAILED: validate_port function missing")
            return False
        
        if hasattr(network_scanner, 'scan_port'):
            print("SUCCESS: scan_port function exists")
        else:
            print("FAILED: scan_port function missing")
            return False
        
        if hasattr(network_scanner, 'scan_host'):
            print("SUCCESS: scan_host function exists")
        else:
            print("FAILED: scan_host function missing")
            return False
        
        print("SUCCESS: Core functions are present")
        return True
    except Exception as e:
        print(f"FAILED: Function validation error: {e}")
        return False

def main():
    print("Running validation tests for network_scanner...")
    
    success = True
    success &= test_import()
    success &= test_help()
    success &= test_functionality()
    
    if success:
        print("\nALL TESTS PASSED")
        return 0
    else:
        print("\nSOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())