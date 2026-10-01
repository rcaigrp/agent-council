import pandas as pd
from collections import Counter

def generate_recommendations(waste_data):
    # Convert to DataFrame if it's a dict
    if isinstance(waste_data, dict):
        waste_data = pd.DataFrame(waste_data)
    
    # Get top categories by amount
    category_totals = waste_data.groupby('category')['amount'].sum()
    top_categories = category_totals.nlargest(3).index.tolist()
    
    recommendations = []
    for category in top_categories:
        if category == 'plastic':
            recommendations.append('Consider switching to reusable containers instead of single-use plastic')
        elif category == 'paper':
            recommendations.append('Try recycling more paper products or using digital alternatives')
        elif category == 'glass':
            recommendations.append('Reuse glass jars for storage instead of buying new ones')
        else:
            recommendations.append(f'Reduce consumption of {category} items')
    
    return recommendations