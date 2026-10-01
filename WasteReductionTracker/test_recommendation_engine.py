import pytest
from models.recommendation import generate_recommendation

def test_generate_recommendation():
    result = generate_recommendation('plastic')
    assert result is not None
    assert isinstance(result, str)

def test_generate_recommendation_empty_input():
    result = generate_recommendation('')
    assert result is not None