import numpy as np
from scipy import signal


class SensorDataProcessor:
    def __init__(self):
        self.sleep_patterns = []
        
    def process_accelerometer_data(self, data):
        # Convert to numpy array for easier processing
        x_values = np.array([point['x'] for point in data])
        y_values = np.array([point['y'] for point in data])
        z_values = np.array([point['z'] for point in data])
        
        # Calculate magnitude of acceleration
        magnitude = np.sqrt(x_values**2 + y_values**2 + z_values**2)
        
        # Apply low-pass filter to smooth the signal
        b, a = signal.butter(4, 0.2, btype='low')
        filtered_magnitude = signal.filtfilt(b, a, magnitude)
        
        return {
            'raw': data,
            'filtered': filtered_magnitude.tolist(),
            'mean_magnitude': np.mean(filtered_magnitude),
            'std_magnitude': np.std(filtered_magnitude)
        }
    
    def process_gyroscope_data(self, data):
        # Convert to numpy array for easier processing
        x_values = np.array([point['x'] for point in data])
        y_values = np.array([point['y'] for point in data])
        z_values = np.array([point['z'] for point in data])
        
        # Calculate magnitude of rotation
        magnitude = np.sqrt(x_values**2 + y_values**2 + z_values**2)
        
        # Apply low-pass filter to smooth the signal
        b, a = signal.butter(4, 0.2, btype='low')
        filtered_magnitude = signal.filtfilt(b, a, magnitude)
        
        return {
            'raw': data,
            'filtered': filtered_magnitude.tolist(),
            'mean_magnitude': np.mean(filtered_magnitude),
            'std_magnitude': np.std(filtered_magnitude)
        }
    
    def detect_sleep_pattern(self, accelerometer_data, gyroscope_data):
        # Simple pattern detection based on low movement
        acc_processed = self.process_accelerometer_data(accelerometer_data)
        gyro_processed = self.process_gyroscope_data(gyroscope_data)
        
        # If both have very low activity, consider it sleep
        if (acc_processed['mean_magnitude'] < 0.5 and 
            gyro_processed['mean_magnitude'] < 0.3):
            pattern = 'deep_sleep'
        elif (acc_processed['mean_magnitude'] < 1.0 and 
              gyro_processed['mean_magnitude'] < 0.5):
            pattern = 'light_sleep'
        else:
            pattern = 'awake'
        
        return {
            'pattern': pattern,
            'accelerometer': acc_processed,
            'gyroscope': gyro_processed
        }