from enum import Enum
class WasteCategory(Enum):
    PLASTIC = "plastic"
    PAPER = "paper"
    ORGANIC = "organic"
    METAL = "metal"
    OTHER = "other"

class WasteAnalyzer:
    @staticmethod
    def categorize_waste(waste_type: str) -> WasteCategory:
        category_map = {
            'plastic': WasteCategory.PLASTIC,
            'paper': WasteCategory.PAPER,
            'organic': WasteCategory.ORGANIC,
            'metal': WasteCategory.METAL,
            'other': WasteCategory.OTHER
        }
        return category_map.get(waste_type.lower(), WasteCategory.OTHER)

    @staticmethod
    def analyze_patterns(waste_data):
        categories = {}
        for item in waste_data:
            category = WasteAnalyzer.categorize_waste(item['type'])
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
        return categories