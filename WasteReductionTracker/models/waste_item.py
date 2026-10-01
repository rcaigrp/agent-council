from models.waste_category import WasteCategory
class WasteItem:
    def __init__(self, name: str, category: WasteCategory, amount: float):
        self.name = name
        self.category = category
        self.amount = amount
