import pytest
from models.goal import Goal
from models.waste_item import WasteItem

def test_create_goal_table():
    Goal.create_table()
    # Test that table was created successfully
    conn = sqlite3.connect('../waste_tracker.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(goals)")
    columns = cursor.fetchall()
    assert len(columns) == 7  # id, user_id, target_category, target_amount, start_date, end_date, status
    conn.close()

def test_save_goal():
    goal = Goal(
        user_id=1,
        target_category='plastic',
        target_amount=50.0
    )
    saved_goal = Goal.save(goal)
    assert saved_goal.id is not None
    assert saved_goal.user_id == 1
    assert saved_goal.target_category == 'plastic'
    assert saved_goal.target_amount == 50.0

def test_get_goals_by_user():
    goals = Goal.get_by_user(1)
    assert isinstance(goals, list)

# Integration test with waste data
def test_goal_with_waste_data_integration():
    # Create a goal for plastic reduction
    goal = Goal(
        user_id=1,
        target_category='plastic',
        target_amount=30.0
    )
    saved_goal = Goal.save(goal)
    
    # Verify the goal was saved correctly
    retrieved_goals = Goal.get_by_user(1)
    assert len(retrieved_goals) == 1
    assert retrieved_goals[0].target_category == 'plastic'
    assert retrieved_goals[0].target_amount == 30.0