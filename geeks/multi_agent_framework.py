import sqlite3
import json

class Memory:
    def __init__(self, db_path="veritas_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS memory
                            (agent TEXT, input TEXT, output TEXT)''')

    def store(self, agent, input_text, output_text):
        self.conn.execute("INSERT INTO memory VALUES (?, ?, ?)", (agent, input_text, output_text))
        self.conn.commit()

    def fetch(self, agent):
        cursor = self.conn.execute("SELECT input, output FROM memory WHERE agent=?", (agent,))
        return [{"input": row[0], "output": row[1]} for row in cursor.fetchall()]
