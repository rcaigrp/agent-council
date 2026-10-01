import sqlite3
from datetime import datetime, timedelta
class SustainabilityGoal:
    def __init__(self, user_id, target_type, target_value, start_date=None, end_date=None):
        self.user_id = user_id
        self.target_type = target_type  # e.g., 'waste_reduction', 'recycling_rate'
        self.target_value = target_value  # numerical goal value
        self.start_date = start_date or datetime.now()
        self.end_date = end_date
        self.created_at = datetime.now()
        self.is_active = True
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'target_type': self.target_type,
            'target_value': self.target_value,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
    
    @staticmethod
    def create_table():
        conn = sqlite3.connect('../waste_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sustainability_goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                target_type TEXT NOT NULL,
                target_value REAL NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT,
                created_at TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1
            )''')
        conn.commit()
        conn.close()