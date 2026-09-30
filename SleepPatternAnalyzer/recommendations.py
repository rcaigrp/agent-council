import json

class RecommendationEngine:
    def __init__(self):
        # Load recommendation rules
        self.rules = {
            'duration': {
                '<6': 'Sleep for at least 6 hours to improve recovery',
                '>=6': 'Good sleep duration'
            },
            'movement': {
                '>2.0': 'Reduce screen time before bed to minimize movement',
                '<=2.0': 'Your movement patterns are healthy'
            }
        }
    
    def get_recommendations(self, metrics):
        recommendations = []
        
        # Duration recommendation
        if metrics['sleep_duration'] < 6:
            recommendations.append(self.rules['duration']['<6'])
        else:
            recommendations.append(self.rules['duration']['>=6'])
        
        # Movement recommendation
        if metrics['movement_score'] > 2.0:
            recommendations.append(self.rules['movement']['>2.0'])
        else:
            recommendations.append(self.rules['movement']['<=2.0'])
        
        return recommendations
    
    def save_recommendations(self, recommendations, filename='recommendations.json'):
        with open(filename, 'w') as f:
            json.dump(recommendations, f)