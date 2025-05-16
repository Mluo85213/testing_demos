import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "test.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", 
                   ("eve.holt@reqres.in", "cityslicka"))

    conn.commit()
    conn.close()
    print(f"✅ 数据库初始化完成，路径：{DB_PATH}")

if __name__ == "__main__":
    init_db()
