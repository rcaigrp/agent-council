import subprocess
import sys

# Run all test files
result1 = subprocess.run([sys.executable, 'test_sensor_data_collector.py'], cwd='/workspace/projects/SleepPatternAnalyzer', capture_output=True, text=True)
print('Sensor Data Collector Test:', result1.stdout)
if result1.stderr:
    print('Sensor Data Collector Errors:', result1.stderr)

result2 = subprocess.run([sys.executable, 'test_data_analyzer.py'], cwd='/workspace/projects/SleepPatternAnalyzer', capture_output=True, text=True)
print('Data Analyzer Test:', result2.stdout)
if result2.stderr:
    print('Data Analyzer Errors:', result2.stderr)

result3 = subprocess.run([sys.executable, 'test_recommendation_engine.py'], cwd='/workspace/projects/SleepPatternAnalyzer', capture_output=True, text=True)
print('Recommendation Engine Test:', result3.stdout)
if result3.stderr:
    print('Recommendation Engine Errors:', result3.stderr)