from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class WasteItem:
    def __init__(self, id: int, name: str, category: str, weight: float, date: str):
        self.id = id
        self.name = name
        self.category = category
        self.weight = weight
        self.date = date

    @staticmethod
    def validate_fields(name: str, category: str, weight: float) -> bool:
        return all([
            isinstance(name, str) and len(name) > 0,
            isinstance(category, str) and len(category) > 0,
            isinstance(weight, (int, float)) and weight >= 0
        ])
