"""Test file for Sleep Pattern Analyzer application"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Test that our app can be imported without errors
try:
    from main import SleepPatternAnalyzerApp
    print("SUCCESS: App imports correctly")
    
    # Test sensor data collection
    from sensor_data_collector import get_sensor_data
    data = get_sensor_data()
    print(f"SUCCESS: Sensor data collected - Accel: {data['accel']}, Gyro: {data['gyro']}")
    
    # Test app creation
    app = SleepPatternAnalyzerApp()
    print("SUCCESS: App instance created")
    
except Exception as e:
    print(f"FAILED: {str(e)}")
    sys.exit(1)