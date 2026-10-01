from typing import List, Dict
from .waste_category import WasteCategory

class RecommendationEngine:
    def __init__(self):
        self.waste_category = WasteCategory()

    def generate_recommendations(self, waste_items: List[Dict]) -> List[str]:
        recommendations = []
        
        # Analyze waste pattern
        analysis = self.waste_category.analyze_waste_pattern(waste_items)
        
        # Get total weight by category
        total_by_category = analysis.get('total_waste_by_category', {})
        
        # Generate recommendations based on waste patterns
        if total_by_category:
            # Most common waste type
            most_common = analysis.get('most_common_waste_type')
            if most_common == 'plastic':
                recommendations.append("Consider switching to reusable containers instead of plastic packaging.")
            elif most_common == 'paper':
                recommendations.append("Try using digital alternatives when possible to reduce paper consumption.")
            elif most_common == 'organic':
                recommendations.append("Start composting organic waste at home to reduce landfill contribution.")
            elif most_common == 'metal':
                recommendations.append("Ensure all metal items are properly recycled through local programs.")
            
            # Overall recommendations
            total_waste = sum(total_by_category.values())
            if total_waste > 10:  # More than 10kg total waste
                recommendations.append("Your daily waste output is quite high. Consider reducing consumption and reusing items.")
            elif total_waste > 5:
                recommendations.append("You're doing well, but there's room for improvement in waste reduction.")
            else:
                recommendations.append("Great job! You're maintaining low daily waste output.")
        
        # Add generic tips
        recommendations.extend([
            "Try to separate recyclables from regular trash.",
            "Use reusable bags, bottles, and containers whenever possible.",
            "Consider donating items you no longer need instead of throwing them away."
        ])
        
        return recommendations[:5]  # Return top 5 recommendations