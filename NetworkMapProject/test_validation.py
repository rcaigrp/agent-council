import sys
import os

def test_import():
    try:
        import network_scanner
        print("SUCCESS: network_scanner imported successfully")
        return True
    except ImportError as e:
        print(f"FAILED: Could not import network_scanner: {e}")
        return False

def test_functions_exist():
    try:
        import network_scanner
        functions = ['scan_port', 'resolve_host', 'scan_network']
        for func in functions:
            if not hasattr(network_scanner, func):
                print(f"FAILED: Function {func} not found in network_scanner")
                return False
        print("SUCCESS: All required functions found")
        return True
    except Exception as e:
        print(f"FAILED: Error checking functions: {e}")
        return False

def main():
    success = True
    success &= test_import()
    success &= test_functions_exist()
    
    if success:
        print("ALL TESTS PASSED")
        sys.exit(0)
    else:
        print("SOME TESTS FAILED")
        sys.exit(1)

if __name__ == '__main__':
    main()