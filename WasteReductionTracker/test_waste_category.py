#!/usr/bin/env python3
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

import pytest
from models.waste_category import categorize_waste, WASTE_CATEGORIES, WasteCategory

def test_categorize_waste_existing_category():
    # Test existing categories
    result = categorize_waste('plastic bottle')
    assert result is not None
    assert result.name == 'Plastic'

    result = categorize_waste('paper newspaper')
    assert result is not None
    assert result.name == 'Paper'

    result = categorize_waste('glass jar')
    assert result is not None
    assert result.name == 'Glass'

def test_categorize_waste_no_match():
    # Test no match returns 'Other' category
    result = categorize_waste('something completely different')
    assert result is not None
    assert result.name == 'Other'

def test_waste_categories_exist():
    # Ensure all predefined categories exist
    assert len(WASTE_CATEGORIES) > 0
    for category in WASTE_CATEGORIES:
        assert category.name is not None
        assert category.description is not None

def test_waste_category_class():
    # Test WasteCategory class instantiation
    category = WasteCategory('Test', 'Test description')
    assert category.name == 'Test'
    assert category.description == 'Test description'

if __name__ == '__main__':
    pytest.main([__file__, '-v'])