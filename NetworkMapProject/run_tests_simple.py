import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

test_file = 'test_scanner_final.py'
try:
    with open(test_file, 'r') as f:
        exec(f.read())
    print('Tests executed successfully')
except Exception as e:
    print(f'Test execution failed: {e}')
    sys.exit(1)