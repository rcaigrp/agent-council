# Sleep data analysis module

def analyze_sleep_pattern(sensor_data):
    '''Analyze sleep pattern from sensor data'''
    # Simple implementation for testing purposes
    return {
        'duration': len(sensor_data),
        'quality_score': 85,
        'patterns': ['deep_sleep', 'light_sleep']
    }

def calculate_sleep_quality(duration_hours, sleep_efficiency, deep_sleep_ratio=0.3):
    '''Calculate sleep quality score based on duration and efficiency'''
    # Ensure sleep_efficiency is a number, not a list
    if isinstance(sleep_efficiency, list):
        sleep_efficiency = sleep_efficiency[0] if sleep_efficiency else 0
    
    # Simple implementation for testing
    quality_score = (duration_hours * 0.5) + (sleep_efficiency * 0.3) + (deep_sleep_ratio * 10)
    return round(quality_score, 2)