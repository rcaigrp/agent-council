import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models.waste_category import WasteCategory, WasteAnalyzer

def test_waste_categorization():
    assert WasteAnalyzer.categorize_waste('plastic') == WasteCategory.PLASTIC
    assert WasteAnalyzer.categorize_waste('PAPER') == WasteCategory.PAPER
    assert WasteAnalyzer.categorize_waste('organic') == WasteCategory.ORGANIC
    assert WasteAnalyzer.categorize_waste('metal') == WasteCategory.METAL
    assert WasteAnalyzer.categorize_waste('unknown') == WasteCategory.OTHER

def test_pattern_analysis():
    waste_data = [
        {'type': 'plastic', 'amount': 2},
        {'type': 'paper', 'amount': 1},
        {'type': 'plastic', 'amount': 3}
    ]
    result = WasteAnalyzer.analyze_patterns(waste_data)
    assert result[WasteCategory.PLASTIC] == 2
    assert result[WasteCategory.PAPER] == 1