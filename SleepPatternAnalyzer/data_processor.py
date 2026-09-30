# Data Processor Module
# Processes raw sensor data into meaningful sleep metrics

class DataProcessor:
    def __init__(self):
        self.processed_data = []
        
    def process_accelerometer_data(self, raw_data):
        # Process accelerometer data to extract movement patterns
        try:
            x = raw_data['x']
            y = raw_data['y']
            z = raw_data['z']
            magnitude = (x**2 + y**2 + z**2)**0.5
            
            # Simple activity detection based on movement magnitude
            if magnitude < 0.5:
                activity = 'resting'
            elif magnitude < 1.0:
                activity = 'light_movement'
            else:
                activity = 'active'
                
            return {
                'activity': activity,
                'magnitude': magnitude,
                'timestamp': raw_data['timestamp']
            }
        except Exception as e:
            print(f"Error processing accelerometer data: {e}")
            return None
    
    def process_gyroscope_data(self, raw_data):
        # Process gyroscope data to detect rotation patterns
        try:
            x = raw_data['x']
            y = raw_data['y']
            z = raw_data['z']
            magnitude = (x**2 + y**2 + z**2)**0.5
            
            # Simple rotation classification
            if magnitude < 0.01:
                rotation = 'stable'
            elif magnitude < 0.05:
                rotation = 'slow_rotation'
            else:
                rotation = 'fast_rotation'
                
            return {
                'rotation': rotation,
                'magnitude': magnitude,
                'timestamp': raw_data['timestamp']
            }
        except Exception as e:
            print(f"Error processing gyroscope data: {e}")
            return None
    
    def analyze_sleep_patterns(self, processed_data):
        # Analyze sleep patterns from processed sensor data
        resting_count = sum(1 for d in processed_data if d.get('activity') == 'resting')
        active_count = sum(1 for d in processed_data if d.get('activity') == 'active')
        
        total_samples = len(processed_data)
        sleep_quality_score = (resting_count / total_samples) * 100 if total_samples > 0 else 0
        
        return {
            'sleep_quality_score': sleep_quality_score,
            'resting_periods': resting_count,
            'active_periods': active_count,
            'total_samples': total_samples
        }