from collections import defaultdict, Counter
from datetime import datetime, timedelta

class WasteAnalyzer:
    def __init__(self):
        # Predefined waste categories and their keywords
        self.categories = {
            'plastic': ['plastic', 'polyethylene', 'polypropylene'],
            'paper': ['paper', 'cardboard', 'newsprint'],
            'glass': ['glass', 'bottle', 'jar'],
            'metal': ['metal', 'aluminum', 'steel'],
            'organic': ['food', 'compost', 'biodegradable'],
            'electronic': ['phone', 'laptop', 'battery', 'electronics']
        }

    def categorize_waste(self, item_description):
        """
        Categorizes a waste item based on keywords in its description
        """
        item_lower = item_description.lower()
        for category, keywords in self.categories.items():
            if any(keyword in item_lower for keyword in keywords):
                return category
        return 'other'

    def analyze_patterns(self, waste_data):
        """
        Analyze waste data to identify patterns and trends
        
        Args:
            waste_data: List of waste items with timestamps
        
        Returns:
            Dictionary containing analysis results
        """
        if not waste_data:
            return {}
        
        # Group by category
        category_counts = Counter(item['category'] for item in waste_data)
        
        # Calculate daily averages
        dates = [item['timestamp'].date() for item in waste_data]
        daily_counts = defaultdict(int)
        for date in dates:
            daily_counts[date] += 1
        
        # Most common categories
        most_common = category_counts.most_common(3)
        
        # Trend analysis (last 7 days)
        recent_dates = [d for d in dates if d >= datetime.now().date() - timedelta(days=7)]
        recent_counts = Counter(recent_dates)
        
        trend = 'stable'
        if len(recent_counts) >= 2:
            values = list(recent_counts.values())
            if values[-1] > values[0]:
                trend = 'increasing'
            elif values[-1] < values[0]:
                trend = 'decreasing'
        
        return {
            'category_breakdown': dict(category_counts),
            'most_common_categories': most_common,
            'daily_average': sum(daily_counts.values()) / len(daily_counts) if daily_counts else 0,
            'trend': trend
        }