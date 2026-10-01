class Category:
    def __init__(self, name, description, recyclable=False, compostable=False):
        self.name = name
        self.description = description
        self.recyclable = recyclable
        self.compostable = compostable

    @staticmethod
    def get_default_categories():
        return [
            Category('plastic', 'Plastic items like bottles, bags, containers', recyclable=True),
            Category('paper', 'Paper products including newspapers, magazines, boxes', recyclable=True),
            Category('glass', 'Glass bottles and jars', recyclable=True),
            Category('metal', 'Aluminum cans, steel containers', recyclable=True),
            Category('organic', 'Food scraps, yard waste', compostable=True),
            Category('hazardous', 'Batteries, electronics, chemicals', recyclable=False, compostable=False),
            Category('other', 'Items that don\'t fit in other categories')
        ]