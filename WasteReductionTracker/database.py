import sqlite3
from models.waste_item import WasteItem
from models.sustainability_goal import SustainabilityGoal

class Database:
    def __init__(self, db_path: str = 'waste_tracker.db'):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create waste_items table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS waste_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                weight REAL NOT NULL,
                date TEXT NOT NULL
            )''')
        
        # Create sustainability_goals table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sustainability_goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                target_date TEXT NOT NULL,
                current_progress INTEGER DEFAULT 0
            )''')
        
        conn.commit()
        conn.close()

    def add_waste_item(self, waste_item: WasteItem):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO waste_items (name, category, weight, date) VALUES (?, ?, ?, ?)',
            (waste_item.name, waste_item.category, waste_item.weight, waste_item.date)
        )
        conn.commit()
        conn.close()

    def get_waste_items(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM waste_items')
        items = cursor.fetchall()
        conn.close()
        return items

    def add_sustainability_goal(self, goal: SustainabilityGoal):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO sustainability_goals (description, target_date, current_progress) VALUES (?, ?, ?)',
            (goal.description, goal.target_date, goal.current_progress)
        )
        conn.commit()
        conn.close()

    def get_sustainability_goals(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sustainability_goals')
        goals = cursor.fetchall()
        conn.close()
        return goals
