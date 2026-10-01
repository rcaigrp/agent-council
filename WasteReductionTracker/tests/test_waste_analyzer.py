import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../')

import pytest
from models.waste_analyzer import WasteAnalyzer

def test_categorize_waste():
    analyzer = WasteAnalyzer()
    
    # Test plastic items
    assert analyzer.categorize_waste('plastic water bottle') == 'plastic'
    assert analyzer.categorize_waste('polyethylene bag') == 'plastic'
    
    # Test paper items
    assert analyzer.categorize_waste('newspaper') == 'paper'
    assert analyzer.categorize_waste('cardboard box') == 'paper'
    
    # Test glass items
    assert analyzer.categorize_waste('glass jar') == 'glass'
    assert analyzer.categorize_waste('wine bottle') == 'glass'
    
    # Test organic items
    assert analyzer.categorize_waste('food scraps') == 'organic'
    assert analyzer.categorize_waste('compostable plate') == 'organic'
    
    # Test other items
    assert analyzer.categorize_waste('wooden chair') == 'other'
    assert analyzer.categorize_waste('metal screw') == 'metal'
    

def test_analyze_patterns():
    analyzer = WasteAnalyzer()
    
    # Test with sample data
    sample_data = [
        {'item': 'plastic bottle', 'category': 'plastic', 'timestamp': '2023-05-01 10:00:00'},
        {'item': 'paper bag', 'category': 'paper', 'timestamp': '2023-05-01 11:00:00'},
        {'item': 'plastic bottle', 'category': 'plastic', 'timestamp': '2023-05-02 12:00:00'}
    ]
    
    # Convert timestamps to datetime objects
    for item in sample_data:
        item['timestamp'] = datetime.strptime(item['timestamp'], '%Y-%m-%d %H:%M:%S')
    
    result = analyzer.analyze_patterns(sample_data)
    assert 'category_breakdown' in result
    assert 'most_common_categories' in result
    assert 'daily_average' in result
    assert 'trend' in result