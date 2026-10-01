import sys
import os
import pytest

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.waste_item import WasteItem
from models.waste_category import WasteCategory
from recommendation_engine import RecommendationEngine

def test_recommendation_engine_empty():
    engine = RecommendationEngine()
    recommendations = engine.get_recommendations([])
    assert len(recommendations) >= 0

def test_recommendation_engine_plastic():
    engine = RecommendationEngine()
    plastic_item = WasteItem('Plastic bottle', WasteCategory.PLASTIC, 3)
    recommendations = engine.get_recommendations([plastic_item])
    assert any('plastic' in rec.lower() for rec in recommendations)

def test_recommendation_engine_multiple_categories():
    engine = RecommendationEngine()
    plastic_item = WasteItem('Plastic bottle', WasteCategory.PLASTIC, 3)
    paper_item = WasteItem('Newspaper', WasteCategory.PAPER, 2)
    organic_item = WasteItem('Food scraps', WasteCategory.ORGANIC, 1)
    recommendations = engine.get_recommendations([plastic_item, paper_item, organic_item])
    assert len(recommendations) > 0

def test_recommendation_engine_high_volume():
    engine = RecommendationEngine()
    items = [WasteItem(f'Item {i}', WasteCategory.OTHER) for i in range(15)]
    recommendations = engine.get_recommendations(items)
    assert any('reduce' in rec.lower() or 'overall' in rec.lower() for rec in recommendations)

def test_recommendation_engine_moderate_volume():
    engine = RecommendationEngine()
    items = [WasteItem(f'Item {i}', WasteCategory.OTHER) for i in range(7)]
    recommendations = engine.get_recommendations(items)
    assert any('reuse' in rec.lower() for rec in recommendations)