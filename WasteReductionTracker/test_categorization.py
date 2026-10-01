import pytest
from models.waste_item import WasteItem

def test_waste_categorization():
    # Test plastic items
    assert WasteItem.categorize_waste('plastic bottle') == 'plastic'
    assert WasteItem.categorize_waste('Plastic Bag') == 'plastic'
    
    # Test paper items
    assert WasteItem.categorize_waste('newspaper') == 'paper'
    assert WasteItem.categorize_waste('Magazine') == 'paper'
    
    # Test organic items
    assert WasteItem.categorize_waste('food scraps') == 'organic'
    assert WasteItem.categorize_waste('fruit peel') == 'organic'
    
    # Test other items
    assert WasteItem.categorize_waste('wood') == 'other'
    assert WasteItem.categorize_waste('stone') == 'other'