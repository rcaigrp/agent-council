from datetime import datetime

class SustainabilityGoal:
    def __init__(self, goal_id, description, target_amount, unit, start_date=None, end_date=None):
        self.goal_id = goal_id
        self.description = description
        self.target_amount = target_amount
        self.unit = unit
        self.start_date = start_date or datetime.now()
        self.end_date = end_date
        self.progress = 0

    def update_progress(self, amount):
        self.progress += amount
        if self.progress > self.target_amount:
            self.progress = self.target_amount

    def to_dict(self):
        return {
            'goal_id': self.goal_id,
            'description': self.description,
            'target_amount': self.target_amount,
            'unit': self.unit,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'progress': self.progress
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['goal_id'],
            data['description'],
            data['target_amount'],
            data['unit'],
            datetime.fromisoformat(data['start_date']),
            datetime.fromisoformat(data['end_date']) if data.get('end_date') else None
        )