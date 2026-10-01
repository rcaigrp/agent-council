import random

class RecommendationEngine:
    def __init__(self):
        self.tips = {
            "plastic": [
                "Use reusable water bottles instead of single-use plastic ones.",
                "Choose products with minimal plastic packaging.",
                "Bring your own shopping bags to reduce plastic bag usage."
            ],
            "paper": [
                "Recycle paper items properly and separate them from other waste.",
                "Use both sides of the paper when possible to reduce consumption.",
                "Opt for digital receipts instead of paper ones."
            ],
            "organic": [
                "Compost food scraps at home to reduce organic waste.",
                "Use biodegradable bags for collecting organic waste.",
                "Plan meals to reduce food waste."
            ],
            "metal": [
                "Recycle metal cans and containers properly.",
                "Choose products with recyclable metal packaging.",
                "Donate usable metal items instead of throwing them away."
            ],
            "other": [
                "Research local recycling centers for proper disposal of special items.",
                "Consider repair or reuse before discarding items.",
                "Donate unwanted items to charities or community groups."
            ]
        }

    def generate_recommendations(self, waste_data):
        """Generate personalized recommendations based on waste data"""
        # Simple logic: recommend based on highest category count
        if not waste_data:
            return ["Start tracking your waste to get personalized tips."]

        # Count items by category
        category_counts = {}
        for item in waste_data:
            category = item.get("category", "other")
            category_counts[category] = category_counts.get(category, 0) + 1

        # Find the most common category
        max_category = max(category_counts, key=category_counts.get)
        
        # Get recommendations for that category
        recommendations = self.tips.get(max_category, [])
        
        # If no specific recommendations, provide a general tip
        if not recommendations:
            return ["Keep tracking your waste to get more personalized tips."]
        
        # Return 2-3 random tips from that category
        return random.sample(recommendations, min(3, len(recommendations)))