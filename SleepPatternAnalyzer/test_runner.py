import sys
import os
import subprocess

def run_tests():
    # Install pytest first
    result = subprocess.run([sys.executable, '-m', 'pip', 'install', 'pytest'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f'Error installing pytest: {result.stderr}')
        return False
    
    # Run the tests
    test_files = ['test_data_analyzer.py', 'test_recommendation_engine.py']
    for test_file in test_files:
        if os.path.exists(test_file):
            result = subprocess.run([sys.executable, '-m', 'pytest', test_file, '-v'], capture_output=True, text=True)
            if result.returncode != 0:
                print(f'Test failed for {test_file}: {result.stderr}')
                return False
            else:
                print(f'{test_file} passed successfully')
    
    print('All tests passed!')
    return True

if __name__ == '__main__':
    run_tests()