import pandas as pd
from datetime import datetime, timedelta

class Goals:
    def __init__(self):
        self.goals_data = {}

    def create_goal(self, user_id, goal_type, target_amount, time_period):
        goal_id = f"goal_{len(self.goals_data) + 1}"
        self.goals_data[goal_id] = {
            'user_id': user_id,
            'goal_type': goal_type,  # e.g., 'reduce_plastic_waste', 'total_waste'
            'target_amount': target_amount,
            'time_period': time_period,  # e.g., 'weekly', 'monthly'
            'start_date': datetime.now(),
            'created_at': datetime.now()
        }
        return goal_id

    def get_user_goals(self, user_id):
        return [goal for goal in self.goals_data.values() if goal['user_id'] == user_id]

    def update_goal_progress(self, goal_id, current_amount):
        if goal_id in self.goals_data:
            self.goals_data[goal_id]['current_amount'] = current_amount
            return True
        return False

    def get_goal_progress(self, goal_id):
        if goal_id in self.goals_data:
            goal = self.goals_data[goal_id]
            progress = (goal.get('current_amount', 0) / goal['target_amount']) * 100
            return {
                'progress_percentage': min(progress, 100),
                'remaining_amount': max(0, goal['target_amount'] - goal.get('current_amount', 0))
            }
        return None