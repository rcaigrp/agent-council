import json
class WasteRecommender:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        
    def get_recommendations(self):
        analysis = self.analyzer.analyze_patterns()
        
        if not analysis.get('total_waste', 0):
            return ['No waste data available. Start tracking your waste to get personalized tips.']
        
        recommendations = []
        categories = analysis.get('categories', {})
        
        # Simple recommendation logic
        if categories.get('plastic', 0) > 5:
            recommendations.append('Reduce plastic usage by switching to reusable bags and containers')
        
        if categories.get('food_waste', 0) > 3:
            recommendations.append('Plan meals better to reduce food waste, compost organic scraps')
        
        if not recommendations:
            recommendations.append('Great job! Keep up the good work on waste reduction.')
            
        return recommendations