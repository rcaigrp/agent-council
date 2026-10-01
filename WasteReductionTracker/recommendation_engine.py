# Waste Reduction Tracker - Recommendation Engine

class RecommendationEngine:
    def __init__(self):
        self.recommendations = [
            "Use reusable bags instead of plastic ones",
            "Choose products with minimal packaging",
            "Compost organic waste",
            "Recycle paper and cardboard properly"
        ]

    def generate_recommendations(self, waste_data=None):
        # Handle empty or None input gracefully
        if not waste_data:
            return ["Start by tracking your daily waste items to get personalized tips"]
        
        # Simple logic for demonstration
        if len(waste_data) > 5:
            return ["You're generating a lot of waste! Try reducing single-use items."]
        elif len(waste_data) > 2:
            return ["Good progress on waste reduction!", "Consider composting organic waste."]
        else:
            return ["Great job! Keep up the sustainable habits."]

    def get_recommendations_for_category(self, category):
        # Return recommendations based on waste category
        if category == "plastic":
            return ["Switch to glass or stainless steel containers"]
        elif category == "paper":
            return ["Recycle paper properly and reduce consumption"]
        else:
            return ["Try to minimize this type of waste"]