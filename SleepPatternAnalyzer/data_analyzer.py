def analyze_sleep_pattern(sleep_data):
    '''Analyze sleep pattern from sensor data'''
    if not sleep_data:
        return None
    
    # Simple analysis: calculate average duration and standard deviation
    avg_duration = sum(sleep_data) / len(sleep_data)
    variance = sum((x - avg_duration) ** 2 for x in sleep_data) / len(sleep_data)
    std_deviation = variance ** 0.5
    
    return {
        'average_duration': avg_duration,
        'std_deviation': std_deviation,
        'total_nights': len(sleep_data)
    }

def calculate_sleep_quality(duration, deep_sleep, sleep_efficiency):
    '''Calculate overall sleep quality score'''
    # Simple weighted calculation
    quality = (duration * 0.3) + (deep_sleep * 0.4) + (sleep_efficiency * 0.3)
    return min(quality, 10.0)  # Cap at 10