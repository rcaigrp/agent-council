import pytest
from models.waste_item import WasteItem
from models.sustainability_goal import SustainabilityGoal
from models.database import Base, engine, SessionLocal

def test_waste_item_model():
    # Test creating a waste item
    waste_item = WasteItem(
        item_name='Plastic Bottle',
        category='Plastic',
        weight_kg=0.5,
        notes='Recyclable'
    )
    
    assert waste_item.item_name == 'Plastic Bottle'
    assert waste_item.category == 'Plastic'
    assert waste_item.weight_kg == 0.5
    assert waste_item.notes == 'Recyclable'
    
    # Test dict conversion
    item_dict = waste_item.to_dict()
    assert item_dict['item_name'] == 'Plastic Bottle'
    assert item_dict['category'] == 'Plastic'
    assert item_dict['weight_kg'] == 0.5

def test_sustainability_goal_model():
    # Test creating a sustainability goal
    goal = SustainabilityGoal(
        title='Reduce Plastic Waste',
        description='Reduce plastic waste by 50% this month',
        target_amount=10,
        target_unit='kg',
        end_date='2024-12-31'
    )
    
    assert goal.title == 'Reduce Plastic Waste'
    assert goal.description == 'Reduce plastic waste by 50% this month'
    assert goal.target_amount == 10
    assert goal.target_unit == 'kg'
    
    # Test dict conversion
    goal_dict = goal.to_dict()
    assert goal_dict['title'] == 'Reduce Plastic Waste'
    assert goal_dict['target_amount'] == 10
    assert goal_dict['target_unit'] == 'kg'

def test_database_setup():
    # Test that database tables are created properly
    Base.metadata.create_all(bind=engine)
    
    # Test session creation
    session = SessionLocal()
    assert session is not None
    session.close()
