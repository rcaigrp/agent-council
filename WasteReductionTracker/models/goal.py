import sqlite3
from datetime import datetime, timedelta
class Goal:
    def __init__(self, id=None, user_id=None, target_category=None, target_amount=0, start_date=None, end_date=None, status='active'):
        self.id = id
        self.user_id = user_id
        self.target_category = target_category
        self.target_amount = target_amount
        self.start_date = start_date or datetime.now().strftime('%Y-%m-%d')
        self.end_date = end_date
        self.status = status
    
    @staticmethod
    def create_table():
        conn = sqlite3.connect('../waste_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                target_category TEXT NOT NULL,
                target_amount REAL NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT,
                status TEXT DEFAULT 'active'
            )''')
        conn.commit()
        conn.close()
    
    @staticmethod
    def save(goal):
        conn = sqlite3.connect('../waste_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO goals (user_id, target_category, target_amount, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, ?)''', 
            (goal.user_id, goal.target_category, goal.target_amount, goal.start_date, goal.end_date, goal.status))
        conn.commit()
        goal.id = cursor.lastrowid
        conn.close()
        return goal
    
    @staticmethod
    def get_by_user(user_id):
        conn = sqlite3.connect('../waste_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM goals WHERE user_id = ?', (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Goal(*row) for row in rows]
    
    @staticmethod
    def update(goal):
        conn = sqlite3.connect('../waste_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE goals SET target_category=?, target_amount=?, end_date=?, status=?
            WHERE id=?''', (goal.target_category, goal.target_amount, goal.end_date, goal.status, goal.id))
        conn.commit()
        conn.close()
        return goal