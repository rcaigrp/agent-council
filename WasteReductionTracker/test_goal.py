import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.goal import Goal
from models.database import Database

class TestGoalsManager(unittest.TestCase):
    def setUp(self):
        self.db = Database('test_waste_tracker.db')
        
    def tearDown(self):
        # Clean up test database
        os.remove('test_waste_tracker.db')

    def test_create_goal(self):
        goal = Goal(
            id=None,
            user_id=1,
            title='Reduce plastic waste',
            target_amount=50.0,
            unit='grams',
            deadline='2024-12-31'
        )
        
        created_goal = self.db.create_goal(goal)
        self.assertIsNotNone(created_goal.id)
        self.assertEqual(created_goal.user_id, 1)
        self.assertEqual(created_goal.title, 'Reduce plastic waste')
        
    def test_get_goal(self):
        goal = Goal(
            id=None,
            user_id=1,
            title='Reduce plastic waste',
            target_amount=50.0,
            unit='grams',
            deadline='2024-12-31'
        )
        
        created_goal = self.db.create_goal(goal)
        retrieved_goal = self.db.get_goal(created_goal.id)
        
        self.assertEqual(retrieved_goal.title, 'Reduce plastic waste')
        
    def test_update_goal(self):
        goal = Goal(
            id=None,
            user_id=1,
            title='Reduce plastic waste',
            target_amount=50.0,
            unit='grams',
            deadline='2024-12-31'
        )
        
        created_goal = self.db.create_goal(goal)
        created_goal.target_amount = 75.0
        
        self.db.update_goal(created_goal)
        updated_goal = self.db.get_goal(created_goal.id)
        
        self.assertEqual(updated_goal.target_amount, 75.0)
        
    def test_delete_goal(self):
        goal = Goal(
            id=None,
            user_id=1,
            title='Reduce plastic waste',
            target_amount=50.0,
            unit='grams',
            deadline='2024-12-31'
        )
        
        created_goal = self.db.create_goal(goal)
        success = self.db.delete_goal(created_goal.id)
        
        self.assertTrue(success)
        
if __name__ == '__main__':
    unittest.main()