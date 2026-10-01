import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'models'))
from goal_manager import GoalsManager

class TestGoalsManager(unittest.TestCase):
    def setUp(self):
        self.manager = GoalsManager(':memory:')

    def test_create_goal(self):
        goal_id = self.manager.create_goal('Reduce plastic waste', 50)
        self.assertIsNotNone(goal_id)
        
    def test_get_goal(self):
        goal_id = self.manager.create_goal('Reduce paper waste', 30)
        goal = self.manager.get_goal(goal_id)
        self.assertEqual(goal['name'], 'Reduce paper waste')
        
    def test_update_goal(self):
        goal_id = self.manager.create_goal('Reduce food waste', 20)
        self.manager.update_goal(goal_id, progress=10)
        goal = self.manager.get_goal(goal_id)
        self.assertEqual(goal['progress'], 10)

if __name__ == '__main__':
    unittest.main()