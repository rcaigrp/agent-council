from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class SustainabilityGoal:
    def __init__(self, id: int, description: str, target_date: str, current_progress: int = 0):
        self.id = id
        self.description = description
        self.target_date = target_date
        self.current_progress = current_progress

    @staticmethod
    def validate_fields(description: str, target_date: str) -> bool:
        return all([
            isinstance(description, str) and len(description) > 0,
            isinstance(target_date, str) and len(target_date) > 0
        ])
