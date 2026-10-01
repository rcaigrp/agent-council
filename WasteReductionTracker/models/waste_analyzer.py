from models.waste_category import WasteCategory
from collections import defaultdict
class WasteAnalyzer:
    def __init__(self):
        self.category_totals = defaultdict(int)

    def analyze_waste_data(self, waste_items):
        """Analyze waste items and return category breakdown and insights."""
        self.category_totals.clear()
        
        for item in waste_items:
            self.category_totals[item.category] += item.quantity
        
        return {
            'category_breakdown': dict(self.category_totals),
            'total_waste': sum(self.category_totals.values()),
            'most_common_category': max(self.category_totals.items(), key=lambda x: x[1])[0].value if self.category_totals else None
        }

    def get_recommendations(self, waste_analysis):
        """Generate personalized recommendations based on waste analysis."""
        recommendations = []
        
        if waste_analysis['total_waste'] > 10:
            recommendations.append("Consider reducing overall consumption to decrease waste.")
        
        if waste_analysis['most_common_category'] == WasteCategory.PLASTIC.value:
            recommendations.append("Try using reusable containers instead of single-use plastics.")
        
        if waste_analysis['most_common_category'] == WasteCategory.PAPER.value:
            recommendations.append("Consider digital alternatives to paper when possible.")
        
        if waste_analysis['most_common_category'] == WasteCategory.ORGANIC.value:
            recommendations.append("Start composting organic waste to reduce landfill contribution.")
        
        return recommendations