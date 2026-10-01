# Sensor data collector module

class SensorDataCollector:
    def __init__(self):
        self.data = []

    def collect_data(self):
        # Simulate collecting sensor data
        return [1, 2, 3, 4, 5]

    def process_data(self, raw_data):
        # Process the raw sensor data
        return [x * 2 for x in raw_data]