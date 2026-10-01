import json
class WasteAnalyzer:
    def __init__(self, data_collector):
        self.data_collector = data_collector
        
    def analyze_patterns(self):
        data = self.data_collector.get_all_data()
        if not data:
            return {}
        
        # Simple pattern analysis
        total_waste = sum(item['quantity'] for item in data)
        
        # Categorize by type
        categories = {}
        for item in data:
            category = item['item_type']
            if category not in categories:
                categories[category] = 0
            categories[category] += item['quantity']
        
        return {
            'total_waste': total_waste,
            'categories': categories
        }