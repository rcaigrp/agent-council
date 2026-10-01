import pytest
from models.waste_analyzer import WasteAnalyzer

def test_categorize_waste():
    analyzer = WasteAnalyzer()
    waste_items = [
        {'name': 'plastic bag', 'category': 'plastic'},
        {'name': 'newspaper', 'category': 'paper'},
        {'name': 'glass bottle', 'category': 'glass'}
    ]
    
    result = analyzer.categorize_waste(waste_items)
    assert 'plastic' in result
    assert 'paper' in result
    assert 'glass' in result


def test_analyze_patterns():
    analyzer = WasteAnalyzer()
    waste_data = [
        {'name': 'plastic bag', 'category': 'plastic'},
        {'name': 'plastic bottle', 'category': 'plastic'},
        {'name': 'newspaper', 'category': 'paper'}
    ]
    
    result = analyzer.analyze_patterns(waste_data)
    assert 'category_distribution' in result
    assert 'most_common_items' in result
    assert result['total_waste_items'] == 3
