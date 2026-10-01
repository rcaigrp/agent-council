import pytest
from models.goal import Goal

def test_create_goal():
    goal_model = Goal()
    goal_id = goal_model.create_goal(1, 'waste_reduction', 50.0)
    assert goal_id > 0

def test_get_user_goals():
    goal_model = Goal()
    goals = goal_model.get_user_goals(1)
    assert isinstance(goals, list)

def test_update_progress():
    goal_model = Goal()
    goal_id = goal_model.create_goal(1, 'waste_reduction', 50.0)
    goal_model.update_progress(goal_id, 25.0)
    goal = goal_model.get_goal_by_id(goal_id)
    assert goal[4] == 25.0  # current_value