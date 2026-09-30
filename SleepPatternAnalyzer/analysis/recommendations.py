import pandas as pd
class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'quality': {
                'high': ['Maintain current sleep schedule', 'Keep bedroom cool and dark'],
                'medium': ['Reduce screen time before bed', 'Avoid caffeine after 2 PM'],
                'low': ['Consider consulting a sleep specialist', 'Establish consistent bedtime routine']
            },
            'duration': {
                'short': ['Try to go to bed earlier', 'Limit daytime naps'],
                'adequate': ['Keep current schedule', 'Maintain regular sleep/wake times'],
                'long': ["Consider if you're oversleeping", "Evaluate sleep quality not just quantity"]
            }
        }
    
    def generate_recommendations(self, sleep_metrics):
        recommendations = []
        
        # Quality-based recommendations
        if sleep_metrics['quality_score'] >= 80:
            recommendations.extend(self.recommendations['quality']['high'])
        elif sleep_metrics['quality_score'] >= 60:
            recommendations.extend(self.recommendations['quality']['medium'])
        else:
            recommendations.extend(self.recommendations['quality']['low'])
        
        # Duration-based recommendations
        if sleep_metrics['duration_hours'] < 6:
            recommendations.extend(self.recommendations['duration']['short'])
        elif sleep_metrics['duration_hours'] > 9:
            recommendations.extend(self.recommendations['duration']['long'])
        else:
            recommendations.extend(self.recommendations['duration']['adequate'])
        
        return list(set(recommendations))  # Remove duplicates