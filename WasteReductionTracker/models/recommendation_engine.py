import pandas as pd
class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'plastic': ['Use reusable water bottles', 'Carry cloth bags'],
            'paper': ['Go paperless when possible', 'Recycle old newspapers'],
            'organic': ['Compost food scraps', 'Use biodegradable products'],
            'metal': ['Avoid single-use cans', 'Donate usable items'],
            'other': ['Repair instead of replace', 'Buy second-hand']
        }
    
    def generate_recommendations(self, waste_data):
        # Simple categorization-based recommendations
        if isinstance(waste_data, dict):
            waste_data = pd.DataFrame(waste_data)
        categories = list(waste_data['category'].value_counts().index)
        suggestions = []
        for category in categories:
            if category in self.recommendations:
                suggestions.extend(self.recommendations[category])
        return list(set(suggestions))  # Remove duplicates