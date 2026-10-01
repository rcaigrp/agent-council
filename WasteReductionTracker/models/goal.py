from datetime import datetime

class Goal:
    def __init__(self, id, user_id, title, target_amount, unit, deadline, created_at=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.target_amount = target_amount
        self.unit = unit
        self.deadline = deadline
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'target_amount': self.target_amount,
            'unit': self.unit,
            'deadline': self.deadline.isoformat() if isinstance(self.deadline, datetime) else self.deadline,
            'created_at': self.created_at.isoformat() if isinstance(self.deadline, datetime) else self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            user_id=data['user_id'],
            title=data['title'],
            target_amount=data['target_amount'],
            unit=data['unit'],
            deadline=datetime.fromisoformat(data['deadline']) if isinstance(data['deadline'], str) else data['deadline']
        )