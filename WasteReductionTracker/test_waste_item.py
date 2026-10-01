import pytest
from models.waste_category import WasteCategory
from models.waste_item import WasteItem

def test_waste_item_creation():
    item = WasteItem('plastic bottle', WasteCategory.PLASTIC, 1.0)
    assert item.name == 'plastic bottle'
    assert item.category == WasteCategory.PLASTIC
    assert item.quantity == 1.0

def test_waste_item_to_dict():
    item = WasteItem('paper', WasteCategory.PAPER, 5.0)
    data = item.to_dict()
    assert data['name'] == 'paper'
    assert data['category'] == 'paper'
    assert data['quantity'] == 5.0