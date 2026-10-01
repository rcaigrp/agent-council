def analyze_sleep_data(sleep_data):
    '''Analyze sleep data to calculate quality metrics'''
    # Simple mock implementation
    if not sleep_data:
        return {'sleep_duration': 0, 'restlessness_index': 0}
    
    # Calculate duration (difference between last and first timestamp)
    duration = sleep_data[-1]['timestamp'] - sleep_data[0]['timestamp']
    
    # Calculate restlessness index (average acceleration)
    total_acceleration = sum(point['acceleration'] for point in sleep_data)
    restlessness_index = total_acceleration / len(sleep_data) if sleep_data else 0
    
    return {
        'sleep_duration': duration,
        'restlessness_index': restlessness_index,
        'sleep_quality': 'good' if restlessness_index < 0.5 else 'poor'
    }