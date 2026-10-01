from models.waste_item import WasteItem
from models.waste_category import WasteCategory

class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            WasteCategory.PLASTIC: [
                "Use reusable water bottles instead of single-use plastic ones.",
                "Choose products with minimal plastic packaging.",
                "Bring your own shopping bags to avoid plastic bags."
            ],
            WasteCategory.PAPER: [
                "Recycle paper products properly.",
                "Use digital alternatives when possible.",
                "Buy products made from recycled paper."
            ],
            WasteCategory.ORGANIC: [
                "Compost organic waste instead of throwing it away.",
                "Use biodegradable containers for food storage.",
                "Plan meals to reduce food waste."
            ],
            WasteCategory.METAL: [
                "Recycle metal cans and containers.",
                "Choose products with recyclable metal packaging.",
                "Buy second-hand items to reduce demand for new metals."
            ],
            WasteCategory.OTHER: [
                "Research proper disposal methods for unusual items.",
                "Donate usable items instead of throwing them away.",
                "Consider the environmental impact before purchasing new items."
            ]
        }

    def get_recommendations(self, waste_items):
        category_counts = {}
        total_items = 0
        
        for item in waste_items:
            category = item.category
            category_counts[category] = category_counts.get(category, 0) + item.quantity
            total_items += item.quantity
        
        # Find the category with highest count
        max_category = max(category_counts.items(), key=lambda x: x[1])[0] if category_counts else None
        
        recommendations = []
        if max_category:
            recommendations.extend(self.recommendations[max_category])
        
        # Add general tips based on total waste amount
        if total_items > 10:
            recommendations.append("Try to reduce overall consumption by planning purchases better.")
        elif total_items > 5:
            recommendations.append("Consider reusing items before discarding them.")
        
        return recommendations