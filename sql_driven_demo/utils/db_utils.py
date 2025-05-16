import sqlite3
import os

def get_user_info(user_id):
    db_path = os.path.join("data", "test.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users WHERE id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return {"email": row[0]} if row else {}

