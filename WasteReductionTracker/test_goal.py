import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
from models.goal import GoalsManager

class TestGoalsManager(unittest.TestCase):
    def setUp(self):
        self.goals_manager = GoalsManager()

    def test_create_goal(self):
        goal_id = self.goals_manager.create_goal("Reduce plastic waste by 50%", "monthly")
        self.assertIsNotNone(goal_id)

    def test_get_goal(self):
        goal_id = self.goals_manager.create_goal("Reduce paper waste by 30%", "weekly")
        goal = self.goals_manager.get_goal(goal_id)
        self.assertEqual(goal['description'], "Reduce paper waste by 30%")

    def test_update_goal(self):
        goal_id = self.goals_manager.create_goal("Reduce food waste by 25%", "daily")
        updated = self.goals_manager.update_goal(goal_id, "Reduce food waste by 40%")
        self.assertTrue(updated)

if __name__ == '__main__':
    unittest.main()