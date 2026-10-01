import pytest
from api.goals import GoalsManager

def test_create_goal():
    manager = GoalsManager()
    goal_id = manager.create_goal('Reduce plastic waste', '100g per week')
    assert goal_id is not None

def test_get_goal():
    manager = GoalsManager()
    goal = manager.get_goal(1)
    assert goal is not None