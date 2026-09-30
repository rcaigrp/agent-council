# Sleep Pattern Analyzer - Main Application
import time
import json
from datetime import datetime

class SleepDataCollector:
    def __init__(self):
        self.data = []
        
    def collect_accelerometer_data(self):
        # Simulate accelerometer data collection
        return {
            'timestamp': time.time(),
            'x': 0.1,
            'y': 0.2,
            'z': 0.9
        }
        
    def collect_gyroscope_data(self):
        # Simulate gyroscope data collection
        return {
            'timestamp': time.time(),
            'x': 0.01,
            'y': 0.02,
            'z': 0.03
        }
        
    def collect_microphone_data(self):
        # Simulate microphone data collection (noise levels)
        return {
            'timestamp': time.time(),
            'noise_level': 45.2
        }
        
    def collect_all_data(self):
        data_point = {
            'timestamp': datetime.now().isoformat(),
            'accelerometer': self.collect_accelerometer_data(),
            'gyroscope': self.collect_gyroscope_data(),
            'microphone': self.collect_microphone_data()
        }
        self.data.append(data_point)
        return data_point

if __name__ == "__main__":
    collector = SleepDataCollector()
    print("Sleep Data Collector initialized")
    sample_data = collector.collect_all_data()
    print(f"Collected sample data: {json.dumps(sample_data, indent=2)}")