from datetime import datetime
class SustainabilityGoal:
    def __init__(self, description, target_amount, unit, deadline):
        self.description = description
        self.target_amount = target_amount
        self.unit = unit
        self.deadline = deadline
        self.created_at = datetime.now()
        self.completed = False

    def to_dict(self):
        return {
            'description': self.description,
            'target_amount': self.target_amount,
            'unit': self.unit,
            'deadline': self.deadline.isoformat(),
            'created_at': self.created_at.isoformat(),
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data['description'],
            target_amount=data['target_amount'],
            unit=data['unit'],
            deadline=datetime.fromisoformat(data['deadline'])
        )