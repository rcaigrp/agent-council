"""Module for collecting sensor data from smartphone sensors"""

import random
import time

class SensorDataCollector:
    def __init__(self):
        self.accelerometer_data = []
        self.gyroscope_data = []
        
    def get_sensor_data(self):
        """Simulate getting sensor data from device"""
        # In a real implementation, this would interface with actual sensors
        # For now, we simulate data collection
        
        # Simulate accelerometer data (x, y, z)
        accel_data = [
            random.uniform(-10.0, 10.0),
            random.uniform(-10.0, 10.0),
            random.uniform(-10.0, 10.0)
        ]
        
        # Simulate gyroscope data (x, y, z)
        gyro_data = [
            random.uniform(-100.0, 100.0),
            random.uniform(-100.0, 100.0),
            random.uniform(-100.0, 100.0)
        ]
        
        return {
            'accel': accel_data,
            'gyro': gyro_data,
            'timestamp': time.time()
        }

# Create global instance
sensor_collector = SensorDataCollector()

def get_sensor_data():
    return sensor_collector.get_sensor_data()