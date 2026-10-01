import sqlite3
from datetime import datetime
from models.goal import Goal

class Database:
    def __init__(self, db_path='waste_tracker.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create goals table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                target_amount REAL NOT NULL,
                unit TEXT NOT NULL,
                deadline DATE NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )''')
        
        conn.commit()
        conn.close()

    def create_goal(self, goal):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO goals (user_id, title, target_amount, unit, deadline)
            VALUES (?, ?, ?, ?, ?)''', (
                goal.user_id,
                goal.title,
                goal.target_amount,
                goal.unit,
                goal.deadline
            ))
        
        goal.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return goal

    def get_goal(self, goal_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM goals WHERE id = ?', (goal_id,))
        row = cursor.fetchone()
        
        conn.close()
        
        if row:
            return Goal.from_dict({
                'id': row[0],
                'user_id': row[1],
                'title': row[2],
                'target_amount': row[3],
                'unit': row[4],
                'deadline': row[5],
                'created_at': row[6]
            })
        return None

    def update_goal(self, goal):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE goals SET title=?, target_amount=?, unit=?, deadline=?
            WHERE id=?''', (
                goal.title,
                goal.target_amount,
                goal.unit,
                goal.deadline,
                goal.id
            ))
        
        conn.commit()
        conn.close()
        return True

    def delete_goal(self, goal_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM goals WHERE id = ?', (goal_id,))
        deleted = cursor.rowcount > 0
        
        conn.commit()
        conn.close()
        return deleted