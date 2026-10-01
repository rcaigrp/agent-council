# models/goal.py

class SustainabilityGoal:
    def __init__(self, user_id, goal_type, target_amount, time_frame):
        self.user_id = user_id
        self.goal_type = goal_type  # e.g., 'reduce_plastic_waste'
        self.target_amount = target_amount  # e.g., 50 (percentage reduction)
        self.time_frame = time_frame  # e.g., 'monthly', 'quarterly', 'yearly'
        self.current_progress = 0
        self.created_at = None
        self.updated_at = None

    def update_progress(self, amount):
        self.current_progress += amount
        return self.current_progress

    def is_completed(self):
        return self.current_progress >= self.target_amount

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'goal_type': self.goal_type,
            'target_amount': self.target_amount,
            'time_frame': self.time_frame,
            'current_progress': self.current_progress,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }