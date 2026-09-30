import pandas as pd
class SleepRecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'duration_short': 'Try to extend your sleep by 15-30 minutes each night to improve recovery.',
            'low_efficiency': 'Improve sleep efficiency by minimizing nighttime awakenings and maintaining a consistent bedtime routine.',
            'long_latency': 'Reduce sleep onset latency by avoiding screens 1 hour before bed and creating a calming pre-sleep ritual.',
            'inconsistent_schedule': 'Maintain a fixed sleep schedule even on weekends for better circadian rhythm regulation.',
            'optimal': 'Your sleep patterns are excellent! Keep up the good work with your current routine.'
        }
    
    def generate_recommendations(self, sleep_data):
        recommendations = []
        if sleep_data['sleep_duration'] < 7:
            recommendations.append(self.recommendations['duration_short'])
        if sleep_data['sleep_efficiency'] < 85:
            recommendations.append(self.recommendations['low_efficiency'])
        if sleep_data['sleep_latency'] > 30:
            recommendations.append(self.recommendations['long_latency'])
        if sleep_data['schedule_consistency'] < 80:
            recommendations.append(self.recommendations['inconsistent_schedule'])
        
        return recommendations if recommendations else [self.recommendations['optimal']]

# Example usage
if __name__ == '__main__':
    engine = SleepRecommendationEngine()
    sample_data = {
        'sleep_duration': 6.5,
        'sleep_efficiency': 80,
        'sleep_latency': 45,
        'schedule_consistency': 75
    }
    print('Recommendations:', engine.generate_recommendations(sample_data))