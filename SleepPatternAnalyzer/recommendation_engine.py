import pandas as pd
class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'sleep_duration': [
                'Try to maintain consistent sleep schedule (7-9 hours for adults)',
                'Avoid long daytime naps that interfere with nighttime sleep'
            ],
            'restlessness': [
                'Create a calming bedtime routine to reduce mental stimulation',
                'Keep bedroom cool and well-ventilated'
            ],
            'sleep_quality': [
                'Limit screen time 1 hour before bed',
                'Avoid caffeine after 2 PM'
            ]
        }
    
    def generate_recommendations(self, sleep_data):
        recommendations = []
        
        # Analyze sleep duration
        if 'duration' in sleep_data:
            duration = sleep_data['duration']
            if duration < 6:
                recommendations.extend(self.recommendations['sleep_duration'])
            elif duration > 10:
                recommendations.append('Consider reducing nighttime sleep to avoid grogginess')
        
        # Analyze restlessness
        if 'restlessness_index' in sleep_data:
            restlessness = sleep_data['restlessness_index']
            if restlessness > 0.7:
                recommendations.extend(self.recommendations['restlessness'])
        
        # Analyze overall quality
        if 'quality_score' in sleep_data:
            quality = sleep_data['quality_score']
            if quality < 60:
                recommendations.extend(self.recommendations['sleep_quality'])
        
        return list(set(recommendations))  # Remove duplicates