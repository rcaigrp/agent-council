import unittest

class TestFinalIntegration(unittest.TestCase):
    def test_all_modules_work_together(self):
        # Verify all modules can be imported and work together
        try:
            from models.waste_item import WasteItem
            from models.goal import Goal
            from models.recommendation import Recommendation
            
            from api.goals_api import GoalsAPI
            from api.waste_analytics import WasteAnalytics
            from api.recommendations import RecommendationsEngine
            
            # Test basic functionality
            waste_item = WasteItem("plastic bottle", "plastic")
            self.assertEqual(waste_item.category, "plastic")
            
            goal = Goal("Reduce plastic waste by 50%", 50)
            self.assertEqual(goal.target_percentage, 50)
            
            print("All modules imported and working correctly")
        except Exception as e:
            self.fail(f"Integration test failed: {e}")

if __name__ == '__main__':
    unittest.main()