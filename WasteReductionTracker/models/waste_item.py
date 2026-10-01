from datetime import datetime

class WasteItem:
    def __init__(self, item_id, name, category, weight, date=None):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.weight = weight
        self.date = date or datetime.now()

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'weight': self.weight,
            'date': self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['item_id'],
            data['name'],
            data['category'],
            data['weight'],
            datetime.fromisoformat(data['date'])
        )