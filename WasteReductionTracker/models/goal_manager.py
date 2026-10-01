import sqlite3
from datetime import datetime
from models.goal import SustainabilityGoal


class GoalsManager:
    def __init__(self, db_path="waste_tracker.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sustainability_goals (
                goal_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                title TEXT NOT NULL,
                target_amount REAL NOT NULL,
                unit TEXT NOT NULL,
                deadline DATE NOT NULL,
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def create_goal(self, goal):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sustainability_goals (goal_id, user_id, title, target_amount, unit, deadline, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            goal.goal_id,
            goal.user_id,
            goal.title,
            goal.target_amount,
            goal.unit,
            goal.deadline,
            goal.created_at,
            goal.updated_at
        ))
        conn.commit()
        conn.close()

    def get_goal(self, goal_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sustainability_goals WHERE goal_id = ?', (goal_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return SustainabilityGoal.from_dict({
                'goal_id': row[0],
                'user_id': row[1],
                'title': row[2],
                'target_amount': row[3],
                'unit': row[4],
                'deadline': datetime.fromisoformat(row[5]),
                'created_at': datetime.fromisoformat(row[6]),
                'updated_at': datetime.fromisoformat(row[7])
            })
        return None

    def update_goal(self, goal):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE sustainability_goals SET title=?, target_amount=?, unit=?, deadline=?, updated_at=?
            WHERE goal_id=?
        ''', (
            goal.title,
            goal.target_amount,
            goal.unit,
            goal.deadline,
            datetime.now(),
            goal.goal_id
        ))
        conn.commit()
        conn.close()

    def delete_goal(self, goal_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM sustainability_goals WHERE goal_id = ?', (goal_id,))
        conn.commit()
        conn.close()