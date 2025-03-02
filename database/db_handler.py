import sqlite3

class DBHandler:
    def __init__(self, db_name="hardware_assets.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)  # ✅ Fixes thread issue
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                serial_number TEXT UNIQUE NOT NULL,
                location TEXT,
                status TEXT
            )
        ''')
        self.conn.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

