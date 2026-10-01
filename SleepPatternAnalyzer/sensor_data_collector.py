import random

def collect_sleep_data():
    '''Simulate collecting sleep data from smartphone sensors'''
    # In a real app, this would interface with device sensors
    # For demo purposes, we'll generate mock data
    sleep_durations = []
    for i in range(5):  # Simulate 5 days of data
        duration = random.uniform(4, 10)  # Random sleep duration between 4-10 hours
        sleep_durations.append(round(duration, 1))
    
    return sleep_durations