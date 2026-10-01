import pytest
from models.waste_item import WasteItem
from models.waste_category import WasteCategory
from models.waste_analyzer import WasteAnalyzer

def test_waste_category_from_string():
    assert WasteCategory.from_string('plastic') == WasteCategory.PLASTIC
    assert WasteCategory.from_string('unknown') == WasteCategory.OTHER

def test_waste_item_creation():
    item = WasteItem('Plastic Bottle', 'plastic', 2)
    assert item.name == 'Plastic Bottle'
    assert item.category == WasteCategory.PLASTIC
    assert item.quantity == 2

def test_waste_analysis():
    items = [
        WasteItem('Plastic Bottle', 'plastic', 3),
        WasteItem('Paper Bag', 'paper', 2),
        WasteItem('Apple Core', 'organic', 1)
    ]
    
    analyzer = WasteAnalyzer()
    analysis = analyzer.analyze_waste_data(items)
    
    assert analysis['total_waste'] == 6
    assert analysis['category_breakdown']['plastic'] == 3
    assert analysis['category_breakdown']['paper'] == 2
    assert analysis['category_breakdown']['organic'] == 1

def test_recommendations():
    items = [
        WasteItem('Plastic Bottle', 'plastic', 5),
        WasteItem('Plastic Bag', 'plastic', 3)
    ]
    
    analyzer = WasteAnalyzer()
    analysis = analyzer.analyze_waste_data(items)
    recommendations = analyzer.get_recommendations(analysis)
    
    assert len(recommendations) >= 1
    assert any('plastic' in rec.lower() for rec in recommendations)