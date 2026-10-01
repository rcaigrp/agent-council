import json
class WasteDataCollector:
    def __init__(self):
        self.data = []
    
    def add_waste_item(self, item_type, quantity, date):
        waste_entry = {
            'item_type': item_type,
            'quantity': quantity,
            'date': date
        }
        self.data.append(waste_entry)
        return waste_entry
    
    def get_all_data(self):
        return self.data