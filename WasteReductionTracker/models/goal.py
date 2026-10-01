class Goal:
    def __init__(self, goal_type, target_amount):
        self.goal_type = goal_type
        self.target_amount = target_amount
        self.current_amount = 0
        self.status = 'active'
        
    def to_dict(self):
        return {
            'goal_type': self.goal_type,
            'target_amount': self.target_amount,
            'current_amount': self.current_amount,
            'status': self.status
        }
        
    @classmethod
    def from_dict(cls, data):
        goal = cls(data['goal_type'], data['target_amount'])
        goal.current_amount = data.get('current_amount', 0)
        goal.status = data.get('status', 'active')
        return goal