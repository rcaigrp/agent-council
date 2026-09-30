import time
import random
class SleepDataCollector:
    def __init__(self):
        self.data_buffer = []
    
    def collect_sensor_data(self):
        # Simulate collecting data from smartphone sensors
        timestamp = time.time()
        accelerometer_data = {
            'x': random.uniform(-1, 1),
            'y': random.uniform(-1, 1),
            'z': random.uniform(-1, 1)
        }
        gyroscope_data = {
            'x': random.uniform(-0.5, 0.5),
            'y': random.uniform(-0.5, 0.5),
            'z': random.uniform(-0.5, 0.5)
        }
        heart_rate = random.randint(60, 100)
        
        sensor_data = {
            'timestamp': timestamp,
            'accelerometer': accelerometer_data,
            'gyroscope': gyroscope_data,
            'heart_rate': heart_rate
        }
        
        self.data_buffer.append(sensor_data)
        return sensor_data
    
    def get_collected_data(self):
        return self.data_buffer