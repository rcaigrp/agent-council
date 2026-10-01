from collections import defaultdict
class WasteAnalysis:
    def __init__(self):
        self.category_totals = defaultdict(int)
        
    def analyze_waste_pattern(self, waste_items):
        """Analyze waste items to identify patterns and trends"""
        for item in waste_items:
            self.category_totals[item.category] += 1
        return dict(self.category_totals)
        
    def get_top_categories(self, limit=3):
        """Get the top waste categories by frequency"""
        sorted_categories = sorted(self.category_totals.items(), key=lambda x: x[1], reverse=True)
        return sorted_categories[:limit]