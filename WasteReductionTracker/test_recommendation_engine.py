import sys
sys.path.append('../')
from models.recommendation_engine import generate_recommendations
import pandas as pd

def test_generate_recommendations():
    # Test data
    waste_data = pd.DataFrame({
        'category': ['plastic', 'paper', 'glass'],
        'amount': [10.5, 5.2, 3.8]
    })
    
    recommendations = generate_recommendations(waste_data)
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0