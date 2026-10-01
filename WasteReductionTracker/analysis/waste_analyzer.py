from collections import defaultdict
from models.waste_item import WasteItem, WasteCategory

class WasteAnalyzer:
    @staticmethod
    def analyze_by_category(waste_items):
        category_totals = defaultdict(float)
        for item in waste_items:
            category_totals[item.category] += item.weight
        return dict(category_totals)

    @staticmethod
    def get_top_categories(waste_items, top_n=3):
        category_totals = WasteAnalyzer.analyze_by_category(waste_items)
        sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
        return sorted_categories[:top_n]

    @staticmethod
    def get_waste_trend(waste_items):
        # Simplified trend analysis - would be more complex in full implementation
        if not waste_items:
            return "No data"
        
        total_weight = sum(item.weight for item in waste_items)
        return f"Total: {total_weight:.2f}kg"

    @staticmethod
    def get_recommendations(waste_items):
        top_categories = WasteAnalyzer.get_top_categories(waste_items)
        recommendations = []
        
        for category, weight in top_categories:
            if category == WasteCategory.ORGANIC:
                recommendations.append("Try composting organic waste instead of sending it to landfill.")
            elif category == WasteCategory.RECYCLABLE:
                recommendations.append("Ensure recyclable items are properly sorted and clean before recycling.")
            elif category == WasteCategory.LANDFILL:
                recommendations.append("Consider reducing the amount of non-recyclable waste by choosing reusable alternatives.")
            elif category == WasteCategory.HAZARDOUS:
                recommendations.append("Hazards items should be taken to special collection points, not regular trash.")
        
        return recommendations