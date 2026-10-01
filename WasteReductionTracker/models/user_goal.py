from datetime import datetime

class UserGoal:
    def __init__(self, id, description, target_weight, deadline, achieved=False):
        self.id = id
        self.description = description
        self.target_weight = target_weight  # in grams
        self.deadline = deadline
        self.achieved = achieved
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'target_weight': self.target_weight,
            'deadline': self.deadline.isoformat(),
            'achieved': self.achieved,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            description=data['description'],
            target_weight=data['target_weight'],
            deadline=datetime.fromisoformat(data['deadline']).date(),
            achieved=data.get('achieved', False)
        )