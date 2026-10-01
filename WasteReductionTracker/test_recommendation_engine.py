import pytest
from models.recommendation_engine import RecommendationEngine

def test_recommendation_engine_initialization():
    engine = RecommendationEngine()
    assert hasattr(engine, 'tips')
    assert isinstance(engine.tips, dict)


def test_generate_recommendations_empty_data():
    engine = RecommendationEngine()
    recommendations = engine.generate_recommendations([])
    assert len(recommendations) == 1
    assert "Start tracking your waste" in recommendations[0]


def test_generate_recommendations_with_data():
    engine = RecommendationEngine()
    sample_data = [
        {"name": "plastic_bottle", "category": "plastic"},
        {"name": "plastic_bag", "category": "plastic"}
    ]
    recommendations = engine.generate_recommendations(sample_data)
    assert len(recommendations) >= 1
    assert len(recommendations) <= 3


def test_generate_recommendations_unknown_category():
    engine = RecommendationEngine()
    sample_data = [
        {"name": "unknown_item", "category": "unknown"}
    ]
    recommendations = engine.generate_recommendations(sample_data)
    assert len(recommendations) >= 1
    assert len(recommendations) <= 3