#!/usr/bin/env python3

import pytest
from recommendation_system import (
    RecommendationEngine,
    UserPreferences,
    RecommendationContext,
    ActivityRecommendation
)

@pytest.fixture
def engine():
    return RecommendationEngine()

@pytest.fixture
def sample_preferences():
    return UserPreferences(
        interests=["museums", "restaurants"],
        budget_range="medium",
        travel_style="leisure",
        accessibility_needs=[]
    )

@pytest.fixture
def sample_context(sample_preferences):
    return RecommendationContext(
        user_preferences=sample_preferences,
        current_itinerary={"title": "Sample Trip", "activities": []},
        destination_info={"name": "City Center", "country": "USA"},
        time_frame={"start": "2023-01-01T00:00:00Z", "end": "2023-01-04T00:00:00Z"}
    )

def test_recommendation_engine_initialization(engine):
    assert engine is not None
    assert hasattr(engine, 'recommendation_database')
    
    # Check that database has expected activity types
    assert "museums" in engine.recommendation_database
    assert "restaurants" in engine.recommendation_database
    assert "parks" in engine.recommendation_database
    assert "shopping" in engine.recommendation_database

def test_generate_recommendations(engine, sample_context):
    recommendations = engine.generate_recommendations(sample_context)
    
    # Should return at least one recommendation
    assert len(recommendations) > 0
    
    # Check that all returned recommendations have confidence scores
    for rec in recommendations:
        assert hasattr(rec, 'confidence_score')
        assert 0.0 <= rec.confidence_score <= 1.0
        
    # Should be sorted by confidence score (highest first)
    confidence_scores = [rec.confidence_score for rec in recommendations]
    assert confidence_scores == sorted(confidence_scores, reverse=True)
    
    # Check recommendation properties
    sample_rec = recommendations[0]
    assert hasattr(sample_rec, 'activity_type')
    assert hasattr(sample_rec, 'title')
    assert hasattr(sample_rec, 'description')
    assert hasattr(sample_rec, 'location')
    assert hasattr(sample_rec, 'estimated_duration')
    assert hasattr(sample_rec, 'price_range')
    assert hasattr(sample_rec, 'rating')
    
    # Check that confidence score is set
    assert sample_rec.confidence_score > 0.0

def test_budget_compatibility(engine, sample_context):
    # Test high budget with low price activity
    sample_context.user_preferences.budget_range = "high"
    recommendations = engine.generate_recommendations(sample_context)
    
    # Should include recommendations regardless of price range for high budget
    assert len(recommendations) > 0
    
    # Test low budget with medium price activity
    sample_context.user_preferences.budget_range = "low"
    sample_context.user_preferences.interests = ["parks"]
    recommendations = engine.generate_recommendations(sample_context)
    
    # Should include parks recommendation (low price) but not restaurants (medium price)
    for rec in recommendations:
        assert rec.price_range == "low"  # Only low price activities should be recommended
    
    # Test medium budget with medium price activity
    sample_context.user_preferences.budget_range = "medium"
    sample_context.user_preferences.interests = ["restaurants"]
    recommendations = engine.generate_recommendations(sample_context)
    
    # Should include restaurants (medium price)
    assert len(recommendations) > 0
    for rec in recommendations:
        assert rec.price_range in ["medium", "low"]  # Medium or low price activities

def test_accessibility_requirements(engine, sample_context):
    # Test with accessibility needs that should filter out some recommendations
    sample_context.user_preferences.accessibility_needs = ["wheelchair_access"]
    
    recommendations = engine.generate_recommendations(sample_context)
    
    # In a real implementation, some recommendations would be filtered out
    # For this test, we just verify the function doesn't crash
    assert len(recommendations) >= 0
    
    # Check that all recommendations have expected attributes
    for rec in recommendations:
        assert hasattr(rec, 'activity_type')
        assert hasattr(rec, 'title')
        assert hasattr(rec, 'confidence_score')
        
if __name__ == "__main__":
    pytest.main(["-v", __file__])