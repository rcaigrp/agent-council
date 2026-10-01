class WasteItem:
    def __init__(self, id, name, category, weight, date):
        self.id = id
        self.name = name
        self.category = category  # e.g., 'plastic', 'paper', 'organic'
        self.weight = weight  # in grams
        self.date = date  # YYYY-MM-DD

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'weight': self.weight,
            'date': self.date
        }