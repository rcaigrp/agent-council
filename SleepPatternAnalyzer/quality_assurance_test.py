import subprocess
import sys

def run_final_tests():
    """Run all final tests to validate project completeness"""
    # Test sensor data collector
    result1 = subprocess.run([sys.executable, "test_sensor_data_collector.py"], 
                           cwd="/workspace/projects/SleepPatternAnalyzer", 
                           capture_output=True, text=True)
    
    # Test data analyzer
    result2 = subprocess.run([sys.executable, "test_data_analyzer.py"], 
                           cwd="/workspace/projects/SleepPatternAnalyzer", 
                           capture_output=True, text=True)
    
    # Test recommendation engine
    result3 = subprocess.run([sys.executable, "test_recommendation_engine.py"], 
                           cwd="/workspace/projects/SleepPatternAnalyzer", 
                           capture_output=True, text=True)
    
    return [result1, result2, result3]

if __name__ == "__main__":
    results = run_final_tests()
    for i, result in enumerate(results):
        if result.returncode == 0:
            print(f"Test {i+1} PASSED")
        else:
            print(f"Test {i+1} FAILED")
            print(result.stderr)
