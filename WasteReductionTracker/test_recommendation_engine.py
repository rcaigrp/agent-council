import pytest
import pandas as pd
from models.recommendation_engine import RecommendationEngine

def test_generate_recommendations():
    engine = RecommendationEngine()
    waste_data = pd.DataFrame({'category': ['plastic', 'paper', 'organic']})
    recommendations = engine.generate_recommendations(waste_data)
    assert len(recommendations) > 0