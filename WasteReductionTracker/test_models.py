import pytest
from models.waste_item import WasteItem
from models.sustainability_goal import SustainabilityGoal

def test_waste_item_creation():
    item = WasteItem('1', 'Plastic Bottle', 'Plastic', 0.5)
    assert item.name == 'Plastic Bottle'
    assert item.category == 'Plastic'
    assert item.weight == 0.5

def test_sustainability_goal_creation():
    goal = SustainabilityGoal('1', 'Reduce plastic waste by 50%', 10, 'kg')
    assert goal.description == 'Reduce plastic waste by 50%'
    assert goal.target_amount == 10
    assert goal.unit == 'kg'

def test_goal_progress_update():
    goal = SustainabilityGoal('1', 'Reduce plastic waste by 50%', 10, 'kg')
    goal.update_progress(3)
    assert goal.progress == 3

    goal.update_progress(5)
    assert goal.progress == 8